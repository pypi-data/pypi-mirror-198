import json
from PyQt5.QtCore import QUrl, Qt, QPointF, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWidgets import QApplication, QShortcut, QSystemTrayIcon

class Wrap:
    class PyApp(QObject):
        event_occurred = pyqtSignal(str, list)

        @pyqtSlot(str, str)
        def handle_js_event(self, event_name, data):
            self.event_occurred.emit(event_name, json.loads(data))

    def __init__(self, html_file, title=None, icon=None, width=1024, height=768, expandable=True,
                 disable_right_click=False, hide_top_bar=False, hide_status_bar=False, clear_cache=False,
                 disable_javascript=False, disable_keyboard_shortcuts=False):
        self.app = QApplication([])
        if title:
            self.app.setApplicationDisplayName(title)
        if icon:
            self.app.setWindowIcon(QIcon(icon))

        self.view = QWebEngineView()
        self.view.setObjectName("WebView")

        if expandable:
            self.view.setMinimumSize(width, height)
        else:
            self.view.setFixedSize(width, height)

        self.view.setUrl(QUrl.fromLocalFile(html_file))

        self.channel = QWebChannel(self.view.page())
        self.pyapp = Wrap.PyApp()
        self.channel.registerObject("pyapp", self.pyapp)
        self.view.page().setWebChannel(self.channel)

        self.view.page().javaScriptConsoleMessage = self._console_message

        if disable_right_click:
            self.view.setContextMenuPolicy(Qt.NoContextMenu)

        if hide_top_bar:
            self.view.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        if hide_status_bar:
            self.view.setStatusBarVisible(False)

        if clear_cache:
            self.view.page().profile().clearAllVisitedLinks()
            self.view.page().profile().clearHttpCache()
            self.view.page().profile().clearAllVisitedLinks()

        if disable_javascript:
            settings = self.view.settings()
            settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

        if disable_keyboard_shortcuts:
            self.view.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, False)
            self.view.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, False)

    def _console_message(self, level, message, line, source_id):
        if level == 0:  # log
            print(message)

    def run(self):
        self.view.show()
        self.app.exec_()

    def call_js_function(self, function_name, *args):
        script = "{}({});".format(function_name, ", ".join(str(arg) for arg in args))
        self.view.page().runJavaScript(script)

    def handle_js_event(self, event_name, handler):
        self.pyapp.event_occurred.connect(lambda name, data: handler(data) if name == event_name else None)
        self.view.page().runJavaScript("window.pyapp.handle_js_event('{}', JSON.stringify);".format(event_name))

    def emit_js_event(self, event_name, *args):
        script = "var event = new CustomEvent('{}', {{ detail: {} }}); window.dispatchEvent(event);".format(event_name,
                                                                                                            json.dumps(
                                                                                                                args))
        self.view.page().runJavaScript(script)

    def toggle_fullscreen(self, shortcut=None):
        if shortcut:
            QShortcut(QKeySequence(shortcut), self.view, self.toggle_fullscreen)

        if self.view.isFullScreen():
            self.view.showNormal()
        else:
            self.view.showFullScreen()

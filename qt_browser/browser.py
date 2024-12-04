import sys
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtCore import QUrl, QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLabel,
    QLineEdit,
    QFileDialog,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QTabWidget
)

from paths import Paths

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        navtb = QToolBar('Navigation')
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(
            QIcon(Paths.icon('arrow-180.png')), 'Back', self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(
            lambda: self.tabs.currentWidget().back()
        )
        navtb.addAction(back_btn)

        next_btn = QAction(
            QIcon(Paths.icon('arrow-000.png')), 'Forward', self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(
            lambda: self.tabs.currentWidget().forward()
        )
        navtb.addAction(next_btn)

        reload_btn = QAction(
            QIcon(Paths.icon('arrow-circle-315.png')), 'Reload', self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload()
        )
        navtb.addAction(reload_btn)

        home_btn = QAction(
            QIcon(Paths.icon('home.png')), 'Home', self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        self.https_icon = QLabel()
        self.https_icon.setPixmap(QPixmap(Paths.icon('lock-nossl.png')))
        navtb.addWidget(self.https_icon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(
            QIcon(Paths.icon('cross-circle.png')), 'Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(
            lambda: self.tabs.currentWidget().stop()
        )
        navtb.addAction(stop_btn)

        file_menu = self.menuBar().addMenu('&File')

        open_file_action = QAction(
            QIcon(Paths.icon('disk--arrow.png')),
            'Open file...',
            self,
        )
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(
            QIcon(Paths.icon('disk--pencil.png')),
            'Save as...',
            self,
        )
        save_file_action.setStatusTip('Save current page to file')
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(
            QIcon(Paths.icon('printer.png')), 'Print...', self)
        print_action.setStatusTip('Print current page')
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        self.printer = QPrinter()

        help_menu = self.menuBar().addMenu('&Help')
        about_action = QAction(
            QIcon(Paths.icon('question.png')),
            'About My Brower',
            self,
        )
        about_action.setStatusTip('Find out more about My Brower')
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_browser_action = QAction(
            QIcon(Paths.icon('lifebuoy.png')),
            'My Browers Homepage',
            self,
        )
        navigate_browser_action.triggered.connect(self.navigate_browser)
        help_menu.addAction(navigate_browser_action)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_dubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.add_new_tab(QUrl("https://www.google.com"))

        self.setCentralWidget(self.tabs)
        self.show()

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == '':
            q.setScheme('http')
        self.tabs.currentWidget().setUrl(q)
    
    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        if q.scheme() == 'https':
            self.https_icon.setPixmap(
                QPixmap(Paths.icon('lock-ssl.png')))
        else:
            self.https_icon.setPixmap(
                QPixmap(Paths.icon('lock-nossl.png')))
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def update_title(self, browser):
        if  browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(f'{title} - My browser')

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            'Open file',
            '',
            'Hypertext Markup Language (*.htm *.html);;'
            'All files (*.*)',
        )
        if filename:
            with open(filename, 'r') as f:
                html = f.read()
            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Save page as',
            '',
            'Hypertext Markup Language (*.htm *.html);;'
            'All files (*.*)',
        )
        if filename:
            def writer(html):
                with open(filename, w) as f:
                    f.write(html)
        self.tabs.currentWidget().page().toHtml(writer)

    def print_page(self):
        page = self.browser.page()
        def call_back(*args):
            pass

        dlg = QPrintDialog(self.printer)
        dlg.accepted.connect(call_back)
        if dlg.exec() == QDialog.Accepted:
            page.print(self.printer, call_back)
    
    def navigate_browser(self):
        self.tabs.currentWidget().setUrl("https://www.pythonguis.com/")

    def about(self):
        dlg = AboutDialog()
        dlg.exec()

    def tab_open_dubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def add_new_tab(self, qurl=None, label='Blank'):
        if qurl is None:
            qurl = QUrl(qurl)
        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(
                qurl, browser
            )
        )
        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(
                i, browser.page().title()
            )
        )

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel('My Browser')
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(Paths.icon('ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel('Version 1'))
        layout.addWidget(QLabel('Copyright 2024 My Browser inc.'))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
app.exec()


        # self.browser = QWebEngineView()
        # self.browser.setUrl(QUrl("https://www.google.com"))     
        # self.browser.urlChanged.connect(self.update_urlbar)
        # self.browser.loadFinished.connect(self.update_title)

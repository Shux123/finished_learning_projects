# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        if not QMainWindow.objectName():
            QMainWindow.setObjectName(u"QMainWindow")
        QMainWindow.resize(281, 356)
        self.centralwidget = QWidget(QMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todo_view = QListView(self.centralwidget)
        self.todo_view.setObjectName(u"todo_view")

        self.verticalLayout.addWidget(self.todo_view)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_delete = QPushButton(self.widget)
        self.button_delete.setObjectName(u"button_delete")

        self.horizontalLayout.addWidget(self.button_delete)

        self.button_complete = QPushButton(self.widget)
        self.button_complete.setObjectName(u"button_complete")

        self.horizontalLayout.addWidget(self.button_complete)


        self.verticalLayout.addWidget(self.widget)

        self.todo_edit = QLineEdit(self.centralwidget)
        self.todo_edit.setObjectName(u"todo_edit")

        self.verticalLayout.addWidget(self.todo_edit)

        self.button_add_todo = QPushButton(self.centralwidget)
        self.button_add_todo.setObjectName(u"button_add_todo")

        self.verticalLayout.addWidget(self.button_add_todo)

        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 281, 33))
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QMainWindow)

        QMetaObject.connectSlotsByName(QMainWindow)
    # setupUi

    def retranslateUi(self, QMainWindow):
        QMainWindow.setWindowTitle(QCoreApplication.translate("QMainWindow", u"To do", None))
        self.button_delete.setText(QCoreApplication.translate("QMainWindow", u"Delete", None))
        self.button_complete.setText(QCoreApplication.translate("QMainWindow", u"Complete", None))
        self.button_add_todo.setText(QCoreApplication.translate("QMainWindow", u"Add to do", None))
    # retranslateUi


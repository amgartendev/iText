# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledjEjYmh.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"")
        self.pushButton = QPushButton(self.login_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 400, 410, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #007AFF;\n"
"	color: #FFFFFF;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1F8AFF;\n"
"}")
        self.lineEdit = QLineEdit(self.login_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(210, 240, 410, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.lineEdit_2 = QLineEdit(self.login_page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 310, 410, 30))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(self.login_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 80, 100, 50))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"}")
        self.label_2 = QLabel(self.login_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 130, 240, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #707070;\n"
"}")
        self.pushButton_2 = QPushButton(self.login_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 460, 411, 24))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: #F3F3F3;\n"
"	border: none;\n"
"}")
        self.pushButton_3 = QPushButton(self.login_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 310, 75, 24))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background-color: #F3F3F3;\n"
"	color: #007AFF;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #1F8AFF;\n"
"}")
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.stackedWidget.addWidget(self.signup_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"L o g   I n", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Please sign in to continue.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? Sign up here", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"FORGOT", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacelCPgAG.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import qtawesome
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton,
                               QScrollArea, QSizePolicy, QStackedWidget,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 564)
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
        self.button_login = QPushButton(self.login_page)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(210, 400, 410, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.button_login.setFont(font)
        self.button_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_login.setStyleSheet(u"QPushButton {\n"
"	background-color: #007AFF;\n"
"	color: #FFFFFF;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1F8AFF;\n"
"}")
        self.input_username = QLineEdit(self.login_page)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setGeometry(QRect(210, 240, 410, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.input_username.setFont(font1)
        self.input_username.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_password = QLineEdit(self.login_page)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(210, 310, 410, 30))
        self.input_password.setFont(font1)
        self.input_password.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_login = QLabel(self.login_page)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(210, 80, 100, 50))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.label_login.setFont(font2)
        self.label_login.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"}")
        self.label_login_description = QLabel(self.login_page)
        self.label_login_description.setObjectName(u"label_login_description")
        self.label_login_description.setGeometry(QRect(210, 130, 240, 30))
        self.label_login_description.setFont(font)
        self.label_login_description.setStyleSheet(u"QLabel {\n"
"	color: #707070;\n"
"}")
        self.button_signup = QPushButton(self.login_page)
        self.button_signup.setObjectName(u"button_signup")
        self.button_signup.setGeometry(QRect(210, 460, 411, 24))
        self.button_signup.setFont(font1)
        self.button_signup.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_signup.setStyleSheet(u"QPushButton {\n"
"	background-color: #F3F3F3;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #F3F3F3;\n"
"	border: none;\n"
"	text-decoration: underline;\n"
"}")
        self.button_forgot_password = QPushButton(self.login_page)
        self.button_forgot_password.setObjectName(u"button_forgot_password")
        self.button_forgot_password.setGeometry(QRect(630, 310, 75, 24))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.button_forgot_password.setFont(font3)
        self.button_forgot_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_forgot_password.setStyleSheet(u"QPushButton {\n"
"	background-color: #F3F3F3;\n"
"	color: #007AFF;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #1F8AFF;\n"
"}")
        self.label_error_message = QLabel(self.login_page)
        self.label_error_message.setObjectName(u"label_error_message")
        self.label_error_message.setEnabled(True)
        self.label_error_message.setHidden(True)
        self.label_error_message.setGeometry(QRect(210, 360, 411, 25))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_error_message.setFont(font4)
        self.label_error_message.setStyleSheet(u"QLabel {\n"
"	color: #F2244A;\n"
"}")
        self.label_error_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_reveal_password = QPushButton(self.login_page)
        self.button_reveal_password.setObjectName(u"button_reveal_password")
        self.button_reveal_password.setGeometry(QRect(160, 305, 40, 40))
        self.button_reveal_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_reveal_password.setIcon(qtawesome.icon("fa5.eye", color="#007AFF"))
        self.button_reveal_password.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.button_reveal_password.setIconSize(QSize(22, 22))
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.input_signup_firstname = QLineEdit(self.signup_page)
        self.input_signup_firstname.setObjectName(u"input_signup_firstname")
        self.input_signup_firstname.setGeometry(QRect(160, 160, 221, 31))
        self.input_signup_firstname.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_signup_lastname = QLineEdit(self.signup_page)
        self.input_signup_lastname.setObjectName(u"input_signup_lastname")
        self.input_signup_lastname.setGeometry(QRect(410, 160, 221, 31))
        self.input_signup_lastname.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_signup_username = QLineEdit(self.signup_page)
        self.input_signup_username.setObjectName(u"input_signup_username")
        self.input_signup_username.setGeometry(QRect(160, 250, 221, 31))
        self.input_signup_username.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_signup_password = QLineEdit(self.signup_page)
        self.input_signup_password.setObjectName(u"input_signup_password")
        self.input_signup_password.setGeometry(QRect(410, 250, 221, 31))
        self.input_signup_password.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_signup_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_signup_confirm_password = QLineEdit(self.signup_page)
        self.input_signup_confirm_password.setObjectName(u"input_signup_confirm_password")
        self.input_signup_confirm_password.setGeometry(QRect(160, 350, 221, 31))
        self.input_signup_confirm_password.setStyleSheet(u"QLineEdit {\n"
"	background-color: #F3F3F3;\n"
"	border: 1px solid #F3F3F3;\n"
"	border-bottom-color: grey;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom-color: #007AFF;\n"
"}")
        self.input_signup_confirm_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(self.signup_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 140, 81, 16))
        self.label.setFont(font4)
        self.label_2 = QLabel(self.signup_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 140, 81, 16))
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.signup_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 230, 81, 16))
        self.label_3.setFont(font4)
        self.label_4 = QLabel(self.signup_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 230, 81, 16))
        self.label_4.setFont(font4)
        self.label_5 = QLabel(self.signup_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 330, 131, 16))
        self.label_5.setFont(font4)
        self.button_create_account = QPushButton(self.signup_page)
        self.button_create_account.setObjectName(u"button_create_account")
        self.button_create_account.setGeometry(QRect(210, 460, 410, 40))
        self.button_create_account.setFont(font)
        self.button_create_account.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_create_account.setStyleSheet(u"QPushButton {\n"
"	background-color: #007AFF;\n"
"	color: #FFFFFF;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1F8AFF;\n"
"}")
        self.button_back_to_login = QPushButton(self.signup_page)
        self.button_back_to_login.setObjectName(u"button_back_to_login")
        self.button_back_to_login.setGeometry(QRect(210, 520, 411, 24))
        self.button_back_to_login.setFont(font1)
        self.button_back_to_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_back_to_login.setStyleSheet(u"QPushButton {\n"
"	background-color: #F3F3F3;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #F3F3F3;\n"
"	border: none;\n"
"	text-decoration: underline;\n"
"}")
        self.label_error_message_firstname = QLabel(self.signup_page)
        self.label_error_message_firstname.setObjectName(u"label_error_message_firstname")
        self.label_error_message_firstname.setGeometry(QRect(160, 200, 221, 21))
        self.label_error_message_firstname.setFont(font4)
        self.label_error_message_firstname.setHidden(True)
        self.label_error_message_firstname.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")
        self.label_error_message_firstname.setWordWrap(True)
        self.label_error_message_lastname = QLabel(self.signup_page)
        self.label_error_message_lastname.setObjectName(u"label_error_message_lastname")
        self.label_error_message_lastname.setGeometry(QRect(410, 200, 221, 21))
        self.label_error_message_lastname.setFont(font4)
        self.label_error_message_lastname.setHidden(True)
        self.label_error_message_lastname.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")
        self.label_error_message_lastname.setWordWrap(True)
        self.label_error_message_username = QLabel(self.signup_page)
        self.label_error_message_username.setObjectName(u"label_error_message_username")
        self.label_error_message_username.setGeometry(QRect(160, 290, 221, 21))
        self.label_error_message_username.setFont(font4)
        self.label_error_message_username.setHidden(True)
        self.label_error_message_username.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")
        self.label_error_message_username.setWordWrap(True)
        self.label_error_message_confirm_password = QLabel(self.signup_page)
        self.label_error_message_confirm_password.setObjectName(u"label_error_message_confirm_password")
        self.label_error_message_confirm_password.setGeometry(QRect(160, 390, 221, 21))
        self.label_error_message_confirm_password.setFont(font4)
        self.label_error_message_confirm_password.setHidden(True)
        self.label_error_message_confirm_password.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")
        self.label_error_message_confirm_password.setWordWrap(True)
        self.label_error_message_password = QLabel(self.signup_page)
        self.label_error_message_password.setObjectName(u"label_error_message_password")
        self.label_error_message_password.setGeometry(QRect(410, 290, 221, 41))
        self.label_error_message_password.setFont(font4)
        self.label_error_message_password.setHidden(True)
        self.label_error_message_password.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}")
        self.label_error_message_password.setWordWrap(True)
        self.label_signup_description = QLabel(self.signup_page)
        self.label_signup_description.setObjectName(u"label_signup_description")
        self.label_signup_description.setGeometry(QRect(150, 80, 191, 30))
        self.label_signup_description.setFont(font)
        self.label_signup_description.setStyleSheet(u"QLabel {\n"
"	color: #707070;\n"
"}")
        self.label_signup = QLabel(self.signup_page)
        self.label_signup.setObjectName(u"label_signup")
        self.label_signup.setGeometry(QRect(150, 30, 131, 50))
        self.label_signup.setFont(font2)
        self.label_signup.setStyleSheet(u"QLabel {\n"
"	color: #000000;\n"
"}")
        self.label_signup_success_message = QLabel(self.signup_page)
        self.label_signup_success_message.setObjectName(u"label_signup_success_message")
        self.label_signup_success_message.setGeometry(QRect(220, 430, 401, 21))
        self.label_signup_success_message.setFont(font4)
        self.label_signup_success_message.setHidden(True)
        self.label_signup_success_message.setStyleSheet(u"color: #13c248;")
        self.label_signup_success_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_signup_reveal_confirm_password = QPushButton(self.signup_page)
        self.button_signup_reveal_confirm_password.setObjectName(u"button_signup_reveal_confirm_password")
        self.button_signup_reveal_confirm_password.setGeometry(QRect(390, 350, 40, 40))
        self.button_signup_reveal_confirm_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_signup_reveal_confirm_password.setIcon(qtawesome.icon("fa5.eye", color="#007AFF"))
        self.button_signup_reveal_confirm_password.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.button_signup_reveal_confirm_password.setIconSize(QSize(22, 22))
        self.button_signup_reveal_password = QPushButton(self.signup_page)
        self.button_signup_reveal_password.setObjectName(u"button_signup_reveal_password")
        self.button_signup_reveal_password.setGeometry(QRect(640, 250, 40, 40))
        self.button_signup_reveal_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_signup_reveal_password.setIcon(qtawesome.icon("fa5.eye", color="#007AFF"))
        self.button_signup_reveal_password.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.button_signup_reveal_password.setIconSize(QSize(22, 22))
        self.stackedWidget.addWidget(self.signup_page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout = QHBoxLayout(self.main_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(210, 16777215))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #E0E0DF;\n"
"	border-right: 1.5px solid #CCCFCD;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_add_contact = QPushButton(self.frame)
        self.button_add_contact.setObjectName(u"button_add_contact")
        self.button_add_contact.setMaximumSize(QSize(40, 40))
        self.button_add_contact.setIcon(qtawesome.icon("fa5s.user-plus"))
        self.button_add_contact.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.button_add_contact)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: #E0E0DF;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 208, 468))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame #frame_2 {\n"
"	background-color: #E0E0DF;\n"
"	border-top: 1.5px solid #CCCFCD;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_profile = QLabel(self.frame_2)
        self.image_profile.setObjectName(u"image_profile")
        self.image_profile.setMaximumSize(QSize(80, 16777215))
        self.image_profile.setStyleSheet(u"")
        self.image_profile.setPixmap(QPixmap(u":/images/background.jpg"))
        self.image_profile.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.image_profile)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.label_profile_name = QLabel(self.frame_7)
        self.label_profile_name.setObjectName(u"label_profile_name")
        font5 = QFont()
        font5.setBold(True)
        self.label_profile_name.setFont(font5)
        self.label_profile_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profile_name.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_profile_name)

        self.label_username = QLabel(self.frame_7)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_username.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_username)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: #E0E0DF;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.button_settings = QPushButton(self.frame_8)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.button_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: #E0E0DF;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.button_settings.setIcon(icon)

        self.verticalLayout_5.addWidget(self.button_settings)

        self.button_logout = QPushButton(self.frame_8)
        self.button_logout.setObjectName(u"button_logout")
        self.button_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_logout.setStyleSheet(u"QPushButton {\n"
"	background-color: #E0E0DF;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.button_logout.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.button_logout)


        self.horizontalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.main_page)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(16777215, 70))
        self.frame_4.setStyleSheet(u"QFrame #frame_4 {\n"
"	background-color: #F3F3F2;\n"
"	border-bottom: 1.5px solid #CCCFCD;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image_contact = QLabel(self.frame_4)
        self.image_contact.setObjectName(u"image_contact")
        self.image_contact.setMaximumSize(QSize(80, 16777215))
        self.image_contact.setStyleSheet(u"")
        self.image_contact.setPixmap(QPixmap(u":/images/background.jpg"))
        self.image_contact.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.image_contact)

        self.label_contact_name = QLabel(self.frame_4)
        self.label_contact_name.setObjectName(u"label_contact_name")
        self.label_contact_name.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_contact_name)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 592, 489))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.scroll_layout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.addWidget(self.scrollArea_2)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.input_message = QLineEdit(self.frame_5)
        self.input_message.setObjectName(u"input_message")
        font6 = QFont()
        font6.setPointSize(9)
        self.input_message.setFont(font6)

        self.horizontalLayout_4.addWidget(self.input_message)

        self.button_send_message = QPushButton(self.frame_5)
        self.button_send_message.setObjectName(u"button_send_message")
        self.button_send_message.setIcon(qtawesome.icon("fa5.paper-plane"))
        self.button_send_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.button_send_message)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.main_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)




        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_login.setText(QCoreApplication.translate("MainWindow", u"L o g   I n", None))
        self.input_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_login_description.setText(QCoreApplication.translate("MainWindow", u"Please sign in to continue.", None))
        self.button_signup.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? Sign up here", None))
        self.button_forgot_password.setText(QCoreApplication.translate("MainWindow", u"FORGOT", None))
        self.label_error_message.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.button_reveal_password.setText("")
        self.button_reveal_password.setText("")
        self.input_signup_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.input_signup_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.input_signup_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.input_signup_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.input_signup_confirm_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Confirm password", None))
        self.button_create_account.setText(QCoreApplication.translate("MainWindow", u"C r e a t e   A c c o u n t", None))
        self.button_back_to_login.setText(QCoreApplication.translate("MainWindow", u"Go back to log in", None))
        self.label_error_message_firstname.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.label_error_message_lastname.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.label_error_message_username.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.label_error_message_confirm_password.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.label_error_message_password.setText(QCoreApplication.translate("MainWindow", u"Error Message Placeholder", None))
        self.label_signup_description.setText(QCoreApplication.translate("MainWindow", u"Create your account.", None))
        self.label_signup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_signup_success_message.setText(QCoreApplication.translate("MainWindow", u"Account successfully created! Go back to the login page.", None))
        self.button_signup_reveal_confirm_password.setText("")
        self.button_add_contact.setText("")
        self.image_profile.setText("")
        self.label_profile_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.button_settings.setText("")
        self.button_logout.setText("")
        self.image_contact.setText("")
        self.label_contact_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.input_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Start writing here...", None))
        self.button_send_message.setText("")
    # retranslateUi

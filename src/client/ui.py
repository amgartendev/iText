# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uirpIQel.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QListView, QListWidget,
                               QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("")
        self.login_window = QWidget()
        self.login_window.setObjectName("login_window")
        self.stackedWidget.addWidget(self.login_window)
        self.main_window = QWidget()
        self.main_window.setObjectName("main_window")
        self.horizontalLayout_2 = QHBoxLayout(self.main_window)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contacts_frame = QFrame(self.main_window)
        self.contacts_frame.setObjectName("contacts_frame")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.contacts_frame.sizePolicy().hasHeightForWidth()
        )
        self.contacts_frame.setSizePolicy(sizePolicy)
        self.contacts_frame.setMinimumSize(QSize(0, 0))
        self.contacts_frame.setMaximumSize(QSize(16777215, 16777215))
        self.contacts_frame.setStyleSheet("background-color: brown;")
        self.contacts_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.contacts_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contacts_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_frame = QFrame(self.contacts_frame)
        self.search_frame.setObjectName("search_frame")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.search_frame.sizePolicy().hasHeightForWidth()
        )
        self.search_frame.setSizePolicy(sizePolicy1)
        self.search_frame.setMinimumSize(QSize(0, 50))
        self.search_frame.setStyleSheet("background-color: pink;")
        self.search_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.search_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_search = QLineEdit(self.search_frame)
        self.lineEdit_search.setObjectName("lineEdit_search")

        self.horizontalLayout_4.addWidget(self.lineEdit_search)

        self.verticalLayout_2.addWidget(self.search_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.contacts_list_frame = QFrame(self.contacts_frame)
        self.contacts_list_frame.setObjectName("contacts_list_frame")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.contacts_list_frame.sizePolicy().hasHeightForWidth()
        )
        self.contacts_list_frame.setSizePolicy(sizePolicy2)
        self.contacts_list_frame.setStyleSheet("background-color: lightgreen;")
        self.contacts_list_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.contacts_list_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contacts_list_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_contacts = QListWidget(self.contacts_list_frame)
        self.listWidget_contacts.setObjectName("listWidget_contacts")
        self.listWidget_contacts.setStyleSheet(
            "QListWidget {\n" "	color: #000000;\n" "}"
        )

        self.verticalLayout_3.addWidget(self.listWidget_contacts)

        self.verticalLayout_2.addWidget(self.contacts_list_frame)

        self.horizontalLayout_2.addWidget(
            self.contacts_frame, 0, Qt.AlignmentFlag.AlignLeft
        )

        self.messages_frame = QFrame(self.main_window)
        self.messages_frame.setObjectName("messages_frame")
        sizePolicy1.setHeightForWidth(
            self.messages_frame.sizePolicy().hasHeightForWidth()
        )
        self.messages_frame.setSizePolicy(sizePolicy1)
        self.messages_frame.setMinimumSize(QSize(0, 0))
        self.messages_frame.setMaximumSize(QSize(16777215, 16777215))
        self.messages_frame.setStyleSheet("background-color: cyan;")
        self.messages_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.messages_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.messages_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contact_details_frame = QFrame(self.messages_frame)
        self.contact_details_frame.setObjectName("contact_details_frame")
        self.contact_details_frame.setStyleSheet("background-color: lightyellow;")
        self.contact_details_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.contact_details_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contact_details_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_to = QLabel(self.contact_details_frame)
        self.label_to.setObjectName("label_to")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_to.sizePolicy().hasHeightForWidth())
        self.label_to.setSizePolicy(sizePolicy3)
        self.label_to.setStyleSheet("QLabel {\n" "	color: #000000;\n" "}")

        self.horizontalLayout_5.addWidget(self.label_to)

        self.label_contact = QLabel(self.contact_details_frame)
        self.label_contact.setObjectName("label_contact")
        sizePolicy3.setHeightForWidth(
            self.label_contact.sizePolicy().hasHeightForWidth()
        )
        self.label_contact.setSizePolicy(sizePolicy3)
        self.label_contact.setStyleSheet("QLabel {\n" "	color: #000000;\n" "}")

        self.horizontalLayout_5.addWidget(self.label_contact)

        self.pushButton_details = QPushButton(self.contact_details_frame)
        self.pushButton_details.setObjectName("pushButton_details")
        self.pushButton_details.setStyleSheet(
            "QPushButton {\n" "	color: #000000;\n" "}"
        )

        self.horizontalLayout_5.addWidget(
            self.pushButton_details, 0, Qt.AlignmentFlag.AlignRight
        )

        self.verticalLayout.addWidget(self.contact_details_frame)

        self.listView_messages = QListView(self.messages_frame)
        self.listView_messages.setObjectName("listView_messages")

        self.verticalLayout.addWidget(self.listView_messages)

        self.list_view_messages_frame = QFrame(self.messages_frame)
        self.list_view_messages_frame.setObjectName("list_view_messages_frame")
        self.list_view_messages_frame.setMinimumSize(QSize(0, 50))
        self.list_view_messages_frame.setStyleSheet("background-color: green;")
        self.list_view_messages_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.list_view_messages_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.list_view_messages_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_message = QLineEdit(self.list_view_messages_frame)
        self.lineEdit_message.setObjectName("lineEdit_message")

        self.horizontalLayout_3.addWidget(self.lineEdit_message)

        self.verticalLayout.addWidget(
            self.list_view_messages_frame, 0, Qt.AlignmentFlag.AlignBottom
        )

        self.horizontalLayout_2.addWidget(self.messages_frame)

        self.stackedWidget.addWidget(self.main_window)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Search...", None)
        )
        self.label_to.setText(QCoreApplication.translate("MainWindow", "To:", None))
        self.label_contact.setText(
            QCoreApplication.translate("MainWindow", "Contact Here", None)
        )
        self.pushButton_details.setText(
            QCoreApplication.translate("MainWindow", "Details", None)
        )
        self.lineEdit_message.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "iMessage", None)
        )

    # retranslateUi

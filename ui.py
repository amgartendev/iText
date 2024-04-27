# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designereRuHNP.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.login_window = QWidget()
        self.login_window.setObjectName(u"login_window")
        self.stackedWidget.addWidget(self.login_window)
        self.main_window = QWidget()
        self.main_window.setObjectName(u"main_window")
        self.horizontalLayout_2 = QHBoxLayout(self.main_window)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contacts_frame = QFrame(self.main_window)
        self.contacts_frame.setObjectName(u"contacts_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contacts_frame.sizePolicy().hasHeightForWidth())
        self.contacts_frame.setSizePolicy(sizePolicy)
        self.contacts_frame.setMinimumSize(QSize(0, 0))
        self.contacts_frame.setMaximumSize(QSize(16777215, 16777215))
        self.contacts_frame.setStyleSheet(u"background-color: brown;")
        self.contacts_frame.setFrameShape(QFrame.NoFrame)
        self.contacts_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contacts_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.search_frame = QFrame(self.contacts_frame)
        self.search_frame.setObjectName(u"search_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_frame.sizePolicy().hasHeightForWidth())
        self.search_frame.setSizePolicy(sizePolicy1)
        self.search_frame.setMinimumSize(QSize(0, 50))
        self.search_frame.setStyleSheet(u"background-color: pink;")
        self.search_frame.setFrameShape(QFrame.NoFrame)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_search = QLineEdit(self.search_frame)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout_4.addWidget(self.lineEdit_search)


        self.verticalLayout_2.addWidget(self.search_frame, 0, Qt.AlignTop)

        self.contacts_list_frame = QFrame(self.contacts_frame)
        self.contacts_list_frame.setObjectName(u"contacts_list_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contacts_list_frame.sizePolicy().hasHeightForWidth())
        self.contacts_list_frame.setSizePolicy(sizePolicy2)
        self.contacts_list_frame.setStyleSheet(u"background-color: lightgreen;")
        self.contacts_list_frame.setFrameShape(QFrame.NoFrame)
        self.contacts_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contacts_list_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget_contacts = QListWidget(self.contacts_list_frame)
        QListWidgetItem(self.listWidget_contacts)
        QListWidgetItem(self.listWidget_contacts)
        self.listWidget_contacts.setObjectName(u"listWidget_contacts")

        self.verticalLayout_3.addWidget(self.listWidget_contacts)


        self.verticalLayout_2.addWidget(self.contacts_list_frame)


        self.horizontalLayout_2.addWidget(self.contacts_frame, 0, Qt.AlignLeft)

        self.messages_frame = QFrame(self.main_window)
        self.messages_frame.setObjectName(u"messages_frame")
        sizePolicy1.setHeightForWidth(self.messages_frame.sizePolicy().hasHeightForWidth())
        self.messages_frame.setSizePolicy(sizePolicy1)
        self.messages_frame.setMinimumSize(QSize(0, 0))
        self.messages_frame.setMaximumSize(QSize(16777215, 16777215))
        self.messages_frame.setStyleSheet(u"background-color: cyan;")
        self.messages_frame.setFrameShape(QFrame.NoFrame)
        self.messages_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.messages_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contact_details_frame = QFrame(self.messages_frame)
        self.contact_details_frame.setObjectName(u"contact_details_frame")
        self.contact_details_frame.setStyleSheet(u"background-color: lightyellow;")
        self.contact_details_frame.setFrameShape(QFrame.NoFrame)
        self.contact_details_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contact_details_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_to = QLabel(self.contact_details_frame)
        self.label_to.setObjectName(u"label_to")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_to.sizePolicy().hasHeightForWidth())
        self.label_to.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_to)

        self.label_contact = QLabel(self.contact_details_frame)
        self.label_contact.setObjectName(u"label_contact")
        sizePolicy3.setHeightForWidth(self.label_contact.sizePolicy().hasHeightForWidth())
        self.label_contact.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_contact)

        self.pushButton_details = QPushButton(self.contact_details_frame)
        self.pushButton_details.setObjectName(u"pushButton_details")

        self.horizontalLayout_5.addWidget(self.pushButton_details, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.contact_details_frame)

        self.listView_messages = QListView(self.messages_frame)
        self.listView_messages.setObjectName(u"listView_messages")

        self.verticalLayout.addWidget(self.listView_messages)

        self.list_view_messages_frame = QFrame(self.messages_frame)
        self.list_view_messages_frame.setObjectName(u"list_view_messages_frame")
        self.list_view_messages_frame.setMinimumSize(QSize(0, 50))
        self.list_view_messages_frame.setStyleSheet(u"background-color: green;")
        self.list_view_messages_frame.setFrameShape(QFrame.NoFrame)
        self.list_view_messages_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.list_view_messages_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_message = QLineEdit(self.list_view_messages_frame)
        self.lineEdit_message.setObjectName(u"lineEdit_message")

        self.horizontalLayout_3.addWidget(self.lineEdit_message)


        self.verticalLayout.addWidget(self.list_view_messages_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.messages_frame)

        self.stackedWidget.addWidget(self.main_window)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))

        __sortingEnabled = self.listWidget_contacts.isSortingEnabled()
        self.listWidget_contacts.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_contacts.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Person 1", None));
        ___qlistwidgetitem1 = self.listWidget_contacts.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Person 2", None));
        self.listWidget_contacts.setSortingEnabled(__sortingEnabled)

        self.label_to.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.label_contact.setText(QCoreApplication.translate("MainWindow", u"Contact Here", None))
        self.pushButton_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.lineEdit_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"iMessage", None))
    # retranslateUi


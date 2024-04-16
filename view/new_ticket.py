# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ticket.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 437)
        Dialog.setStyleSheet(u"QWidget {\n"
"    font-family: \"Noto Sans SC\";\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(68, 76, 92, 255), stop:0.5 rgba(52, 61, 70, 235), stop:1 rgba(40, 47, 56, 255));\n"
"}")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.new_ticket = QFrame(Dialog)
        self.new_ticket.setObjectName(u"new_ticket")
        self.new_ticket.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.new_ticket.setFrameShape(QFrame.Shape.NoFrame)
        self.new_ticket.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.new_ticket)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_ticket_label = QLabel(self.new_ticket)
        self.new_ticket_label.setObjectName(u"new_ticket_label")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(20)
        font.setBold(True)
        self.new_ticket_label.setFont(font)
        self.new_ticket_label.setStyleSheet(u"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")
        self.new_ticket_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.new_ticket_label)

        self.ticket_date = QDateEdit(self.new_ticket)
        self.ticket_date.setObjectName(u"ticket_date")
        self.ticket_date.setStyleSheet(u"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;\n"
"	font-size: 16pt;")
        self.ticket_date.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ticket_date.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.ticket_date.setDateTime(QDateTime(QDate(2024, 11, 4), QTime(17, 0, 0)))
        self.ticket_date.setCurrentSectionIndex(0)

        self.verticalLayout.addWidget(self.ticket_date)

        self.ticket_description = QLineEdit(self.new_ticket)
        self.ticket_description.setObjectName(u"ticket_description")
        self.ticket_description.setStyleSheet(u"font-size: 16pt;\n"
"   background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")
        self.ticket_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.ticket_description)

        self.ticket_brand = QLineEdit(self.new_ticket)
        self.ticket_brand.setObjectName(u"ticket_brand")
        self.ticket_brand.setStyleSheet(u"font-size: 16pt;\n"
"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")

        self.verticalLayout.addWidget(self.ticket_brand)

        self.ticket_model = QLineEdit(self.new_ticket)
        self.ticket_model.setObjectName(u"ticket_model")
        self.ticket_model.setStyleSheet(u"font-size: 16pt;\n"
"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")

        self.verticalLayout.addWidget(self.ticket_model)

        self.ticket_employee = QLineEdit(self.new_ticket)
        self.ticket_employee.setObjectName(u"ticket_employee")
        self.ticket_employee.setStyleSheet(u"font-size: 16pt;\n"
"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")

        self.verticalLayout.addWidget(self.ticket_employee)

        self.ticket_status = QComboBox(self.new_ticket)
        self.ticket_status.addItem("")
        self.ticket_status.addItem("")
        self.ticket_status.addItem("")
        self.ticket_status.addItem("")
        self.ticket_status.setObjectName(u"ticket_status")
        self.ticket_status.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"background-color: #78a5a3;\n"
"color: #FFFFFF;\n"
"border: 1px solid #444c5c;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"    color: black;\n"
"}")

        self.verticalLayout.addWidget(self.ticket_status)

        self.save_ticket_button = QPushButton(self.new_ticket)
        self.save_ticket_button.setObjectName(u"save_ticket_button")
        self.save_ticket_button.setMinimumSize(QSize(230, 50))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setBold(True)
        self.save_ticket_button.setFont(font1)
        self.save_ticket_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #555B70;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #555B70;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #363D4A;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_ticket_button.setIcon(icon)
        self.save_ticket_button.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.save_ticket_button)


        self.horizontalLayout.addWidget(self.new_ticket)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.new_ticket_label.setText(QCoreApplication.translate("Dialog", u"New ticket", None))
        self.ticket_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.ticket_brand.setPlaceholderText(QCoreApplication.translate("Dialog", u"Brand", None))
        self.ticket_model.setText("")
        self.ticket_model.setPlaceholderText(QCoreApplication.translate("Dialog", u"Model", None))
        self.ticket_employee.setPlaceholderText(QCoreApplication.translate("Dialog", u"EmployeeId", None))
        self.ticket_status.setItemText(0, QCoreApplication.translate("Dialog", u"Created", None))
        self.ticket_status.setItemText(1, QCoreApplication.translate("Dialog", u"In progress", None))
        self.ticket_status.setItemText(2, QCoreApplication.translate("Dialog", u"Done", None))
        self.ticket_status.setItemText(3, QCoreApplication.translate("Dialog", u"Closed", None))

        self.ticket_status.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose status", None))
        self.save_ticket_button.setText(QCoreApplication.translate("Dialog", u"Save new ticket", None))
    # retranslateUi


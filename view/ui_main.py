# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    font-family: \"Noto Sans SC\";\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(68, 76, 92, 255), stop:0.5 rgba(52, 61, 70, 235), stop:1 rgba(40, 47, 56, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balances_frame = QFrame(self.centralwidget)
        self.balances_frame.setObjectName(u"balances_frame")
        self.balances_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.balances_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.balances_frame)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.label = QLabel(self.balances_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")

        self.verticalLayout_21.addWidget(self.label)

        self.tableView_4 = QTableView(self.balances_frame)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setStyleSheet(u"QTableView {\n"
"    background-color: #444c5c;\n"
"    border: 1px solid #556677;\n"
"    gridline-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-color: #556677;\n"
"    gridline-color: #556677;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #445566;\n"
"    padding: 4px;\n"
"    border: 1px solid #556677;\n"
"    color: #ffffff;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #444c5c;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #556677;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #445566;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #556677;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableView_4.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_4.horizontalHeader().setStretchLastSection(True)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView_4.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_21.addWidget(self.tableView_4)

        self.label_2 = QLabel(self.balances_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"    background-color: #78a5a3;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #444c5c;\n"
"    border-radius: 4px;")

        self.verticalLayout_21.addWidget(self.label_2)

        self.tableView_3 = QTableView(self.balances_frame)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setStyleSheet(u"QTableView {\n"
"    background-color: #444c5c;\n"
"    border: 1px solid #556677;\n"
"    gridline-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-color: #556677;\n"
"    gridline-color: #556677;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #445566;\n"
"    padding: 4px;\n"
"    border: 1px solid #556677;\n"
"    color: #ffffff;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #444c5c;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #556677;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #445566;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #556677;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableView_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableView_3.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_21.addWidget(self.tableView_3)

        self.save_pdf_button = QPushButton(self.balances_frame)
        self.save_pdf_button.setObjectName(u"save_pdf_button")
        self.save_pdf_button.setFont(font1)
        self.save_pdf_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:5px;\n"
"width: 230;\n"
"height: 25;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.verticalLayout_21.addWidget(self.save_pdf_button)


        self.horizontalLayout_2.addWidget(self.balances_frame)

        self.balances_frame_2 = QFrame(self.centralwidget)
        self.balances_frame_2.setObjectName(u"balances_frame_2")
        self.balances_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.balances_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.balances_frame_2)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.tableView_2 = QTableView(self.balances_frame_2)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setAutoFillBackground(False)
        self.tableView_2.setStyleSheet(u"QTableView {\n"
"    background-color: #444c5c;\n"
"    border: 1px solid #556677;\n"
"    gridline-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-color: #556677;\n"
"    gridline-color: #556677;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #445566;\n"
"    padding: 4px;\n"
"    border: 1px solid #556677;\n"
"    color: #ffffff;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #444c5c;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #556677;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #445566;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #556677;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableView_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.verticalLayout_20.addWidget(self.tableView_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.add_employee = QPushButton(self.balances_frame_2)
        self.add_employee.setObjectName(u"add_employee")
        self.add_employee.setFont(font1)
        self.add_employee.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 25;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.add_employee.setFlat(False)

        self.horizontalLayout_4.addWidget(self.add_employee)

        self.delete_employee = QPushButton(self.balances_frame_2)
        self.delete_employee.setObjectName(u"delete_employee")
        self.delete_employee.setFont(font1)
        self.delete_employee.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:5px;\n"
"width: 230;\n"
"height: 25;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_4.addWidget(self.delete_employee)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.balances_frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"    background-color: #444c5c;\n"
"    border: 1px solid #556677;\n"
"    gridline-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-color: #556677;\n"
"    gridline-color: #556677;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #556677;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #445566;\n"
"    padding: 4px;\n"
"    border: 1px solid #556677;\n"
"    color: #ffffff;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #444c5c;\n"
"    width: 10px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #556677;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;"
                        "\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid #445566;\n"
"    background: #556677;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 1px solid #445566;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: #556677;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)


        self.verticalLayout_2.addWidget(self.tableView)

        self.btn_frame = QFrame(self.frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_ticket_button = QPushButton(self.btn_frame)
        self.new_ticket_button.setObjectName(u"new_ticket_button")
        self.new_ticket_button.setMinimumSize(QSize(150, 50))
        self.new_ticket_button.setFont(font1)
        self.new_ticket_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.new_ticket_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.new_ticket_button)

        self.delete_ticket_button = QPushButton(self.btn_frame)
        self.delete_ticket_button.setObjectName(u"delete_ticket_button")
        self.delete_ticket_button.setMinimumSize(QSize(150, 50))
        self.delete_ticket_button.setFont(font1)
        self.delete_ticket_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.delete_ticket_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.delete_ticket_button)

        self.edit_ticket_button = QPushButton(self.btn_frame)
        self.edit_ticket_button.setObjectName(u"edit_ticket_button")
        self.edit_ticket_button.setMinimumSize(QSize(150, 50))
        self.edit_ticket_button.setFont(font1)
        self.edit_ticket_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.edit_ticket_button.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.edit_ticket_button)

        self.detail_ticket_button = QPushButton(self.btn_frame)
        self.detail_ticket_button.setObjectName(u"detail_ticket_button")
        self.detail_ticket_button.setMinimumSize(QSize(150, 50))
        self.detail_ticket_button.setFont(font1)
        self.detail_ticket_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.detail_ticket_button)

        self.parts_ticket_button = QPushButton(self.btn_frame)
        self.parts_ticket_button.setObjectName(u"parts_ticket_button")
        self.parts_ticket_button.setMinimumSize(QSize(150, 50))
        self.parts_ticket_button.setFont(font1)
        self.parts_ticket_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.parts_ticket_button)


        self.verticalLayout_2.addWidget(self.btn_frame)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Parts", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estimates", None))
        self.save_pdf_button.setText(QCoreApplication.translate("MainWindow", u"Save estimates and parts to pdf", None))
        self.add_employee.setText(QCoreApplication.translate("MainWindow", u"Add employee", None))
        self.delete_employee.setText(QCoreApplication.translate("MainWindow", u"Remove employee", None))
        self.new_ticket_button.setText(QCoreApplication.translate("MainWindow", u"New ticket", None))
        self.delete_ticket_button.setText(QCoreApplication.translate("MainWindow", u"Delete ticket", None))
        self.edit_ticket_button.setText(QCoreApplication.translate("MainWindow", u"Edit ticket", None))
        self.detail_ticket_button.setText(QCoreApplication.translate("MainWindow", u"Add estimates", None))
        self.parts_ticket_button.setText(QCoreApplication.translate("MainWindow", u"Add parts", None))
    # retranslateUi


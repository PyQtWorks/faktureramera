# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/faktureramera.ui'
#
# Created: Mon Feb 23 20:51:24 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.customerGroup = QtWidgets.QGroupBox(self.tab)
        self.customerGroup.setMinimumSize(QtCore.QSize(200, 200))
        self.customerGroup.setMaximumSize(QtCore.QSize(16777215, 200))
        self.customerGroup.setObjectName("customerGroup")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.customerGroup)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.customerGroup)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.customerChooser = QtWidgets.QComboBox(self.customerGroup)
        self.customerChooser.setMinimumSize(QtCore.QSize(300, 0))
        self.customerChooser.setObjectName("customerChooser")
        self.verticalLayout_4.addWidget(self.customerChooser)
        self.newCustomerButton = QtWidgets.QPushButton(self.customerGroup)
        self.newCustomerButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.newCustomerButton.setObjectName("newCustomerButton")
        self.verticalLayout_4.addWidget(self.newCustomerButton, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(self.customerGroup)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.referenceField = QtWidgets.QLineEdit(self.groupBox_2)
        self.referenceField.setObjectName("referenceField")
        self.horizontalLayout_5.addWidget(self.referenceField)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.newCustomerLayout = QtWidgets.QVBoxLayout()
        self.newCustomerLayout.setObjectName("newCustomerLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.newCustomerLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.newCustomerLayout)
        self.verticalLayout_2.addWidget(self.customerGroup)
        self.jobsGroup = QtWidgets.QGroupBox(self.tab)
        self.jobsGroup.setObjectName("jobsGroup")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.jobsGroup)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.jobsGroup)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 732, 231))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.jobsLayout = QtWidgets.QVBoxLayout()
        self.jobsLayout.setObjectName("jobsLayout")
        self.verticalLayout_6.addLayout(self.jobsLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.jobsGroup)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 75))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addJobButton = QtWidgets.QPushButton(self.groupBox_3)
        self.addJobButton.setObjectName("addJobButton")
        self.horizontalLayout_2.addWidget(self.addJobButton)
        self.removeJobButton = QtWidgets.QPushButton(self.groupBox_3)
        self.removeJobButton.setObjectName("removeJobButton")
        self.horizontalLayout_2.addWidget(self.removeJobButton)
        self.zeroButton = QtWidgets.QPushButton(self.groupBox_3)
        self.zeroButton.setObjectName("zeroButton")
        self.horizontalLayout_2.addWidget(self.zeroButton)
        spacerItem2 = QtWidgets.QSpacerItem(640, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.saveGenerateButton = QtWidgets.QPushButton(self.groupBox_3)
        self.saveGenerateButton.setObjectName("saveGenerateButton")
        self.horizontalLayout_2.addWidget(self.saveGenerateButton)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maculateButton = QtWidgets.QPushButton(self.groupBox)
        self.maculateButton.setObjectName("maculateButton")
        self.horizontalLayout.addWidget(self.maculateButton)
        self.editBillButton = QtWidgets.QPushButton(self.groupBox)
        self.editBillButton.setObjectName("editBillButton")
        self.horizontalLayout.addWidget(self.editBillButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.generateButton = QtWidgets.QPushButton(self.groupBox)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faktureramera"))
        self.customerGroup.setTitle(_translate("MainWindow", "Kund"))
        self.label.setText(_translate("MainWindow", "Kund:"))
        self.newCustomerButton.setText(_translate("MainWindow", "Ny"))
        self.label_2.setText(_translate("MainWindow", "Referens:"))
        self.jobsGroup.setTitle(_translate("MainWindow", "Jobb"))
        self.addJobButton.setText(_translate("MainWindow", "Nytt jobb"))
        self.removeJobButton.setText(_translate("MainWindow", "Ta bort jobb"))
        self.zeroButton.setText(_translate("MainWindow", "Nollställ"))
        self.saveGenerateButton.setText(_translate("MainWindow", "Generera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Fakturera"))
        self.maculateButton.setText(_translate("MainWindow", "Makulera"))
        self.editBillButton.setText(_translate("MainWindow", "Ändra i faktura"))
        self.generateButton.setText(_translate("MainWindow", "Generera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Historik"))


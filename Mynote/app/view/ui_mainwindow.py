# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Sun Nov 22 21:43:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widgetTop = QtGui.QWidget(self.centralwidget)
        self.widgetTop.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widgetTop.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color:#7D9EC0;\n"
"}"))
        self.widgetTop.setObjectName(_fromUtf8("widgetTop"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetTop)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widgetTop)
        self.label_2.setMaximumSize(QtCore.QSize(782, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton_close = QtGui.QPushButton(self.widgetTop)
        self.pushButton_close.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pushButton_close.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: transparent;\n"
"}"))
        self.pushButton_close.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/close window.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widgetTop)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widgetLeft = QtGui.QWidget(self.splitter)
        self.widgetLeft.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color:#4A708B;\n"
"}"))
        self.widgetLeft.setObjectName(_fromUtf8("widgetLeft"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widgetLeft)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.widgetLeft)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: transparent;\n"
"border-style:outset;\n"
"border-width: 0px;\n"
"padding: 5px 0;\n"
"color: #fff;\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/new one.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.treeView = QtGui.QTreeView(self.widgetLeft)
        self.treeView.setFrameShape(QtGui.QFrame.NoFrame)
        self.treeView.setFrameShadow(QtGui.QFrame.Plain)
        self.treeView.setLineWidth(0)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.verticalLayout.addWidget(self.treeView)
        self.widgetMiddle = QtGui.QWidget(self.splitter)
        self.widgetMiddle.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color: #CCCCCC;\n"
"}\n"
"QLineEdit{\n"
"border-radius: 10px;\n"
"padding: 5px 10px;\n"
"margin: 0 10%;\n"
"background-color: white;\n"
"border: 1px solid #c9c9c9;\n"
"color: #1b1b1e;\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: white;\n"
"border: 1px solid #969696;\n"
"}"))
        self.widgetMiddle.setObjectName(_fromUtf8("widgetMiddle"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetMiddle)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.widgetMiddle)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label = QtGui.QLabel(self.widgetMiddle)
        self.label.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color: #B0B0B0;\n"
"}"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.listView = QtGui.QListView(self.widgetMiddle)
        self.listView.setFrameShape(QtGui.QFrame.NoFrame)
        self.listView.setFrameShadow(QtGui.QFrame.Plain)
        self.listView.setLineWidth(0)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_2.addWidget(self.listView)
        self.widgetRight = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetRight.sizePolicy().hasHeightForWidth())
        self.widgetRight.setSizePolicy(sizePolicy)
        self.widgetRight.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color:#D4D4D4;\n"
"}"))
        self.widgetRight.setObjectName(_fromUtf8("widgetRight"))
        self.verticalLayoutRight = QtGui.QVBoxLayout(self.widgetRight)
        self.verticalLayoutRight.setMargin(0)
        self.verticalLayoutRight.setObjectName(_fromUtf8("verticalLayoutRight"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widgetRight)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.plainTextEdit.setLineWidth(0)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayoutRight.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mynote", None))
        self.label_2.setText(_translate("MainWindow", "Mynote", None))
        self.pushButton.setText(_translate("MainWindow", "New Note", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))

import icon_rc

from PyQt4 import QtCore, QtGui
from view.ui_mainwindow import Ui_MainWindow 

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # initialize ui
        self.initUI()
        
        # no frame window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def initUI(self):
        self.ui.lineEdit.textEdited[str].connect(self.updateLabelText)
        self.ui.pushButton.clicked.connect(self.buttonClick)
        
        #resize window when no frame window
        self.ui.verticalLayoutRight.addWidget(QtGui.QSizeGrip(self), 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

    def buttonClick(self):
        QtGui.QMessageBox.about(self, 'title', 'content')

    def updateLabelText(self, text):
        self.ui.label.setText(text)
        
    #add for window movable
    def mousePressEvent(self, event):
        """ override mouse press event """
        self._postion = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        """ override mouse move event """
        self.move(event.globalPos() - self._postion)

    def closeEvent(self, event):
        """ override close event """
        event.accept()
    #add for window movable

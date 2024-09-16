# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_file import Ui_Form

class para(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setObjectName("self")
        self.resize(800, 589)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(self)
        self.actionImport.setObjectName("actionImport")
        self.actionParameters = QtWidgets.QAction(self)
        self.actionParameters.setObjectName("actionParameters")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImport)
        self.menuSettings.addAction(self.actionParameters)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.ui = Ui_Form()
        self.ui.setupUi()
        self.horizontalLayout.addLayout(self.ui.horizontalLayout_5)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        
        self.menuFile.setTitle(_translate("self", "File"))
        self.menuSettings.setTitle(_translate("self", "Settings"))
        self.actionSave.setText(_translate("self", "Export"))
        self.actionImport.setText(_translate("self", "Import"))
        self.actionParameters.setText(_translate("self", "Parameters"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = Ui_self()
#     ui.setupUi()
#     ui.show()
#     sys.exit(app.exec_())


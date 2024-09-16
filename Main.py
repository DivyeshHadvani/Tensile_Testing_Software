import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Welcome_page import Ui_Form
from Login_Page_Main import Login_page_main_class


class UI(QtWidgets.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        
        # Load the ui file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.Admin_PB.clicked.connect(self.open_Admin_Login_window_1_1)
        self.ui.Manager_PB.clicked.connect(self.open_Manager_Login_window_1_2)
        self.ui.Operator_PB.clicked.connect(self.open_Operator_Login_window_1_3)
        
    def open_Admin_Login_window_1_1(self):
        UIWindow.hide()
        # self.window_1_1 = QtWidgets.QWidget()
        # self.ui_1_1 = Ui_Admin_Login_Page()
        # self.ui_1_1.setupUi(self.window_1_1)
        # self.window_1_1.show()
                 
        self.window_1_1 = QtWidgets.QWidget()
        self.ui_4 = Login_page_main_class("open_Admin_Login_window_1_1")
        
    def open_Manager_Login_window_1_2(self):
        UIWindow.hide()
        # self.window_1_2 = QtWidgets.QWidget()
        # self.ui_1_2 = Ui_Manager_Login_Page()
        # self.ui_1_2.setupUi(self.window_1_2)
        # self.window_1_2.show()
        
        self.window_1_1 = QtWidgets.QWidget()
        self.ui_4 = Login_page_main_class("open_Manager_Login_window_1_2")
    
    
    def open_Operator_Login_window_1_3(self):
        UIWindow.hide() 
        # self.window_1_3 = QtWidgets.QWidget()
        # self.ui_1_3 = Ui_Operator_Login_Page()
        # self.ui_1_3.setupUi(self.window_1_3)
        # self.window_1_3.show()
        
        self.window_1_1 = QtWidgets.QWidget()
        self.ui_4 = Login_page_main_class("open_Operator_Login_window_1_3")
    
    def closeEvent(self, event):
        print("i am in main 51 closeevent")
    

if __name__ == "__main__":
    print("hei i am here")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec_())
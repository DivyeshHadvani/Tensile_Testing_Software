from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QAction

import pickle

# from Admin_Login_Page import Ui_Admin_Login_Page
from Login_Page import Ui_Login_Page
from Manager_home_page_main import Manager_home_page_main
from Trackability_main import Trackability_page_main

class Login_page_main_class(QtWidgets.QWidget):
    
    def __init__(self,page=None):
        super(Login_page_main_class, self).__init__()
        
        # print(page)
        self.login_page_window = QtWidgets.QWidget()
        self.ui = Ui_Login_Page()
        self.ui.setupUi(self.login_page_window)
        # self.ui.closeEvent = self.on_close
        
        self.ui.error_message_Label.setText("")
        
        if page == "open_Admin_Login_window_1_1":
                self.ui.username_Label.setText("Admin Username")
        
        if page == "open_Manager_Login_window_1_2":
                self.ui.username_Label.setText("Manager Username")
                
        if page == "open_Operator_Login_window_1_3":
                self.ui.username_Label.setText("Operator Username")
                
        self.login_page_window.show()
        
        # self.ui.Login_PB.clicked.connect(self.open_new_window)
        self.ui.Login_PB.clicked.connect(lambda: self.open_new_window_login_page_main(page))
        self.ui.Forgot_Password_PB.clicked.connect(self.open_new_window)
        
    def open_new_window(self):
        print("i have forgot password....")

    def open_new_window_login_page_main(self,page):
        # self.login_page_window.hide()    
        
        if page == "open_Admin_Login_window_1_1":
                # self.login_page_window.hide() 
                # self.track_window = QtWidgets.QWidget()
                # self.track_ui = Ui_Trackability_Page()
                # self.track_ui.setupUi(self.track_window)
                # self.track_window.show()
                pass
        
        if page == "open_Manager_Login_window_1_2":
            
            try:    
                with open("Manager_userprofiledatabase.pickle", 'rb') as f:
                    data1 = pickle.load(f)
                    
                user_id = [inner_tuple[0] for inner_tuple in data1]
                password_id = [inner_tuple[3] for inner_tuple in data1]
                                    
                print("self.ui.username_LineEdit",self.ui.username_LineEdit.text())
                print("self.ui.password_LineEdit",self.ui.password_LineEdit.text())
                print("Manager user_name",user_id)
                print("Manager password_", password_id)
                
                if self.ui.username_LineEdit.text() == "":
                    self.ui.error_message_Label.setText("Please enter User Name...")
                    
                else:    
                    if self.ui.username_LineEdit.text() in user_id and self.ui.password_LineEdit.text() in password_id:
                        self.login_page_window.hide() 
                        self.manager_home_window_main = QtWidgets.QMainWindow()
                        self.manager_home_ui = Manager_home_page_main()
                    else:
                        self.ui.error_message_Label.setText("Incorrect username or password... Please try again...")
                    
            except:
                pass
    
        if page == "open_Operator_Login_window_1_3":

            try:
                with open("operator_userprofiledatabase.pickle", 'rb') as f:
                    data1 = pickle.load(f)
                    
                print(data1)
                user_id = [inner_tuple[0] for inner_tuple in data1]
                password_id = [inner_tuple[3] for inner_tuple in data1]
                                    
                print("self.ui.username_LineEdit",self.ui.username_LineEdit.text())
                print("self.ui.password_LineEdit",self.ui.password_LineEdit.text())
                print("operator user_name",user_id)
                print("operator password_", password_id)
                
                if self.ui.username_LineEdit.text() == "":
                    self.ui.error_message_Label.setText("Please enter User Name...")
                    
                else:    
                    if self.ui.username_LineEdit.text() in user_id and self.ui.password_LineEdit.text() in password_id:
                        self.login_page_window.hide() 
                        self.trackability_window_main = QtWidgets.QMainWindow()
                        self.trackability_main_ui = Trackability_page_main(self.ui.username_LineEdit.text())
                    else:
                        self.ui.error_message_Label.setText("Incorrect username or password... Please try again...")
                        
            except:
                pass
        
if __name__ == "__main__":
    print("i am 28 in Login_page_main page")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Login_page_main_class()
    # UIWindow.show()

    sys.exit(app.exec_())
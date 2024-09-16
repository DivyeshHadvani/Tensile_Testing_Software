from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QAction

import re
import pickle


from User_profile_create_page import Ui_User_profile_create_page
# from Manager_home_page_main import Manager_home_page_main

class User_profile_create_page_main(QtWidgets.QWidget):
    def __init__(self,parent=None):
        print("parent",type(parent))
        print(parent)
        # super().__init__(parent)
        super(User_profile_create_page_main, self).__init__(parent)
        
        self.user_profile_create_page_window = QtWidgets.QWidget()
        self.ui = Ui_User_profile_create_page()
        self.ui.setupUi(self.user_profile_create_page_window)
        self.user_profile_create_page_window.show()
        
        self.ui.first_name_Label.setText("")
        self.ui.Last_name_Label.setText("")
        self.ui.username_Label.setText("")
        self.ui.password_Label.setText("")
        self.ui.confirm_password_Label.setText("")
        self.ui.error_message_Label.setText("")
        
        # # set clear button for QLineEdit
        # self.first_name_LineEdit.setClearButtonEnabled(True)
        # self.Last_name_LineEdit.setClearButtonEnabled(True)
        # self.username_LineEdit.setClearButtonEnabled(True)
        # self.password_LineEdit.setClearButtonEnabled(True)
        # self.confirm_password_LineEdit.setClearButtonEnabled(True)
        
        # change default icon of clear button
        # icon = QIcon("")
        # self.first_name_LineEdit.findChildren(QAction)[0].setIcon(icon)
        
        # Set placeholder text for QLineEdit
        self.ui.first_name_LineEdit.setPlaceholderText("First Name")
        self.ui.Last_name_LineEdit.setPlaceholderText("Last Name")
        self.ui.username_LineEdit.setPlaceholderText("Username")
        self.ui.password_LineEdit.setPlaceholderText("Password")
        self.ui.confirm_password_LineEdit.setPlaceholderText("Confirm Password")
        
                
        # show label when QLineEdit text changed
        self.ui.first_name_LineEdit.textChanged.connect(self.do_first_name_label)
        self.ui.Last_name_LineEdit.textChanged.connect(self.do_last_name_label)
        self.ui.username_LineEdit.textChanged.connect(self.do_username_label)
        self.ui.password_LineEdit.textChanged.connect(self.do_password_Label)
        self.ui.confirm_password_LineEdit.textChanged.connect(self.do_confirm_password_Label)
        
        self.ui.login_PB.clicked.connect(self.check_before_create_profile)
        self.ui.close_PB.clicked.connect(self.isEnabledtrue)
        # self.ui.close_PB.clicked.connect(lambda: self.isEnabledtrue(parent))
    
    def do_first_name_label(self, text):
        if text:
            self.ui.first_name_Label.setText("First Name")
        else:
            self.ui.first_name_Label.setText("")
    
    def do_last_name_label(self, text):
        if text:
            self.ui.Last_name_Label.setText("Last Name")
        else:
            self.ui.Last_name_Label.setText("")
            
    def do_username_label(self, text):
        if text:
            self.ui.username_Label.setText("Username")
        else:
            self.ui.username_Label.setText("")

    def do_password_Label(self, text):
        if text:
            self.ui.password_Label.setText("Password")
        else:
            self.ui.password_Label.setText("")

    def do_confirm_password_Label(self, text):
        if text:
            self.ui.confirm_password_Label.setText("Confirm Password")
        else:
            self.ui.confirm_password_Label.setText("")
            
    def check_before_create_profile(self):   
        self.ui.error_message_Label.setText("")
        try:
            if len(self.ui.username_LineEdit.text()) < 6:
                print("Username must be at least 6 characters long.")   
                self.ui.error_message_Label.setText("Username must be at least 6 characters long.")  
            else:
                if len(self.ui.password_LineEdit.text()) < 6:
                    print("Password must be at least 6 characters long.")   
                    self.ui.error_message_Label.setText("Password must be at least 6 characters long.") 
                else:
                    if not re.search("[A-Z]", self.ui.password_LineEdit.text()):
                        print("Password must contain at least one capital letter.")
                        self.ui.error_message_Label.setText("Password must contain at least one capital letter.")
                    else:
                        if not re.search("[0-9]", self.ui.password_LineEdit.text()):
                            print("Password must contain at least one numeric digit.")
                            self.ui.error_message_Label.setText("Password must contain at least one numeric digit.")
                        else:
                            special_chars = re.findall(r'[!@#$%^&*()+_-]', self.ui.password_LineEdit.text())
                        
                            if len(special_chars) == 0:
                                print("Password must contain at least one special character.") 
                                self.ui.error_message_Label.setText("Password must contain at least one special character.")
                            else:    
                                if self.ui.password_LineEdit.text() != self.ui.confirm_password_LineEdit.text():
                                    print("Passwords do not match. Please try again.")
                                    self.ui.error_message_Label.setText("Passwords do not match. Please try again.")
                                else:   
                                    self.ui.error_message_Label.setStyleSheet("color: rgb(29, 173, 34);")
                                    self.ui.error_message_Label.setText("Account registered successfully!")  
                                    
                                    # data = ((self.ui.first_name_LineEdit.text()),
                                    #         (self.ui.Last_name_LineEdit.text()),
                                    #         (self.ui.username_LineEdit.text()),
                                    #         (self.ui.password_LineEdit.text()),
                                    #         (self.ui.confirm_password_LineEdit.text()),)
                                    
                                    filename = str(self.ui.username_LineEdit.text())
                                    
                                    # self.write_to_pickle(filename)
                                    self.write_to_pickle("operator_userprofiledatabase")
                                    
                                    # read_data = self.read_from_pickle(filename)
                                    read_data = self.read_from_pickle("operator_userprofiledatabase.pickle")
                                    print(read_data)
                                    # for i in read_data:
                                    #     print(i)

                                    print("Account registered successfully!")
                                    
            
        except Exception as e:
            print("An unexpected error occurred:", e)
            

    # Function to write data to pickle file
    def write_to_pickle(self,filename):
        SAVENAME = filename + ".pickle"
        
        try:
            with open(SAVENAME, 'rb') as f:
                data = pickle.load(f)
            
                data1 = ((self.ui.username_LineEdit.text()),
                        (self.ui.first_name_LineEdit.text()),
                        (self.ui.Last_name_LineEdit.text()),
                        (self.ui.password_LineEdit.text()),
                        (self.ui.confirm_password_LineEdit.text()),)
                
                # Combine the existing tuple new_tuple with the new tuple t
                output_tuple = data + (data1,)
                
            with open(SAVENAME, 'wb') as f:
                pickle.dump(output_tuple, f)
                    
        except:
            data = ((self.ui.username_LineEdit.text()),
                    (self.ui.first_name_LineEdit.text()),
                    (self.ui.Last_name_LineEdit.text()),
                    (self.ui.password_LineEdit.text()),
                    (self.ui.confirm_password_LineEdit.text()),)
            
            output_tuple = (data,)
            
            with open(SAVENAME, 'wb') as f:
                pickle.dump(output_tuple, f)
        
        
    # Function to read data from pickle file
    def read_from_pickle(self,filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data
    
    def isEnabledtrue(self):
        self.user_profile_create_page_window.hide()

        try:
            self.parent().enable_main_window()
        except Exception as e:
            print("i am in except at 196", e)           
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = User_profile_create_page_main()
    # UIWindow.show()
    sys.exit(app.exec_())
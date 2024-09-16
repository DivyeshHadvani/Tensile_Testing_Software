from PyQt5 import QtCore, QtGui, QtWidgets

import re
import pickle


from Recipe_create_page import Ui_Recipe_create_page



class Recipe_create_page_main(QtWidgets.QWidget):
    def __init__(self,parent=None):
        print("parent",type(parent))
        print(parent)
        # super().__init__(parent)
        super(Recipe_create_page_main, self).__init__(parent)
        
        self.recipe_create_page_window = QtWidgets.QWidget()
        self.ui = Ui_Recipe_create_page()
        self.ui.setupUi(self.recipe_create_page_window)
        self.recipe_create_page_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)              #       remove the title bar
        
        self.recipe_create_page_window.show()
        
        
        
        self.ui.error_message_Label.setText("")
        
        # Set up QLineEdit to accept only integers
        self.int_validator = QtGui.QIntValidator()
        self.ui.speed_lineEdit.setValidator(self.int_validator)
        self.ui.distance_lineEdit.setValidator(self.int_validator)
        
        # Make ComboBox Clickable
        self.ui.motion_direction_comboBox.activated.connect(self.clicker)
              
        # # Add items to combobox
        # Add placeholder item
        self.ui.motion_direction_comboBox.addItem("Select an option")
        self.ui.motion_direction_comboBox.addItem("Forward")
        self.ui.motion_direction_comboBox.addItem("Reverse")
        # # Add a list
        # my_toppings = ["Select an option", "Forward", "Reverse"]
        # self.ui.motion_direction_comboBox.addItems(my_toppings)
        
        # Set the placeholder as the current index
        self.ui.motion_direction_comboBox.setCurrentIndex(0)
        
        # Connect to showPopup to remove the placeholder
        self.ui.motion_direction_comboBox.showPopup = self.remove_placeholder_and_show
        
        self.ui.close_PB.clicked.connect(self.isEnabledtrue)
        self.ui.save_PB.clicked.connect(self.check_before_create_recipe)
        
    def remove_placeholder_and_show(self):
        if self.ui.motion_direction_comboBox.currentText() == "Select an option":
            self.ui.motion_direction_comboBox.removeItem(0)
        QtWidgets.QComboBox.showPopup(self.ui.motion_direction_comboBox)
        
    def clicker(self):
        self.ui.error_message_Label.setText(f'You Picked: {self.ui.motion_direction_comboBox.currentText()}')
        
    def check_before_create_recipe(self): 
        self.ui.error_message_Label.setText("")   
        try:
            if len(self.ui.recipe_name_lineEdit.text()) < 6:
                print("Recipe Name must be at least 6 characters long.")  
                self.ui.error_message_Label.setText("Recipe Name must be at least 6 characters long.") 
            else:
                print(self.ui.motion_direction_comboBox.currentText())
                if not self.ui.motion_direction_comboBox.currentText() in ["Forward", "Reverse"]:
                    print("Please select motion direction.")
                    self.ui.error_message_Label.setText("Please select motion direction.")
                else:
                    if len(self.ui.speed_lineEdit.text()) < 1:
                        print("Please fill speed data.")
                        self.ui.error_message_Label.setText("Please fill speed data.")
                    else:
                        if len(self.ui.distance_lineEdit.text()) < 1:
                            print("Please fill distance data.")
                            self.ui.error_message_Label.setText("Please fill distance data.")
                        else:
                            
                            # self.write_to_pickle(filename)
                            self.write_to_pickle("recipe_database")
                            
                            # read_data = self.read_from_pickle(filename)
                            read_data = self.read_from_pickle("recipe_database.pickle")
                            print(read_data)
                            # for i in read_data:
                            #     print(i)
                            self.ui.error_message_Label.setStyleSheet("color: rgb(29, 173, 34);")
                            self.ui.error_message_Label.setText("Recipe registered successfully!") 
                            
        except Exception as e:
            print("An unexpected error occurred:", e)
                            
                        
    # Function to write data to pickle file
    def write_to_pickle(self,filename):
        SAVENAME = filename + ".pickle"  
        
        try:
            with open(SAVENAME, 'rb') as f:
                data = pickle.load(f)  
            
            data1 = ((self.ui.recipe_name_lineEdit.text()),
                    (self.ui.motion_direction_comboBox.currentText()),
                    (self.ui.speed_lineEdit.text()),
                    (self.ui.distance_lineEdit.text()),)  
            
            # Combine the existing tuple new_tuple with the new tuple t
            output_tuple = data + (data1,)
            
            with open(SAVENAME, 'wb') as f:
                pickle.dump(output_tuple, f)
        
        except:
            data = ((self.ui.recipe_name_lineEdit.text()),
                    (self.ui.motion_direction_comboBox.currentText()),
                    (self.ui.speed_lineEdit.text()),
                    (self.ui.distance_lineEdit.text()),)  
            
            output_tuple = (data,)
            
            with open(SAVENAME, 'wb') as f:
                pickle.dump(output_tuple, f)
                
    # Function to read data from pickle file
    def read_from_pickle(self,filename):
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data
                
                
    def isEnabledtrue(self):
        self.recipe_create_page_window.hide()

        try:
            self.parent().enable_main_window()
        except Exception as e:
            print("i am in except", e)
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Recipe_create_page_main()
    # UIWindow.show()
    sys.exit(app.exec_())
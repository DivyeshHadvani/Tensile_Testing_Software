from PyQt5 import QtCore, QtGui, QtWidgets

import re
import pickle

# from Trackability import Ui_Trackability_Page
from Trackability_Mainwindow import Ui_MainWindow



class Trackability_page_main(QtWidgets.QWidget):
    def __init__(self,username=None,parent=None):
        print("username",type(username))
        print(username)
        print("parent",type(parent))
        print(parent)
        # super().__init__(parent)
        super(Trackability_page_main, self).__init__(parent)
        
        # self.Trackability_window = QtWidgets.QWidget()
        # self.ui = Ui_Trackability_Page()
        # self.ui.setupUi(self.Trackability_window)
        # self.Trackability_window.show()
        
        self.Trackability_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Trackability_window)
               
        self.Trackability_window.show()
        
        read_data_operator = self.read_from_pickle("operator_userprofiledatabase.pickle")
        try:
            operator_name = self.find_operator_name(username,read_data_operator)
            self.ui.operator_name_value_Label.setText(operator_name)
        except Exception as e:
            print("i am in except", e)
        
        # # Add a list
        # my_recipes = ["Select an option"]
        # self.ui.select_recipe_comboBox.addItems(my_recipes)
        
        # Add items to combobox
        self.ui.select_recipe_comboBox.addItem("Select an option")
        # Set the placeholder as the current index
        self.ui.select_recipe_comboBox.setCurrentIndex(0)
        # Connect to showPopup to remove the placeholder
        self.ui.select_recipe_comboBox.showPopup = self.remove_placeholder_and_show
        
        try:
            # Reading data from pickle file
            read_data = self.read_from_pickle("recipe_database.pickle")
            print("read_data",type(read_data))
            print(read_data)
            for item in read_data:
                print("item",item)
                
            # Finding the length of the tuple
            length_of_tuple = len(read_data)
            
            # Extracting and printing the first element of each sub-tuple
            for i in range(length_of_tuple):
                name = read_data[i][0]
                # my_recipes.append(name)
                # print(my_recipes)
                # Add items to combobox
                self.ui.select_recipe_comboBox.addItem(name)
                
                print(f"{i} = \"{name}\"")
                
        except Exception as e:
            print("i am in except", e)
        
        # Make ComboBox Clickable
        # self.ui.select_recipe_comboBox.activated.connect(self.clicker)
        self.ui.select_recipe_comboBox.activated.connect(lambda: self.clicker(read_data))
        
    def find_operator_name(self,username, data):
        for item in data:
            if item[0] == username:
                return item[1]
        return None  # Return None if the code is not found
        
    def remove_placeholder_and_show(self):
        if self.ui.select_recipe_comboBox.currentText() == "Select an option":
            self.ui.select_recipe_comboBox.removeItem(0)
        QtWidgets.QComboBox.showPopup(self.ui.select_recipe_comboBox)
        
    # Function to read data from pickle file
    def read_from_pickle(self,filename):
        with open(filename, 'rb') as f:
            data1 = pickle.load(f)
        return data1
        
    def clicker(self,read_data):
       print(f'You Picked: {self.ui.select_recipe_comboBox.currentText()}')
       current_index_recipe = self.ui.select_recipe_comboBox.currentIndex()
       
       print(read_data[current_index_recipe][1])
       print(read_data[current_index_recipe][2])
       print(read_data[current_index_recipe][3])
       
       self.ui.motion_direction_value_Label.setText(read_data[current_index_recipe][1])
       self.ui.speed_value_Label.setText(read_data[current_index_recipe][2])
       self.ui.distance_value_Label.setText(read_data[current_index_recipe][3])
       
    #    read_data_operator = self.read_from_pickle("operator_userprofiledatabase.pickle")
    #    self.ui.operator_name_value_Label.setText(read_data_operator[current_index_recipe][0])
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Trackability_page_main()
    # UIWindow.show()
    sys.exit(app.exec_())
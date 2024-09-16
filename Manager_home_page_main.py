from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtWidgets import QMessageBox

import pickle

from Manager_home_page import Ui_manager_home_page
from User_profile_create_page_main import User_profile_create_page_main
from Recipe_create_page_main import Recipe_create_page_main

class Manager_home_page_main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Manager_home_page_main, self).__init__()
        
        self.manager_home_window = QtWidgets.QMainWindow()
        self.ui = Ui_manager_home_page()
        self.ui.setupUi(self.manager_home_window)
        self.manager_home_window.show()
        
        self.ui.users_profile_tableWidget.setHorizontalHeaderLabels(["User Name", "First Name", "Last Name", "Action"])  # Set header labels
        # Adjust table properties
        self.ui.users_profile_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.users_profile_tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.ui.search_input_lineEdit.textChanged.connect(self.search_table_profile)
        
        self.ui.recipe_tableWidget.setHorizontalHeaderLabels(["Recipe Name", "Motion Direction", "Speed", "Distance", "Action"])  # Set header labels
        # Adjust table properties
        self.ui.recipe_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ui.recipe_tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.ui.search_input_recipe_lineEdit.textChanged.connect(self.search_table_recipe)
        
        self.update_populate_data()
                    
        self.ui.create_user_profile_PB.clicked.connect(self.open_new_create_user_profile_window)
        self.ui.create_operation_method_PB.clicked.connect(self.open_new_create_operation_method_window)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        
    def update_populate_data(self):
        try:
            # Reading data from pickle file
            read_data = self.read_from_pickle("operator_userprofiledatabase.pickle")
            # print("read_data",type(read_data),read_data)
            # print("Data read from pickle file:")
            for item in read_data:
                print("item",item)
                
            self.populate_users_profile_table(read_data)
        except Exception as e:
            print("i am in except", e)
        
        try:
            # Reading data from pickle file
            read_data = self.read_from_pickle("recipe_database.pickle")
            for item in read_data:
                print("item",item)
                
            self.populate_recipe_table(read_data)
        except Exception as e:
            print("i am in except", e)
        
    def populate_users_profile_table(self, data):
        print("len",len(data))
        self.ui.users_profile_tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                if col < 3:
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)                 
                    # print("col",col)
                    self.ui.users_profile_tableWidget.setItem(row, col, item)
        
                # # Enable editing only for the "Action" column
                # if col == 1:
                #     print("i am in if",col)
                #     # item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)  # Enable editing for the "Action" column
                # else:
                #     item.setFlags(QtCore.Qt.ItemIsEnabled)  # Disable editing for other columns
                #     print("i am in else",col)
                                 
        # Add push buttons to Action column
        for row in range(self.ui.users_profile_tableWidget.rowCount()):
            # button = QtWidgets.QPushButton(f"Action"+str(row+1), self.tableWidget)
            button = QtWidgets.QPushButton(f"Action {row+1}", self.ui.users_profile_tableWidget)
            button.setObjectName(f"action_button_{row+1}")
            # print(button.objectName)                                              #output is   <built-in method objectName of QPushButton object at 0x0000026472A54430>
            print("button object name",button.objectName())                                              #output is  Action1
            # button.clicked.connect(self.on_action_button_clicked)
            # button.clicked.connect(lambda: self.on_action_button_clicked(button.objectName()))
            button.clicked.connect(lambda checked, r=row+1: self.on_action_button_clicked(r))
            self.ui.users_profile_tableWidget.setCellWidget(row, 3, button)
            
    def populate_recipe_table(self, data):
        print("len",len(data))
        self.ui.recipe_tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                if col < 4:
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)                 
                    # print("col",col)
                    self.ui.recipe_tableWidget.setItem(row, col, item)
                                 
        # Add push buttons to Action column
        for row in range(self.ui.recipe_tableWidget.rowCount()):
            # button = QtWidgets.QPushButton(f"Action"+str(row+1), self.tableWidget)
            button = QtWidgets.QPushButton(f"Action {row+1}", self.ui.recipe_tableWidget)
            button.setObjectName(f"action_button_{row+1}")
            # print(button.objectName)                                              #output is   <built-in method objectName of QPushButton object at 0x0000026472A54430>
            print("button object name",button.objectName())                                              #output is  Action1
            button.clicked.connect(lambda checked, r=row+1: self.on_action_button_clicked(r))
            self.ui.recipe_tableWidget.setCellWidget(row, 4, button)
            
    # Function to read data from pickle file
    def read_from_pickle(self,filename):
        with open(filename, 'rb') as f:
            data1 = pickle.load(f)
        return data1

    def tab_changed(self, index):
        print("index page",index)
        
        if index == self.ui.tabWidget.indexOf(self.ui.permissions_tab):
            QMessageBox.information(None, "Welcome", "Welcome to the table view!")
                    
    def on_action_button_clicked(self,objectname):
        print("Button clicked in row:", objectname)
        print("i am in pushbutton", str(objectname))
    
    def search_table_profile(self, text):
        # If the search input is empty, show all rows and return
        if not text:
            for row in range(self.ui.users_profile_tableWidget.rowCount()):
                self.ui.users_profile_tableWidget.setRowHidden(row, False)
            return

        # Get the number of rows and columns in the table
        rows = self.ui.users_profile_tableWidget.rowCount()
        cols = self.ui.users_profile_tableWidget.columnCount()

        # Iterate through each cell in the table
        for row in range(rows):
            row_hidden = True  # Flag to indicate if the row should be hidden
            for col in range(cols):
                item = self.ui.users_profile_tableWidget.item(row, col)
                if item and text.lower() in item.text().lower():  # Check if the text is in the cell
                    row_hidden = False  # If text found, row should not be hidden
                    break
            self.ui.users_profile_tableWidget.setRowHidden(row, row_hidden)  # Hide or show the row based on the flag
            
    def search_table_recipe(self, text):
        # If the search input is empty, show all rows and return
        if not text:
            for row in range(self.ui.recipe_tableWidget.rowCount()):
                self.ui.recipe_tableWidget.setRowHidden(row, False)
            return

        # Get the number of rows and columns in the table
        rows = self.ui.recipe_tableWidget.rowCount()
        cols = self.ui.recipe_tableWidget.columnCount()

        # Iterate through each cell in the table
        for row in range(rows):
            row_hidden = True  # Flag to indicate if the row should be hidden
            for col in range(cols):
                item = self.ui.recipe_tableWidget.item(row, col)
                if item and text.lower() in item.text().lower():  # Check if the text is in the cell
                    row_hidden = False  # If text found, row should not be hidden
                    break
            self.ui.recipe_tableWidget.setRowHidden(row, row_hidden)  # Hide or show the row based on the flag
        
    def open_new_create_user_profile_window(self):
        # self.manager_home_window.hide() 
        self.manager_home_window.setEnabled(False) 
        # self.setEnabled(False)  # Disable main window while dialog is open  
        self.user_profile_create_page_window = QtWidgets.QWidget()
        self.ui_user_profile_create_page_window = User_profile_create_page_main(self)
        
    def open_new_create_operation_method_window(self):
        # self.manager_home_window.hide() 
        self.manager_home_window.setEnabled(False) 
        # self.setEnabled(False)  # Disable main window while dialog is open  
        self.create_operation_method_window = QtWidgets.QWidget()
        self.ui_create_operation_method_window = Recipe_create_page_main(self)
        
    def enable_main_window(self):
        self.update_populate_data()
        self.manager_home_window.setEnabled(True)
        
            
if __name__ == "__main__":
    print("i am in manager home page")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UIWindow = Manager_home_page_main()
    # UIWindow.show()
    sys.exit(app.exec_())
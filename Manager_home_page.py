# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manager_home_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manager_home_page(object):
    def setupUi(self, manager_home_page):
        manager_home_page.setObjectName("manager_home_page")
        manager_home_page.setEnabled(True)
        manager_home_page.resize(1203, 891)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        manager_home_page.setFont(font)
        self.centralwidget = QtWidgets.QWidget(manager_home_page)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1171, 821))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.create_user_profile_PB = QtWidgets.QPushButton(self.home_tab)
        self.create_user_profile_PB.setGeometry(QtCore.QRect(110, 30, 241, 131))
        self.create_user_profile_PB.setObjectName("create_user_profile_PB")
        self.create_operation_method_PB = QtWidgets.QPushButton(self.home_tab)
        self.create_operation_method_PB.setGeometry(QtCore.QRect(430, 30, 241, 131))
        self.create_operation_method_PB.setObjectName("create_operation_method_PB")
        self.tabWidget.addTab(self.home_tab, "")
        self.user_tab = QtWidgets.QWidget()
        self.user_tab.setObjectName("user_tab")
        self.users_profile_tableWidget = QtWidgets.QTableWidget(self.user_tab)
        self.users_profile_tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 561))
        self.users_profile_tableWidget.setRowCount(10)
        self.users_profile_tableWidget.setColumnCount(4)
        self.users_profile_tableWidget.setObjectName("users_profile_tableWidget")
        self.layoutWidget = QtWidgets.QWidget(self.user_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 600, 541, 36))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_label = QtWidgets.QLabel(self.layoutWidget)
        self.search_label.setMinimumSize(QtCore.QSize(100, 0))
        self.search_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_label.setObjectName("search_label")
        self.horizontalLayout.addWidget(self.search_label)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.search_input_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_input_lineEdit.setSizePolicy(sizePolicy)
        self.search_input_lineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.search_input_lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.search_input_lineEdit.setObjectName("search_input_lineEdit")
        self.horizontalLayout.addWidget(self.search_input_lineEdit)
        self.tabWidget.addTab(self.user_tab, "")
        self.permissions_tab = QtWidgets.QWidget()
        self.permissions_tab.setObjectName("permissions_tab")
        self.tabWidget.addTab(self.permissions_tab, "")
        self.operations_method_tab = QtWidgets.QWidget()
        self.operations_method_tab.setObjectName("operations_method_tab")
        self.recipe_tableWidget = QtWidgets.QTableWidget(self.operations_method_tab)
        self.recipe_tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 561))
        self.recipe_tableWidget.setRowCount(10)
        self.recipe_tableWidget.setColumnCount(5)
        self.recipe_tableWidget.setObjectName("recipe_tableWidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.operations_method_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 600, 541, 36))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_recipe_label = QtWidgets.QLabel(self.layoutWidget_2)
        self.search_recipe_label.setMinimumSize(QtCore.QSize(100, 0))
        self.search_recipe_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_recipe_label.setObjectName("search_recipe_label")
        self.horizontalLayout_2.addWidget(self.search_recipe_label)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.search_input_recipe_lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input_recipe_lineEdit.sizePolicy().hasHeightForWidth())
        self.search_input_recipe_lineEdit.setSizePolicy(sizePolicy)
        self.search_input_recipe_lineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.search_input_recipe_lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.search_input_recipe_lineEdit.setObjectName("search_input_recipe_lineEdit")
        self.horizontalLayout_2.addWidget(self.search_input_recipe_lineEdit)
        self.tabWidget.addTab(self.operations_method_tab, "")
        manager_home_page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(manager_home_page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1203, 26))
        self.menubar.setObjectName("menubar")
        manager_home_page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(manager_home_page)
        self.statusbar.setObjectName("statusbar")
        manager_home_page.setStatusBar(self.statusbar)

        self.retranslateUi(manager_home_page)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(manager_home_page)

    def retranslateUi(self, manager_home_page):
        _translate = QtCore.QCoreApplication.translate
        manager_home_page.setWindowTitle(_translate("manager_home_page", "Manager Window"))
        self.create_user_profile_PB.setText(_translate("manager_home_page", "Create \n"
"User Profile"))
        self.create_operation_method_PB.setText(_translate("manager_home_page", "Create New \n"
"Operation \n"
"Method"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("manager_home_page", "Home"))
        self.search_label.setText(_translate("manager_home_page", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_tab), _translate("manager_home_page", "Users/Groups"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.permissions_tab), _translate("manager_home_page", "Permissions"))
        self.search_recipe_label.setText(_translate("manager_home_page", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.operations_method_tab), _translate("manager_home_page", "Operation\'s Method"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager_home_page = QtWidgets.QMainWindow()
    ui = Ui_manager_home_page()
    ui.setupUi(manager_home_page)
    manager_home_page.show()
    sys.exit(app.exec_())

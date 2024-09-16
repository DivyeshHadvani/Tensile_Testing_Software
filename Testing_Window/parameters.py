# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameters.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import serial.tools.list_ports

from plotter import plotter_and_data

class para(QtWidgets.QDialog):
    change_set_unit_value = QtCore.pyqtSignal(int)
    def __init__(self):
        QtCore.QThread.__init__(self)
        # super().__init__()

        self.setObjectName("Dialog")
        self.resize(400, 550)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(400, 550))
        self.setMaximumSize(QtCore.QSize(400, 550))

        # print("main_D",type(sizePolicy))
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 300, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.com_distal_label = QtWidgets.QLabel(self.groupBox_2)
        self.com_distal_label.setGeometry(QtCore.QRect(1, 21, 46, 16))
        self.com_distal_label.setObjectName("com_distal_label")
        self.distal_com = QtWidgets.QComboBox(self.groupBox_2)
        self.distal_com.setGeometry(QtCore.QRect(150, 20, 100, 20))
        self.distal_com.setObjectName("distal_com")
        self.distal_com.addItem("")
        self.distal_com.addItem("")
        self.distal_baude_label = QtWidgets.QLabel(self.groupBox_2)
        self.distal_baude_label.setGeometry(QtCore.QRect(1, 47, 70, 16))
        self.distal_baude_label.setObjectName("distal_baude_label")
        self.distal_baude = QtWidgets.QLineEdit(self.groupBox_2)
        self.distal_baude.setGeometry(QtCore.QRect(150, 50, 133, 20))
        self.distal_baude.setObjectName("distal_baude")


        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 100, 300, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.proximal_com_label = QtWidgets.QLabel(self.groupBox_3)
        self.proximal_com_label.setGeometry(QtCore.QRect(1, 21, 70, 16))
        self.proximal_com_label.setObjectName("proximal_com_label")
        self.proximal_com = QtWidgets.QComboBox(self.groupBox_3)
        self.proximal_com.setGeometry(QtCore.QRect(150, 20, 100, 20))
        self.proximal_com.setObjectName("proximal_com")
        self.proximal_com.addItem("")
        self.proximal_com.addItem("")
        self.proximal_baude_label = QtWidgets.QLabel(self.groupBox_3)
        self.proximal_baude_label.setGeometry(QtCore.QRect(1, 47, 70, 16))
        self.proximal_baude_label.setObjectName("proximal_baude_label")
        self.proximal_baude = QtWidgets.QLineEdit(self.groupBox_3)
        self.proximal_baude.setGeometry(QtCore.QRect(150, 50, 133, 20))
        self.proximal_baude.setObjectName("proximal_baude")


        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 188, 101, 16))
        self.label_7.setObjectName("label_7")
        self.roller_dia = QtWidgets.QLineEdit(self)
        self.roller_dia.setGeometry(QtCore.QRect(170, 188, 133, 20))
        self.roller_dia.setObjectName("roller_dia")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(20, 214, 140, 16))
        self.label_8.setObjectName("label_8")
        self.roller_steps = QtWidgets.QLineEdit(self)
        self.roller_steps.setGeometry(QtCore.QRect(170, 214, 133, 20))
        self.roller_steps.setText("")
        self.roller_steps.setObjectName("roller_steps")

        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 100, 16))
        self.label_10.setObjectName("label_10")
        self.axis_pitch = QtWidgets.QLineEdit(self)
        self.axis_pitch.setGeometry(QtCore.QRect(170, 240, 133, 20))
        self.axis_pitch.setObjectName("axis_pitch")

        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(20, 266, 131, 16))
        self.label_9.setObjectName("label_9")
        self.axis_steps = QtWidgets.QLineEdit(self)
        self.axis_steps.setGeometry(QtCore.QRect(170, 266, 133, 20))
        self.axis_steps.setText("")
        self.axis_steps.setObjectName("axis_steps")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(20, 300, 100, 16))
        self.label_11.setObjectName("label_11")
        self.Unit_comboBox = QtWidgets.QComboBox(self)                                  #   self.Unit_comboBox = QtWidgets.QComboBox(Dialog)
        self.Unit_comboBox.setGeometry(QtCore.QRect(170, 300, 100, 20))
        # self.Unit_comboBox.setEditable(False)
        # self.Unit_comboBox.setMaxVisibleItems(10)
        self.Unit_comboBox.setObjectName("Unit_comboBox")
        # self.Unit_comboBox.addItem("")
        # self.Unit_comboBox.addItem("")

        
        # List of items to add to the combo box
        self.unit_combobox_list = ["F vs mm", "kgf vs mm"]
        
        # Add items to the combo box
        self.Unit_comboBox.addItems(self.unit_combobox_list)
        
        self.groupBox_5 = QtWidgets.QGroupBox(self)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 340, 300, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.Arduino_com_label = QtWidgets.QLabel(self.groupBox_5)
        self.Arduino_com_label.setGeometry(QtCore.QRect(1, 21, 70, 16))
        self.Arduino_com_label.setObjectName("Arduino_com_label")
        self.Arduino_com = QtWidgets.QComboBox(self.groupBox_5)
        self.Arduino_com.setGeometry(QtCore.QRect(150, 20, 100, 20))
        self.Arduino_com.setObjectName("Arduino_com")
        self.Arduino_com.addItem("")
        self.Arduino_com.addItem("")
        self.Arduino_baude_label = QtWidgets.QLabel(self.groupBox_5)
        self.Arduino_baude_label.setGeometry(QtCore.QRect(1, 47, 70, 16))
        self.Arduino_baude_label.setObjectName("Arduino_baude_label")
        self.Arduino_baude = QtWidgets.QLineEdit(self.groupBox_5)
        self.Arduino_baude.setGeometry(QtCore.QRect(150, 50, 133, 20))
        self.Arduino_baude.setObjectName("Arduino_baude")


        self.save_parameters = QtWidgets.QPushButton(self)
        # self.save_parameters = QtWidgets.QPushButton(self, clicked = lambda: self.save_all_para(sizePolicy))
        self.save_parameters.setGeometry(QtCore.QRect(190, 450, 75, 23))
        self.save_parameters.setObjectName("save_parameters")
        # self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.save_parameters.clicked.connect(self.save_all_para)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(70, 500, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # self.retranslateUi(Dialog)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)
        # self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept) # type: ignore
        self.buttonBox.rejected.connect(self.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)


        self.retranslateUi()
        # self.Unit_comboBox.setCurrentIndex(0)
        # QtCore.QMetaObject.connectSlotsByName(self)
        
    def save_all_para(self,window):
        print("saving")
        self.all_parameters = {
        "distal_port":self.distal_com.currentText(),
        "distal_baude":self.distal_baude.text(),
        "proximal_port":self.proximal_com.currentText(),
        "proximal_baude":self.proximal_baude.text(),
        "roller_dia":self.roller_dia.text(),
        "roller_steps":self.roller_steps.text(),
        "axis_pitch":self.axis_pitch.text(),
        "axis_steps":self.axis_steps.text(),
        "Unit_selection":self.Unit_comboBox.currentText(),
        "Arduino_port":self.Arduino_com.currentText(),
        "Arduino_baude":self.Arduino_baude.text(),
        }
        # with open("parameters.pkl",'wb') as para_file:
        with open("setting_parameters.pickle",'wb') as para_file:
            pickle.dump(self.all_parameters, para_file, pickle.HIGHEST_PROTOCOL)

        # self.plotter_para.to_check_unit()
        # self.plotter_para = plotter_and_data(self.ui_para)           # plotter_and_data(self.ui_para)             # both are same

        try:
            # self.proximal_gauge_mark10 = mark10_f_values()
            #  self.proximal_gauge_mark10.update_set_unit()
            # print("self.proximal_gauge_mark10.change_unit",self.proximal_gauge_mark10.change_unit)
            # self.proximal_gauge_mark10.change_unit = True
            self.temp_S1_val_temp = 24
            print("self.temp_S1_val_temp",self.temp_S1_val_temp)
            # self.prox_unit.proximal_Unit_Update_clicked()
            # self.prox_unit.proximal_zero_clicked()
            # self.pro.proximal_zero_clicked()
            # self.prox_unit.connect_proximal()
            self.change_set_unit_value.emit(self.temp_S1_val_temp)


            # self.proximal_gauge_mark10.update_set_unit()


    #         connect_com()
    #         pass
        except:
            print("na thayu ne yes in parameters 221")
            pass

    # def connect_com(self):
    #     pass
    def to_check_unit(self):
        # print("i am in to check now")
        self.load_para_plotter()
        
    def load_para_plotter(self):
        try:
            # print("Load para_plotter")
            with open("setting_parameters.pickle", 'rb') as para_file:
                self.all_parameters = pickle.load(para_file)
            # print(self.all_parameters)
            # print(self.all_parameters['Unit_selection'])
            self.Unit_show = self.all_parameters['Unit_selection']
            # print("Unit_show", self.Unit_show)

        except:
            pass
    
    def load_para(self):
        try:
            with open("setting_parameters.pickle",'rb') as para_file:
                self.all_parameters = pickle.load(para_file)
            # print(self.all_parameters)
            # print(type(self.all_parameters))

            keysList = list(self.all_parameters.keys())
            ValueList = list(self.all_parameters.values())
            # print(keysList)
            # print(ValueList)
            
            # print("self.proximal_baude_01",self.proximal_baude)
            self.proximal_baude.setText(str(self.all_parameters['proximal_baude']))
            # print("self.proximal_baude_02",self.proximal_baude)
            self.distal_baude.setText(str(self.all_parameters['distal_baude']))
            self.Arduino_baude.setText(str(self.all_parameters['Arduino_baude']))
            self.roller_dia.setText(self.all_parameters['roller_dia'])
            self.roller_steps.setText(self.all_parameters['roller_steps'])
            self.axis_pitch.setText(self.all_parameters['axis_pitch'])
            self.axis_steps.setText(self.all_parameters['axis_steps'])
            
            if self.all_parameters['Unit_selection'] in self.unit_combobox_list:
                self.Unit_comboBox.setCurrentIndex(self.unit_combobox_list.index(self.all_parameters['Unit_selection']))
            
            self.buttonBox.accepted.connect(self.accept) # type: ignore

        except:
            pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Parameters"))

        self.groupBox_3.setTitle(_translate("self", "Proximal force sensor"))
        self.proximal_com_label.setText(_translate("self", "COM port"))
        self.proximal_com.setItemText(0, _translate("self", "COM0"))                       #   ("self", "COM11")
        # self.proximal_com.setItemText(1, _translate("self", "COM1"))                        #   ("self", "COM1")
        self.proximal_baude_label.setText(_translate("self", "Baud rate"))

        self.label_7.setText(_translate("self", "Roller dia (mm)"))
        self.label_8.setText(_translate("self", "Roller motor steps/rev"))
        self.label_9.setText(_translate("self", "Axis motor steps/rev"))
        self.label_10.setText(_translate("self", "Axis pitch (mm)"))
        self.label_11.setText(_translate("self", "Unit Selection"))

        self.groupBox_2.setTitle(_translate("self", "Distal force sensor"))
        self.com_distal_label.setText(_translate("self", "COM port"))
        self.distal_com.setItemText(0, _translate("self", "COM0"))
        # self.distal_com.setItemText(1, _translate("self", "COM1"))
        self.distal_baude_label.setText(_translate("self", "Baud rate"))

        self.groupBox_5.setTitle(_translate("self", "Arduino Controller"))
        self.Arduino_com_label.setText(_translate("self", "COM port"))
        self.Arduino_com.setItemText(0, _translate("self", "COM0"))                       #   ("self", "COM11")
        # self.Arduino_com.setItemText(1, _translate("self", "COM1"))                        #   ("self", "COM1")
        self.Arduino_baude_label.setText(_translate("self", "Baud rate"))


        self.save_parameters.setText(_translate("self", "Save"))

        # self.Unit_comboBox.setCurrentText(_translate("self", "F vs mm"))
        # self.Unit_comboBox.setItemText(0, _translate("self", "F vs mm"))
        # self.Unit_comboBox.setItemText(1, _translate("self", "kgf vs mm"))

    def find_devices(self):
        self.proximal_com.clear()
        self.distal_com.clear()
        self.Arduino_com.clear()
        connected = []
        Unit_list = ["F vs mm","kgf vs mm"]
        comlist = serial.tools.list_ports.comports()
        for element in comlist:
            connected.append(element.device)
            self.proximal_com.addItem(element.device)
            self.distal_com.addItem(element.device)
            self.Arduino_com.addItem(element.device)
        try:
            self.proximal_com.setCurrentIndex(connected.index(self.all_parameters['proximal_port']))
        except:
            pass
        try:
            self.distal_com.setCurrentIndex(connected.index(self.all_parameters['distal_port']))
        except:
            pass
        try:
            self.Arduino_com.setCurrentIndex(connected.index(self.all_parameters['Arduino_port']))
        except:
            pass
        try:
            self.Unit_comboBox.setCurrentIndex(Unit_list.index(self.all_parameters['Unit_selection']))
        except:
            print("i am fail")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = para()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

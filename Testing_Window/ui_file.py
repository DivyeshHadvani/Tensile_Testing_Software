# -*- coding: utf-8 -*-

#  implementation generated from reading ui file 'D:\trackability\1.0\itr3\main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import new_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self):
        # .setObjectName("")
        # .resize(1301, 938)
        # .setStyleSheet("")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(500, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.smt_logo = QtWidgets.QLabel()
        self.smt_logo.setMaximumSize(QtCore.QSize(400, 400))
        self.smt_logo.setStyleSheet("image: url(:/logo/images/aa.png);")
        self.smt_logo.setText("")
        self.smt_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.smt_logo.setObjectName("smt_logo")
        self.verticalLayout.addWidget(self.smt_logo)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.record_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.record_label.setFont(font)
        self.record_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.record_label.setObjectName("record_label")
        self.gridLayout_3.addWidget(self.record_label, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 5, 2, 1, 1)
        self.speed_of_motor = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.speed_of_motor.sizePolicy().hasHeightForWidth())
        self.speed_of_motor.setSizePolicy(sizePolicy)
        self.speed_of_motor.setMinimumSize(QtCore.QSize(400, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speed_of_motor.setFont(font)
        self.speed_of_motor.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.speed_of_motor.setObjectName("speed_of_motor")
        self.gridLayout_3.addWidget(self.speed_of_motor, 3, 1, 1, 2)
        self.distance_to_be_covered = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distance_to_be_covered.sizePolicy().hasHeightForWidth())
        self.distance_to_be_covered.setSizePolicy(sizePolicy)
        self.distance_to_be_covered.setMinimumSize(QtCore.QSize(400, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_to_be_covered.setFont(font)
        self.distance_to_be_covered.setObjectName("distance_to_be_covered")
        self.gridLayout_3.addWidget(self.distance_to_be_covered, 4, 1, 1, 2)
        
        self.is_roller = QtWidgets.QRadioButton()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.is_roller.setFont(font)
        self.is_roller.setObjectName("is_roller")
        self.gridLayout_3.addWidget(self.is_roller, 0, 1, 1, 1)
        
        self.speed_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speed_label.setFont(font)
        self.speed_label.setObjectName("speed_label")
        self.gridLayout_3.addWidget(self.speed_label, 3, 0, 1, 1)
        self.distance_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.distance_label.setFont(font)
        self.distance_label.setObjectName("distance_label")
        self.gridLayout_3.addWidget(self.distance_label, 4, 0, 1, 1)
        self.select_motor_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_motor_label.setFont(font)
        self.select_motor_label.setObjectName("select_motor_label")
        self.gridLayout_3.addWidget(self.select_motor_label, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 8, 0, 1, 3)
        self.directory_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.directory_label.sizePolicy().hasHeightForWidth())
        self.directory_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.directory_label.setFont(font)
        self.directory_label.setObjectName("directory_label")
        self.gridLayout_3.addWidget(self.directory_label, 6, 0, 1, 1)
        self.browse_directory = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.browse_directory.sizePolicy().hasHeightForWidth())
        self.browse_directory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browse_directory.setFont(font)
        self.browse_directory.setObjectName("browse_directory")
        self.gridLayout_3.addWidget(self.browse_directory, 6, 2, 1, 1)
        self.test_name = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.test_name.sizePolicy().hasHeightForWidth())
        self.test_name.setSizePolicy(sizePolicy)
        self.test_name.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test_name.setFont(font)
        self.test_name.setObjectName("test_name")
        self.gridLayout_3.addWidget(self.test_name, 7, 1, 1, 1)
        self.save_directory = QtWidgets.QLineEdit()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.save_directory.sizePolicy().hasHeightForWidth())
        self.save_directory.setSizePolicy(sizePolicy)
        self.save_directory.setMinimumSize(QtCore.QSize(300, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_directory.setFont(font)
        self.save_directory.setObjectName("save_directory")
        self.gridLayout_3.addWidget(self.save_directory, 6, 1, 1, 1)
        self.test_name_label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.test_name_label.setFont(font)
        self.test_name_label.setObjectName("test_name_label")
        self.gridLayout_3.addWidget(self.test_name_label, 7, 0, 1, 1)
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Arduino_Start_Stop = QtWidgets.QPushButton()
        # self.Arduino_Start_Stop.setText("Arduino_Start")
        # self.Arduino_Start_Stop.setObjectName("Arduino_Start_Stop")
        # self.horizontalLayout_6.addWidget(self.Arduino_Start_Stop)
        
        self.Arduino_Start_Stop = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Arduino_Start_Stop.sizePolicy().hasHeightForWidth())
        self.Arduino_Start_Stop.setSizePolicy(sizePolicy)
        self.Arduino_Start_Stop.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Arduino_Start_Stop.setFont(font)
        self.Arduino_Start_Stop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Arduino_Start_Stop.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Arduino_Start_Stop.setObjectName("Arduino_Start_Stop")
        self.horizontalLayout_6.addWidget(
            self.Arduino_Start_Stop, 0, QtCore.Qt.AlignHCenter)
               
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 9, 0, 1, 3)

        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # self.move_axis_left_end = QtWidgets.QPushButton()
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.move_axis_left_end.sizePolicy().hasHeightForWidth())
        # self.move_axis_left_end.setSizePolicy(sizePolicy)
        # self.move_axis_left_end.setMinimumSize(QtCore.QSize(90, 70))
        # self.move_axis_left_end.setStyleSheet("#move_axis_left_end {\n"
        #                                       "background-color: transparent;\n"
        #                                       "background: none;\n"
        #                                       "    border-image: url(:/logo/images/two_left_.png);\n"
        #                                       "border: none;\n"
        #                                       "background-repeat: none;\n"
        #                                       "}\n"
        #                                       "#move_axis_left_end:pressed\n"
        #                                       "{\n"
        #                                       "\n"
        #                                       "border-image: url(:/logo/images/two_left_after_.png);}")
        # self.move_axis_left_end.setText("")
        # self.move_axis_left_end.setObjectName("move_axis_left_end")
        # self.horizontalLayout_6.addWidget(self.move_axis_left_end)
        # self.move_axis_left_one = QtWidgets.QPushButton()
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(60)
        # sizePolicy.setVerticalStretch(60)
        # sizePolicy.setHeightForWidth(
        #     self.move_axis_left_one.sizePolicy().hasHeightForWidth())
        # self.move_axis_left_one.setSizePolicy(sizePolicy)
        # self.move_axis_left_one.setMinimumSize(QtCore.QSize(70, 70))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.move_axis_left_one.setFont(font)
        # self.move_axis_left_one.setStyleSheet("#move_axis_left_one {\n"
        #                                       "background-color: transparent;\n"
        #                                       "    border-image: url(:/logo/images/one_left_.png);\n"
        #                                       "background: none;\n"
        #                                       "border: none;\n"
        #                                       "background-repeat: none;\n"
        #                                       "}\n"
        #                                       "#move_axis_left_one:pressed\n"
        #                                       "{\n"
        #                                       "border-image: url(:/logo/images/one_left_after_.png);\n"
        #                                       "}")
        # self.move_axis_left_one.setText("")
        # self.move_axis_left_one.setObjectName("move_axis_left_one")
        # self.horizontalLayout_6.addWidget(self.move_axis_left_one)
        # self.move_axis = QtWidgets.QLabel()
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.move_axis.setFont(font)
        # self.move_axis.setAlignment(QtCore.Qt.AlignCenter)
        # self.move_axis.setObjectName("move_axis")
        # self.horizontalLayout_6.addWidget(self.move_axis)
        # self.move_axis_right_one = QtWidgets.QPushButton()
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.move_axis_right_one.sizePolicy().hasHeightForWidth())
        # self.move_axis_right_one.setSizePolicy(sizePolicy)
        # self.move_axis_right_one.setMinimumSize(QtCore.QSize(70, 70))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.move_axis_right_one.setFont(font)
        # self.move_axis_right_one.setStyleSheet("#move_axis_right_one {\n"
        #                                        "background-color: transparent;\n"
        #                                        "background: none;\n"
        #                                        "border-image: url(:/logo/images/one_right_.png);\n"
        #                                        "border: none;\n"
        #                                        "background-repeat: none;\n"
        #                                        "}\n"
        #                                        "#move_axis_right_one:pressed\n"
        #                                        "{\n"
        #                                        "border-image: url(:/logo/images/one_right_after_.png);\n"
        #                                        "}")
        # self.move_axis_right_one.setText("")
        # self.move_axis_right_one.setAutoDefault(False)
        # self.move_axis_right_one.setObjectName("move_axis_right_one")
        # self.horizontalLayout_6.addWidget(self.move_axis_right_one)
        # self.move_axis_right_end = QtWidgets.QPushButton()
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(
        #     self.move_axis_right_end.sizePolicy().hasHeightForWidth())
        # self.move_axis_right_end.setSizePolicy(sizePolicy)
        # self.move_axis_right_end.setMinimumSize(QtCore.QSize(90, 70))
        # self.move_axis_right_end.setStyleSheet("#move_axis_right_end {\n"
        #                                        "background-color: transparent;\n"
        #                                        "background: none;\n"
        #                                        "    border-image: url(:/logo/images/two_right_.png);\n"
        #                                        "border: none;\n"
        #                                        "background-repeat: none;\n"
        #                                        "}\n"
        #                                        "#move_axis_right_end:pressed\n"
        #                                        "{\n"
        #                                        "\n"
        #                                        "border-image: url(:/logo/images/two_right_after_.png);}")
        # self.move_axis_right_end.setText("")
        # self.move_axis_right_end.setObjectName("move_axis_right_end")
        # self.horizontalLayout_6.addWidget(self.move_axis_right_end)
        # spacerItem2 = QtWidgets.QSpacerItem(
        #     40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_6.addItem(spacerItem2)
        
        
        # self.gridLayout_3.addLayout(self.horizontalLayout_6, 9, 0, 1, 3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.record_proximal_force_gauge = QtWidgets.QCheckBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.record_proximal_force_gauge.setFont(font)
        self.record_proximal_force_gauge.setObjectName(
            "record_proximal_force_gauge")
        self.verticalLayout_4.addWidget(self.record_proximal_force_gauge)
        self.record_distal_force_gauge = QtWidgets.QCheckBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.record_distal_force_gauge.setFont(font)
        self.record_distal_force_gauge.setObjectName(
            "record_distal_force_gauge")
        self.verticalLayout_4.addWidget(self.record_distal_force_gauge)
        self.record_video = QtWidgets.QCheckBox()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.record_video.setFont(font)
        self.record_video.setObjectName("record_video")
        self.verticalLayout_4.addWidget(self.record_video)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 5, 1, 1, 1)
        
        # self.is_axis = QtWidgets.QRadioButton()
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.is_axis.setFont(font)
        # self.is_axis.setObjectName("is_axis")
        # self.gridLayout_3.addWidget(self.is_axis, 1, 1, 1, 1)
        
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.graphing_layout = QtWidgets.QVBoxLayout()
        self.graphing_layout.setObjectName("graphing_layout")
        self.horizontalLayout_5.addLayout(self.graphing_layout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.proximal_force_gauge_groupbox = QtWidgets.QGroupBox()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_force_gauge_groupbox.sizePolicy().hasHeightForWidth())
        self.proximal_force_gauge_groupbox.setSizePolicy(sizePolicy)
        self.proximal_force_gauge_groupbox.setMinimumSize(
            QtCore.QSize(320, 200))
        self.proximal_force_gauge_groupbox.setStyleSheet(
            "QGroupBox { border: 1px solid black;}")
        self.proximal_force_gauge_groupbox.setObjectName(
            "proximal_force_gauge_groupbox")
        self.layoutWidget_6 = QtWidgets.QWidget(
            self.proximal_force_gauge_groupbox)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 20, 421, 164))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.connect_proximal_force_gauge = QtWidgets.QPushButton(
            self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connect_proximal_force_gauge.sizePolicy().hasHeightForWidth())
        self.connect_proximal_force_gauge.setSizePolicy(sizePolicy)
        self.connect_proximal_force_gauge.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connect_proximal_force_gauge.setFont(font)
        self.connect_proximal_force_gauge.setStyleSheet(
            "background-color: rgb(255, 170, 0);")
        self.connect_proximal_force_gauge.setObjectName(
            "connect_proximal_force_gauge")
        self.verticalLayout_5.addWidget(self.connect_proximal_force_gauge)
        self.set_proximal_zero = QtWidgets.QPushButton(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_proximal_zero.sizePolicy().hasHeightForWidth())
        self.set_proximal_zero.setSizePolicy(sizePolicy)
        self.set_proximal_zero.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_proximal_zero.setFont(font)
        self.set_proximal_zero.setObjectName("set_proximal_zero")
        self.verticalLayout_5.addWidget(self.set_proximal_zero)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.proximal_force_value_label = QtWidgets.QLabel(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_force_value_label.sizePolicy().hasHeightForWidth())
        self.proximal_force_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_force_value_label.setFont(font)
        self.proximal_force_value_label.setObjectName(
            "proximal_force_value_label")
        self.horizontalLayout_2.addWidget(
            self.proximal_force_value_label, 0, QtCore.Qt.AlignLeft)
        self.proximal_force_value = QtWidgets.QLabel(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_force_value.sizePolicy().hasHeightForWidth())
        self.proximal_force_value.setSizePolicy(sizePolicy)
        self.proximal_force_value.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_force_value.setFont(font)
        self.proximal_force_value.setObjectName("proximal_force_value")
        self.horizontalLayout_2.addWidget(self.proximal_force_value)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.proximal_maximum_force_label = QtWidgets.QLabel(
            self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_maximum_force_label.sizePolicy().hasHeightForWidth())
        self.proximal_maximum_force_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_maximum_force_label.setFont(font)
        self.proximal_maximum_force_label.setObjectName(
            "proximal_maximum_force_label")
        self.horizontalLayout_11.addWidget(self.proximal_maximum_force_label)
        self.proximal_maximum_force = QtWidgets.QLabel(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_maximum_force.sizePolicy().hasHeightForWidth())
        self.proximal_maximum_force.setSizePolicy(sizePolicy)
        self.proximal_maximum_force.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_maximum_force.setFont(font)
        self.proximal_maximum_force.setObjectName("proximal_maximum_force")
        self.horizontalLayout_11.addWidget(self.proximal_maximum_force)
        self.proximal_maximum_force_position_label = QtWidgets.QLabel(
            self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_maximum_force_position_label.sizePolicy().hasHeightForWidth())
        self.proximal_maximum_force_position_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_maximum_force_position_label.setFont(font)
        self.proximal_maximum_force_position_label.setObjectName(
            "proximal_maximum_force_position_label")
        self.horizontalLayout_11.addWidget(
            self.proximal_maximum_force_position_label)
        self.proximal_maximum_force_position_value = QtWidgets.QLabel(
            self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_maximum_force_position_value.sizePolicy().hasHeightForWidth())
        self.proximal_maximum_force_position_value.setSizePolicy(sizePolicy)
        self.proximal_maximum_force_position_value.setMinimumSize(
            QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_maximum_force_position_value.setFont(font)
        self.proximal_maximum_force_position_value.setObjectName(
            "proximal_maximum_force_position_value")
        self.horizontalLayout_11.addWidget(
            self.proximal_maximum_force_position_value)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.proximal_average_force = QtWidgets.QLabel(self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proximal_average_force.sizePolicy().hasHeightForWidth())
        self.proximal_average_force.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.proximal_average_force.setFont(font)
        self.proximal_average_force.setObjectName("proximal_average_force")
        self.verticalLayout_5.addWidget(self.proximal_average_force)
        self.layoutWidget_6.raise_()
        self.verticalLayout_6.addWidget(self.proximal_force_gauge_groupbox)
        self.distal_force_gauge_groupbox = QtWidgets.QGroupBox()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_force_gauge_groupbox.sizePolicy().hasHeightForWidth())
        self.distal_force_gauge_groupbox.setSizePolicy(sizePolicy)
        self.distal_force_gauge_groupbox.setMinimumSize(QtCore.QSize(320, 200))
        self.distal_force_gauge_groupbox.setStyleSheet(
            "QGroupBox { border: 1px solid black;}")
        self.distal_force_gauge_groupbox.setObjectName(
            "distal_force_gauge_groupbox")
        self.layoutWidget_7 = QtWidgets.QWidget(
            self.distal_force_gauge_groupbox)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 10, 349, 162))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.connect_distal_force_gauge = QtWidgets.QPushButton(
            self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connect_distal_force_gauge.sizePolicy().hasHeightForWidth())
        self.connect_distal_force_gauge.setSizePolicy(sizePolicy)
        self.connect_distal_force_gauge.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connect_distal_force_gauge.setFont(font)
        self.connect_distal_force_gauge.setStyleSheet(
            "background-color: rgb(255, 170, 0);")
        self.connect_distal_force_gauge.setObjectName(
            "connect_distal_force_gauge")
        self.verticalLayout_8.addWidget(self.connect_distal_force_gauge)
        self.set_distal_zero = QtWidgets.QPushButton(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.set_distal_zero.sizePolicy().hasHeightForWidth())
        self.set_distal_zero.setSizePolicy(sizePolicy)
        self.set_distal_zero.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_distal_zero.setFont(font)
        self.set_distal_zero.setObjectName("set_distal_zero")
        self.verticalLayout_8.addWidget(self.set_distal_zero)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.distal_force_value_label = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_force_value_label.sizePolicy().hasHeightForWidth())
        self.distal_force_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_force_value_label.setFont(font)
        self.distal_force_value_label.setObjectName("distal_force_value_label")
        self.horizontalLayout_7.addWidget(
            self.distal_force_value_label, 0, QtCore.Qt.AlignLeft)
        self.distal_force_value = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_force_value.sizePolicy().hasHeightForWidth())
        self.distal_force_value.setSizePolicy(sizePolicy)
        self.distal_force_value.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_force_value.setFont(font)
        self.distal_force_value.setObjectName("distal_force_value")
        self.horizontalLayout_7.addWidget(self.distal_force_value)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.distal_maximum_force_label = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_maximum_force_label.sizePolicy().hasHeightForWidth())
        self.distal_maximum_force_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_maximum_force_label.setFont(font)
        self.distal_maximum_force_label.setObjectName(
            "distal_maximum_force_label")
        self.horizontalLayout_10.addWidget(self.distal_maximum_force_label)
        self.distal_maximum_force = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_maximum_force.sizePolicy().hasHeightForWidth())
        self.distal_maximum_force.setSizePolicy(sizePolicy)
        self.distal_maximum_force.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_maximum_force.setFont(font)
        self.distal_maximum_force.setObjectName("distal_maximum_force")
        self.horizontalLayout_10.addWidget(self.distal_maximum_force)
        self.distal_maximum_force_position_label = QtWidgets.QLabel(
            self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_maximum_force_position_label.sizePolicy().hasHeightForWidth())
        self.distal_maximum_force_position_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_maximum_force_position_label.setFont(font)
        self.distal_maximum_force_position_label.setObjectName(
            "distal_maximum_force_position_label")
        self.horizontalLayout_10.addWidget(
            self.distal_maximum_force_position_label)
        self.distal_maximum_force_position_value = QtWidgets.QLabel(
            self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_maximum_force_position_value.sizePolicy().hasHeightForWidth())
        self.distal_maximum_force_position_value.setSizePolicy(sizePolicy)
        self.distal_maximum_force_position_value.setMinimumSize(
            QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_maximum_force_position_value.setFont(font)
        self.distal_maximum_force_position_value.setObjectName(
            "distal_maximum_force_position_value")
        self.horizontalLayout_10.addWidget(
            self.distal_maximum_force_position_value)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.distal_average_force = QtWidgets.QLabel(self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.distal_average_force.sizePolicy().hasHeightForWidth())
        self.distal_average_force.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.distal_average_force.setFont(font)
        self.distal_average_force.setObjectName("distal_average_force")
        self.verticalLayout_8.addWidget(self.distal_average_force)
        self.verticalLayout_6.addWidget(self.distal_force_gauge_groupbox)
        self.connect_camera = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connect_camera.sizePolicy().hasHeightForWidth())
        self.connect_camera.setSizePolicy(sizePolicy)
        self.connect_camera.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.connect_camera.setFont(font)
        self.connect_camera.setStyleSheet(
            "background-color: rgb(255, 170, 0);")
        self.connect_camera.setObjectName("connect_camera")
        self.verticalLayout_6.addWidget(
            self.connect_camera, 0, QtCore.Qt.AlignHCenter)
        self.start_test = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(
            self.start_test.sizePolicy().hasHeightForWidth())
        self.start_test.setSizePolicy(sizePolicy)
        self.start_test.setMinimumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.start_test.setFont(font)
        self.start_test.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.start_test.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.start_test.setObjectName("start_test")
        self.verticalLayout_6.addWidget(
            self.start_test, 0, QtCore.Qt.AlignHCenter)
        self.all_test_data = QtWidgets.QGroupBox()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.all_test_data.sizePolicy().hasHeightForWidth())
        self.all_test_data.setSizePolicy(sizePolicy)
        self.all_test_data.setMinimumSize(QtCore.QSize(330, 312))
        self.all_test_data.setStyleSheet(
            "QGroupBox { border: 1px solid black;}")
        self.all_test_data.setObjectName("all_test_data")
        self.scrollArea = QtWidgets.QScrollArea(self.all_test_data)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 300, 280))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 50))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 278))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.checkBox.setObjectName("checkBox")
        # self.verticalLayout_7.addWidget(self.checkBox)
        # self.checkBox_11 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.checkBox_11.setObjectName("checkBox_11")
        # self.verticalLayout_7.addWidget(self.checkBox_11)
        # self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.verticalLayout_7.addWidget(self.checkBox_2)
        # self.checkBox_10 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.checkBox_10.setObjectName("checkBox_10")
        # self.verticalLayout_7.addWidget(self.checkBox_10)
        self.checkbox_spacer = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(self.checkbox_spacer)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.all_test_data)
        self.clear_all_button = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clear_all_button.sizePolicy().hasHeightForWidth())
        self.clear_all_button.setSizePolicy(sizePolicy)
        self.clear_all_button.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setObjectName("clear_all_button")
        self.verticalLayout_6.addWidget(self.clear_all_button)

        self.horizontalLayout_current_test = QtWidgets.QHBoxLayout()
        self.horizontalLayout_current_test.setObjectName(
            "horizontalLayout_current_test")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_current_test = QtWidgets.QLabel()
        self.select_current_test.setFont(font)
        self.select_current_test.setSizePolicy(sizePolicy)
        self.select_current_test.setMinimumSize(QtCore.QSize(30, 0))
        self.current_test_combo = QtWidgets.QComboBox()
        self.current_test_combo.setFont(font)
        self.horizontalLayout_current_test.addWidget(self.select_current_test)
        self.horizontalLayout_current_test.addWidget(self.current_test_combo)

        self.verticalLayout_6.addLayout(self.horizontalLayout_current_test)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        # self.menubar_()
        self.retranslateUi()
        self.validations()

    def menubar_(self,):
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        # .setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        # .setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction()
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction()
        self.actionImport.setObjectName("actionImport")
        self.actionParameters = QtWidgets.QAction()
        self.actionParameters.setObjectName("actionParameters")
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionImport)
        self.menuSettings.addAction(self.actionParameters)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        # QtCore.QMetaObject.connectSlotsByName()
        # self.actionExport.triggered.connect(self.import_clicked)
        QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        # .setWindowTitle(_translate("", "UDTE"))
        self.record_label.setText(_translate("", "Record             :"))
        self.is_roller.setText(_translate("", "Roller"))
        self.speed_label.setText(_translate("", "Speed (mm/s)   :"))
        self.distance_label.setText(_translate("", "Distance (mm)  :"))
        self.select_motor_label.setText(_translate("", "Select motor      :"))
        self.directory_label.setText(_translate("", "Save directory :"))
        self.browse_directory.setText(_translate("", "Browse"))
        self.test_name_label.setText(_translate("", "Test Name     :"))
        # self.move_axis.setText(_translate("", "Move axis"))
        self.record_proximal_force_gauge.setText(
            _translate("", "Proximal Force Gauge"))
        self.record_distal_force_gauge.setText(
            _translate("", "Distal Force Gauge"))
        self.record_video.setText(_translate("", "Video"))
        # self.is_axis.setText(_translate("", "Axis"))
        self.proximal_force_gauge_groupbox.setTitle(
            _translate("", "Proximal force gauge"))
        self.connect_proximal_force_gauge.setText(
            _translate("", "Connect Proximal force gauge"))
        self.set_proximal_zero.setText(_translate("", "Set zero "))
        self.proximal_force_value_label.setText(
            _translate("", "Current force value :"))
        self.proximal_force_value.setText(_translate("", "0.02 N"))
        self.proximal_maximum_force_label.setText(
            _translate("", "Max force : "))
        self.proximal_maximum_force.setText(_translate("", "0.02 N"))
        self.proximal_maximum_force_position_label.setText(
            _translate("", "    at position :"))
        self.proximal_maximum_force_position_value.setText(
            _translate("", "00 mm"))
        self.proximal_average_force.setText(
            _translate("", "Average force : 0.00 N"))
        self.distal_force_gauge_groupbox.setTitle(
            _translate("", "Distal force gauge"))
        self.connect_distal_force_gauge.setText(
            _translate("", "Connect Distal force gauge"))
        self.set_distal_zero.setText(_translate("", "Set zero "))
        self.distal_force_value_label.setText(
            _translate("", "Current force value :"))
        self.distal_force_value.setText(_translate("", "0.00 N"))
        self.distal_maximum_force_label.setText(_translate("", "Max force : "))
        self.distal_maximum_force.setText(_translate("", "0.00 N"))
        self.distal_maximum_force_position_label.setText(
            _translate("", "    at position :"))
        self.distal_maximum_force_position_value.setText(
            _translate("", "00 mm"))
        self.distal_average_force.setText(
            _translate("", "Average force : 0.00 N"))
        self.connect_camera.setText(_translate("", "Connect camera"))
        self.start_test.setText(_translate("", "Start"))
        self.Arduino_Start_Stop.setText(_translate("", "Arduino_Start"))
        self.all_test_data.setTitle(
            _translate("", "Select which tests to plot"))
        # self.checkBox.setText(_translate("", "CheckBox"))
        # self.checkBox_11.setText(_translate("", "CheckBox"))
        # self.checkBox_2.setText(_translate("", "CheckBox"))
        # self.checkBox_10.setText(_translate("", "CheckBox"))
        self.clear_all_button.setText(_translate("", "Clear All"))
        self.select_current_test.setText(_translate("", "Current test"))
        # self.menuFile.setTitle(_translate("", "File"))
        # self.menuSettings.setTitle(_translate("", "Settings"))
        # self.actionExport.setText(_translate("", "Export"))
        # self.actionImport.setText(_translate("", "Import"))
        # self.actionParameters.setText(_translate("", "Parameters"))
        self.proximal_average_force.setText("Average force : -- N")
        self.proximal_maximum_force.setText("--")
        self.proximal_maximum_force_position_value.setText("--")
        self.distal_average_force.setText("Average force : -- N")
        self.distal_maximum_force.setText("--")
        self.distal_maximum_force_position_value.setText("--")

    def validations(self):
        numericals_only = QRegExpValidator(QRegExp("[0-9]*"))
        numbers = QRegExpValidator(QRegExp("[0-9-]*"))
        file_names = QRegExpValidator(QRegExp("[0-9A-Za-z-_]*"))
        self.test_name.setValidator(file_names)
        self.speed_of_motor.setValidator(numericals_only)
        self.distance_to_be_covered.setValidator(numbers)

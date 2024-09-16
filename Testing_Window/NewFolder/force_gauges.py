from mark10_force_reader import mark10_f_values, save_to_file  # ,random_generator
from mark10_force_reader_distal import mark10_f_values_distal#, #random_generator     #   save_to_file,
import queue
import os
from PyQt5.QtWidgets import QMessageBox, QGraphicsPixmapItem
from PyQt5 import QtWidgets, QtGui
from errors import show_error
# from image_taker import image_taker
# from forsentek_force_reader import forsentek_f_values
from colors import colors
# from parameters import para

# from Trackability_Mainwindow import Ui_MainWindow


# import inspect										# add by dev


class conditions_for_proximal():

    def __init__(self, ui):

        self.ui = ui
        # self.ui = Ui_MainWindow()

        ####################################################
        ##### All queues for data ##########################
        # self.record_force_q = queue.Queue()
        # self.record_time_q = queue.Queue()
        # self.image_queue = queue.Queue(1)
        # self.mark10_q = queue.Queue(1)
        #####################################################
        self.proximal_connected = False
        self.distal_connected = False
        self.camera_connected = False
        # self.current_plotter = current_plotter
        # self.all_plotter = all_plotter
        self.colors = colors()
        self.proximal_force = 0
        self.distal_force = 0

        self.temp_force_ = None
        self.temp_time_ = None


###################################################################################################################################################################

        self.proximal_thread = mark10_f_values()

        #################################################
        self.proximal_thread.mark10_connection_fail_signal.connect(
            self.proximal_connection_problem)
        self.proximal_thread.mark10_not_found_signal.connect(
            self.proximal_not_found)
        self.proximal_thread.mark10_connection_lost_signal.connect(
            self.proximal_connection_lost)

        ###################################################
        self.ui.connect_proximal_force_gauge_PB.clicked.connect(
            self.connect_proximal)
        self.ui.set_proximal_zero_PB.clicked.connect(self.proximal_zero_clicked)
        ###
#################################################################################################################################
##################################################################################################################################
#################################################################################################################################

        self.distal_thread = mark10_f_values_distal()

        #################################################
        self.distal_thread.mark10_connection_fail_signal.connect(
            self.proximal_connection_problem)
        self.distal_thread.mark10_not_found_signal.connect(
            self.proximal_not_found)
        self.distal_thread.mark10_connection_lost_signal.connect(
            self.proximal_connection_lost)

        ###################################################
        self.ui.connect_distal_force_gauge_PB.clicked.connect(
            self.connect_distal)
        self.ui.set_distal_zero_PB.clicked.connect(self.distal_zero_clicked)
        ###

###################################################################################################################################################################

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene.addItem(self.pixmap_item)

        # self.images_from_camera = image_taker(
        #     self.proximal_thread, self.distal_thread)
        # # self.images_from_camera.image_signal.connect(self.got_image)

        ###########
        self.errors_ = show_error()
        ####
        self.saver_thread = save_to_file(self.ui)
        ####
        self.maximum_forces = []
        self.maximum_force_x_val = []
        ######
        self.all_proximal_f_data = []
        self.all_proximal_t_data = []
        self.all_proximal_labels = []
        ####
        self.all_distal_f_data = []
        self.all_distal_t_data = []
        self.all_distal_labels = []
        self.checkboxes = []


    def add_checkboxes(self):
        temp_checkbox = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents)
        temp_checkbox.setText(self.all_proximal_labels[-1])
        temp_checkbox.setChecked(True)
        # temp_checkbox.stateChanged.connect(self.update_all_graphs)
        self.checkboxes.append(temp_checkbox)
        self.ui.verticalLayout_7.removeItem(self.ui.checkbox_spacer)
        self.ui.verticalLayout_7.addWidget(temp_checkbox)
        self.ui.verticalLayout_7.addItem(self.ui.checkbox_spacer)
        # self.update_all_graphs()

    def got_force_signal(self, f_vals):
        self.temp_force_ = f_vals

    def got_time_signal(self, t_vals):
        self.temp_time_ = t_vals

    def connect_proximal(self):
        print(self.colors.colors[0])
        print("Clicked in force gauge 216")

        if self.proximal_connected:
            self.proximal_connected = False
            print("i am here if in force gauge 220")
            self.proximal_thread.stop()
            # print(f'Thread still alive? {self.proximal_thread.is_alive()}')
            self.ui.connect_proximal_force_gauge_PB.setStyleSheet(
                "background-color: rgb(255, 170, 0);")
            self.ui.connect_proximal_force_gauge_PB.setText(
                "Connect Proximal force gauge")
        else:
            if self.proximal_thread.connect_com():
                self.proximal_connected = True
                print("i am here else in force gauge 227")
                self.proximal_thread.start()
                # print(type(self.proximal_thread))                           #       it is showing <class 'mark10_force_reader.mark10_f_values'>
                # print(f'Thread still alive? {self.proximal_thread.name}')
                self.ui.connect_proximal_force_gauge_PB.setStyleSheet(
                    "background-color: rgb(99, 255, 138);")
                self.ui.connect_proximal_force_gauge_PB.setText(
                    "Disconnect Proximal force gauge")

    def connect_distal(self):
        print("Clicked")

        if self.distal_connected:
            self.distal_connected = False
            self.distal_thread.stop()
            self.ui.connect_distal_force_gauge_PB.setStyleSheet(
                "background-color: rgb(255, 170, 0);")
            self.ui.connect_distal_force_gauge_PB.setText(
                "Connect Distal force gauge")
        else:
            print("force_gauge_connect_distal_01")
            if self.distal_thread.connect_com():
                self.distal_connected = True
                print("force_gauge_connect_distal_02")
                self.distal_thread.start()
                self.ui.connect_distal_force_gauge_PB.setStyleSheet(
                    "background-color: rgb(99, 255, 138);")
                self.ui.connect_distal_force_gauge_PB.setText(
                    "Disconnect Distal force gauge")

    def proximal_zero_clicked(self):
        print("................................................i am here in force gauge 258 ",self)
        self.proximal_thread.set_zero()
        print("i am here in thread in force gauge 257")
        # self.proximal_thread.update_set_unit()

    ####################################################################################################################################################################

    def proximal_Unit_Update_clicked(self):
        print("i am here in thread in force gauge 261")
        # self.proximal_thread.update_set_unit()
        self.proximal_thread.set_zero()

    ####################################################################################################################################################################

    def proximal_not_found(self):
        print("Proximal force gauge is not connected")
        self.proximal_connected = False
        self.errors_.proximal_not_found()

    def proximal_connection_problem(self):
        print("Got error from thread. Could not connect gauge")
        self.proximal_connected = False
        self.errors_.proximal_connection_problem()

    def proximal_connection_lost(self):
        print("Connection to proximal force gauge has been lost")
        self.ui.connect_proximal_force_gauge_PB.setStyleSheet(
            "background-color: rgb(255, 170, 0);")
        self.ui.connect_proximal_force_gauge_PB.setText(
            "Connect Proximal force gauge")
        self.errors_.proximal_connection_problem()
        self.proximal_connected = False

    def distal_zero_clicked(self):
        self.distal_thread.set_zero()

    def distal_not_found(self):
        print("Distal force gauge is not connected")
        self.distal_connected = False
        self.errors_.distal_not_found()

    def distal_connection_problem(self):
        print("Got error from thread. Could not connect distal gauge")
        self.distal_connected = False
        self.errors_.distal_connection_problem()

    def distal_connection_lost(self):
        print("Connection to distal force gauge has been lost")
        self.ui.connect_distal_force_gauge_PB.setStyleSheet(
            "background-color: rgb(255, 170, 0);")
        self.ui.connect_distal_force_gauge_PB.setText(
            "Connect Proximal force gauge")
        self.errors_.distal_connection_problem()
        self.distal_connected = False

    def got_proximal_force(self, val):
        self.proximal_force = val
        self.ui.proximal_current_force_value_Label.setText(str(val))

    def start_clicked(self):

        pass

    def start_recording(self):
        pass

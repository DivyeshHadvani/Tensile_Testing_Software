from parameters import para
from login import Login
import time
from ui_file import Ui_Form
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from plotter import plotter_and_data
from mark10_force_reader import mark10_f_values, save_to_file   #   ,random_generator
from mark10_force_reader_distal import mark10_f_values_distal, save_to_file, random_generator
from force_gauges import conditions_for_proximal
from os.path import expanduser
import os
from controller import motor_controller
from check_before_start import check_before_start
# from test_data import all_test_data
global f_value_experiment
f_value_experiment = 0


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1100)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setCentralWidget(self.centralwidget)
        self.menus_()
        self.ui = Ui_Form()
        self.ui.setupUi()

        self.parameter_dialog = para()

        self.horizontalLayout.addLayout(self.ui.horizontalLayout_5)
        # self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.show()
        self.ready_for_test = True  # Flag for starting test
        self.should_plot = False
        self.current_running_status = False

        self.plotter = plotter_and_data(self.ui)
        self.ui.graphing_layout.addWidget(self.plotter.canvas)
        self.ui.graphing_layout.addWidget(self.plotter.toolbar)
        self.ui.graphing_layout.addWidget(self.plotter.canvas_all)
        self.ui.graphing_layout.addWidget(self.plotter.toolbar_all)

        self.test_time = 0
        self.test_start_time = 0
        self.button_clicks()
        self.prox = conditions_for_proximal(self.ui)
        self.data_file = None

        ####
        # self.random_thread = random_generator(self.prox.proximal_thread)
        # self.random_thread.sig.connect(self.plot__)
        ####
        self.ui.clear_all_button.clicked.connect(self.clear_all_command)
        ####

        # Controller define
        self.controller = motor_controller(self.ui)
        # self.controller.connect_com()                                 #           dev editing
        self.before_start_checks = check_before_start(
            self.ui, self.plotter, self.prox)
        # GUI updator
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_gui)
        self.update_timer.start(100)
        #####
        self.read_proximal_timer = QtCore.QTimer()
        self.read_proximal_timer.timeout.connect(self.read_proximal_data)
        #####
        self.read_distal_timer = QtCore.QTimer()
        self.read_distal_timer.timeout.connect(self.read_distal_data)
        #####
        self.read_both_timer = QtCore.QTimer()
        self.read_both_timer.timeout.connect(self.read_both)
        #####
        self.ui.current_test_combo.currentIndexChanged.connect(
            self.update_combo)

        self.ui.Arduino_Start_Stop.clicked.connect(
            self.controller.connect_Ardunio)

    def read_proximal_data(self):

        ti = time.time()-self.test_start_time
        # print("ti",ti)
        # print("self.test_start_time",self.test_start_time)
        # print("self.test_time",self.test_time)
        if ti < self.test_time and self.current_running_status:
            self.plotter.temp_proximal_force.append(
                round(self.prox.proximal_thread.present_reading, 4))
            self.plotter.temp_time.append(round(ti, 2))
            self.prox.images_from_camera.displacement = round(
                int(self.ui.speed_of_motor.text())*ti, 2)
            self.plotter.temp_displacement.append(
                self.prox.images_from_camera.displacement)
        else:
            self.read_proximal_timer.stop()
            self.prox.saver_thread.file_name = self.before_start_checks.data_file
            self.prox.saver_thread.p_f_data = self.plotter.temp_proximal_force
            self.prox.saver_thread.t_data = self.plotter.temp_time
            self.prox.saver_thread.dis_data = self.plotter.temp_displacement
            self.prox.saver_thread.which_test = "proximal"
            self.prox.saver_thread.start()
            print("test is stopeed")
            self.plotter.add_proximal_data()
            self.change_start_button()
        pass

    def read_distal_data(self):
        ti = time.time()-self.test_start_time
        if ti < self.test_time and self.current_running_status:
            self.plotter.temp_distal_force.append(
                round(self.prox.distal_thread.present_reading,4))			#	reading)
            self.plotter.temp_time.append(round(ti, 2))
            self.prox.images_from_camera.displacement = round(
                int(self.ui.speed_of_motor.text())*ti, 2)
            self.plotter.temp_displacement.append(
                self.prox.images_from_camera.displacement)
        else:
            self.read_distal_timer.stop()
            self.prox.saver_thread.file_name = self.before_start_checks.data_file
            self.prox.saver_thread.d_f_data = self.plotter.temp_distal_force
            self.prox.saver_thread.t_data = self.plotter.temp_time
            self.prox.saver_thread.dis_data = self.plotter.temp_displacement
            self.prox.saver_thread.which_test = "distal"
            self.prox.saver_thread.start()
            self.plotter.add_distal_data()
            self.change_start_button()
        pass

    def read_both(self):
        ti = time.time()-self.test_start_time
        if ti < self.test_time and self.current_running_status:
            p = self.prox.proximal_thread.present_reading
            d = self.prox.distal_thread.present_reading                         #   reading
            if p == 0:
                self.plotter.temp_push_values.append(0)
            else:
                self.plotter.temp_push_values.append((d/p)*100)
            self.plotter.temp_proximal_force.append(p)
            self.plotter.temp_distal_force.append(d)
            self.prox.images_from_camera.displacement = round(
                int(self.ui.speed_of_motor.text())*ti, 2)
            self.plotter.temp_displacement.append(
                self.prox.images_from_camera.displacement)
            self.plotter.temp_time.append(ti)
        else:
            self.read_both_timer.stop()
            self.prox.saver_thread.file_name = self.before_start_checks.data_file
            self.prox.saver_thread.p_f_data = self.plotter.temp_proximal_force
            self.prox.saver_thread.d_f_data = self.plotter.temp_distal_force
            self.prox.saver_thread.push_data = self.plotter.temp_push_values
            self.prox.saver_thread.t_data = self.plotter.temp_time
            self.prox.saver_thread.dis_data = self.plotter.temp_displacement
            self.prox.saver_thread.which_test = "both"
            self.prox.saver_thread.start()
            self.plotter.add_both_data()
            self.change_start_button()
        pass

    def update_gui(self):
        self.ui.proximal_force_value.setText(
            str(self.prox.proximal_thread.present_reading))
        self.ui.distal_force_value.setText(
            str(self.prox.distal_thread.present_reading))                      #   str(self.prox.distal_thread.reading))
        self.prox.got_image()
        if self.current_running_status:
            self.plotter.plot_now()

    def read_data(self):
        self.prox.proximal_thread.present_reading

    def clear_all_command(self):
        message = "Are you sure you want to clear all data ? \n\nYou will be unable to retrieve data once cleared !"
        warning = QMessageBox(
            QMessageBox.Warning, "Clear all data", message, QMessageBox.NoButton, self)
        warning.addButton("Clear", QMessageBox.AcceptRole)
        warning.addButton("Cancel", QMessageBox.RejectRole)
        if warning.exec_() == QMessageBox.AcceptRole:
            self.plotter.clear_all_data()
        else:
            pass

    def button_clicks(self):
        self.ui.browse_directory.clicked.connect(self.browse_now)
        self.ui.start_test.clicked.connect(self.start_testing)
        # self.ui.move_axis_right_one.clicked.connect(self.move_axis_right_one)
        # self.ui.move_axis_left_one.clicked.connect(self.move_axis_left_one)
        # self.ui.move_axis_right_end.clicked.connect(self.move_axis_right_end)
        # self.ui.move_axis_left_end.clicked.connect(self.move_axis_left_end)

    def browse_now(self):
        # options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        self.my_dir = QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QFileDialog.ShowDirsOnly)
        self.ui.save_directory.setText(self.my_dir)
        print(self.my_dir)
        print(self.controller.controller_connected)

    def get_export_name(self):
        export_name, _ = QFileDialog.getSaveFileName(self,
                                                     "Export",
                                                     "",
                                                     "Pickle (*.pkl)")
        return export_name

    def get_import_name(self):
        import_name, _ = QFileDialog.getOpenFileName(self,
                                                     "Import",
                                                     "",
                                                     "Pickle (*.pkl)")
        return import_name

    def start_testing(self):

        if not self.current_running_status:
            self.before_start_checks.checks()

            #################### Check if controller is connected ##########################
            if not self.controller.controller_connected:
                self.before_start_checks.ready_for_test = False
                _ = QMessageBox.critical(self, "Controller not connected",  # error message
                                         "Test cannot be performed, because controller is not connected. Please connect the controller and restart the software in order to perform test.",
                                         QMessageBox.Retry)

            ###############################################################################
            #################  Start recording ############################################
            if self.before_start_checks.ready_for_test and not self.current_running_status:
                self.test_time = abs(float(self.ui.distance_to_be_covered.text(
                ))/float(self.ui.speed_of_motor.text()))  # Time for which it should be recorded

                # print("i am here self.test_time in start_testing", self.test_time)
                self.current_running_status = True
                
                if self.ui.is_roller.isChecked():
                    self.controller.rotate_roller_signal(
                        int(self.ui.speed_of_motor.text()), int(self.ui.distance_to_be_covered.text()))

                if self.ui.record_video.isChecked():
                    self.prox.images_from_camera.start_recording(
                        self.test_time, self.ui.save_directory.text()+"/"+self.ui.test_name.text()+"/video.avi")

                if self.ui.record_proximal_force_gauge.isChecked() and not self.ui.record_distal_force_gauge.isChecked():
                    # self.prox.proximal_zero_clicked()
                    # print("i am here self.test_start_time in def start_testing")
                    time.sleep(1)
                    self.test_start_time = time.time()
                    self.read_proximal_timer.start(20)                                  #   auto restart in every 20 milisecond
                    self.plotter.what_plot = "proximal"

                if not self.ui.record_proximal_force_gauge.isChecked() and self.ui.record_distal_force_gauge.isChecked():
                    # self.prox.distal_zero_clicked()
                    time.sleep(1)
                    self.test_start_time = time.time()
                    self.read_distal_timer.start(20)
                    self.plotter.what_plot = "distal"

                if self.ui.record_proximal_force_gauge.isChecked() and self.ui.record_distal_force_gauge.isChecked():
                    # self.prox.proximal_thread.proximal_zero_clicked()
                    time.sleep(1)
                    self.prox.distal_zero_clicked()
                    self.test_start_time = time.time()
                    self.read_both_timer.start(20)
                    self.plotter.what_plot = "both"

                if self.ui.record_video.isChecked():
                    self.prox.images_from_camera.record_time = self.test_time
                    self.prox.images_from_camera.video_file_name = self.ui.save_directory.text(
                    )+"/"+self.ui.test_name.text()+"/"+self.ui.test_name.text()+".avi"
                    self.prox.images_from_camera.should_record = True

                # if self.ui.is_axis.isChecked():
                #     self.controller.rotate_axis_signal(int(self.ui.speed_of_motor.text()), int(
                #         self.ui.distance_to_be_covered.text()))  # Sending signal to controller for motor movement
                # else:
                #     self.controller.rotate_roller_signal(
                #         int(self.ui.speed_of_motor.text()), int(self.ui.distance_to_be_covered.text()))

                # if self.ui.is_roller.isChecked():
                #     self.controller.rotate_roller_signal(
                #         int(self.ui.speed_of_motor.text()), int(self.ui.distance_to_be_covered.text()))
                pass

            if self.current_running_status:
                self.ui.start_test.setStyleSheet(
                    "background-color: rgb(255, 170, 0);")
                self.ui.start_test.setText("Stop")
                print("I am here in main test is started")  # devediting
        else:
            self.change_start_button()

    def change_start_button(self):
        self.ui.start_test.setStyleSheet(
            "background-color: rgb(99, 255, 138);")
        self.ui.start_test.setText("Start")
        self.controller.stop_rotations()
        self.current_running_status = False

    def closing_in(self):
        self.controller.stop()

    # def move_axis_right_one(self):
    #     self.controller.rotate_axis_one_right()

    # def move_axis_left_one(self):
    #     self.controller.rotate_axis_one_left()

    # def move_axis_right_end(self):
    #     self.controller.rotate_axis_signal(
    #         1, 50, "move_axis_right_end_main.py")

    # def move_axis_left_end(self):
    #     self.controller.rotate_axis_signal(-1,
    #                                        50, "move_axis_left_end_main.py")

    def export_data(self):
        name = self.get_export_name()
        print(name)
        self.plotter.save_pkl(name)
        pass

    def import_data(self):
        name = self.get_import_name()
        self.plotter.load_pkl(name)
        pass

    def menus_(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(self)
        self.actionImport.setObjectName("actionImport")

        self.actionParameters = QtWidgets.QAction(self)
        self.actionParameters.setObjectName("actionParameters")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImport)
        self.menuSettings.addAction(self.actionParameters)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "UDTE"))
        self.menuFile.setTitle(_translate("self", "File"))
        self.menuSettings.setTitle(_translate("self", "Settings"))
        self.actionSave.setText(_translate("self", "Export"))
        self.actionImport.setText(_translate("self", "Import"))
        self.actionParameters.setText(_translate("self", "Parameters"))
        self.actionParameters.triggered.connect(self.setting_main)
        self.actionImport.triggered.connect(self.import_data)
        self.actionSave.triggered.connect(self.export_data)

    def setting_main(self):                       #   when we click parameter option in manu
        print("now i am here ac in main")
        self.parameter_dialog.load_para()
        self.parameter_dialog.find_devices()
        self.parameter_dialog.show()

    def update_combo(self, index_combo):
        print(index_combo)
        if index_combo >= 0:
            self.plotter.combo_changes(index_combo)
        else:
            pass
        pass


def close_it(app, ui):
    app.exec_()
    try:
        ui.closing_in()
    except:
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login = Login()
    # if login.exec_() == QtWidgets.QDialog.Accepted:
    ui = AppWindow()
    ui.show()
    sys.exit(close_it(app, ui))

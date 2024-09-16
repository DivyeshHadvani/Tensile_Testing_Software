from PyQt5 import QtCore
import time
import serial
import serial.tools.list_ports
import csv
import numpy as np
import random
import pickle
from ui_file import Ui_Form

import inspect


class mark10_f_values(QtCore.QThread):
    # Signal which indicates failing of mark10 fourge gauge
    mark10_connection_fail_signal = QtCore.pyqtSignal()
    mark10_not_found_signal = QtCore.pyqtSignal()
    mark10_connection_lost_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(mark10_f_values, self).__init__()
        # self.com = "COM3"
        self.should_read = False  # Flag which will decide should stop or not
        self.zero_value = 0
        self.read_value = 0
        self.found = True
        self.present_reading = 0
        self.record_starting_time = 0
        self.record = False
        self.s = None
        self.record_time = 0
        self.time_record = []
        self.force_record = []
        self.click_zero = False
        self.ui = Ui_Form()
        self.change_unit = False
        print("self.change_unit_01",self.change_unit)

    def load_para(self):
        try:
            with open("parameters.pkl", 'rb') as para_file:
                self.all_parameters = pickle.load(para_file)
            # print("all_parameters in mark10 41",self.all_parameters)
            self.com = self.all_parameters['proximal_port']
            self.baude = int(self.all_parameters['proximal_baude'])
            self.setunit = self.all_parameters['Unit_selection']
            print("self.setunit",self.setunit)
            # self.proximal_baude_01.setText(str(self.all_parameters['proximal_baude']))

        except:
            print("Parameters file is not available")
            self.com = "COM1"
            self.baude = 9600
            pass

    def update_set_unit(self):
        print("Came to True........................................")
        # self.change_unit = True

        # self.change_Unit_value.emit(self.change_unit)
        # if self.change_unit:
        #     self.load_para()

        #     if self.setunit == "kgf vs mm":
        #         self.s.write(b'KG\r\n')
        #     else:
        #         self.s.write(b'N\r\n')

        #     self.change_unit = False
    #     self.load_para()
    #     try:
    #         print("self.setunit in try mark10 57",self.setunit)
    #         if self.setunit == "kgf vs mm":
    #             # self.s.close()
    #             try:
    #                 self.s.close()
    #                 print("here 62")
    #             except:
    #                 pass
    #             try:
    #                 self.s = serial.Serial(self.com, self.baude)
    #                 print("here 67")
    #             except:
    #                 pass
    #             # print("to check serial port is open or not 60", self.s.is_open)
    #             # self.s = serial.Serial(self.com, self.baude)
    #             # print("to check serial port is open or not 62", self.s.is_open)
    #             self.s.write(b'KG\r\n')

    #             try:
    #                 self.s.close()
    #                 print("here 62")
    #             except:
    #                 pass

    #         else:
    #             try:
    #                 self.s.close()
    #                 print("here 78")
    #             except:
    #                 pass
    #             try:
    #                 self.s = serial.Serial(self.com, self.baude)
    #                 print("here 84")
    #             except:
    #                 pass
    #             # self.s.close()
    #             # print("to check serial port is open or not 68", self.s.is_open)
    #             # self.s = serial.Serial(self.com, self.baude)
    #             # print("to check serial port is open or not 70", self.s.is_open)
    #             self.s.write(b'N\r\n')

    #             try:
    #                 self.s.close()
    #                 print("here 62")
    #             except:
    #                 pass

    #     except:
    #         print("na thyu in mark 10 94")
    #         pass
    #     pass

    def connect_com(self):  # This function returns mark 10 object
        self.load_para()

        if self.found:                                          # checking flag
            try:
                # try:
                #     print("to check serial port is open or not 70", self.s.is_open)
                # except:
                #     pass

                self.s = serial.Serial(self.com, self.baude)
                # print("to check serial port is open or not 73", self.s.is_open)
                time.sleep(0.1)

                if self.setunit == "kgf vs mm":
                    self.s.write(b'KG\r\n')
                else:
                    self.s.write(b'N\r\n')

                # self.s.write(b'N\r\n')      #   self.s.write(b'LB\r\n')         Pg.22
                time.sleep(0.1)
                self.s.write(b'CUR\r\n')
                print("Connected successfully")
                self.should_read = True
                return True  # Set force unit to Newton
            except:
                # print("to check serial port is open or not 84", self.s.is_open)
                self.mark10_connection_fail_signal.emit()
                return False
        else:
            self.mark10_not_found_signal.emit()
            print("Didn't found any mark10")
            return False

    # This function finds the com port where mark 10 is connected  using manufacturer
    def find_com(self):
        comlist = serial.tools.list_ports.comports()      # gives list of active COM ports
        connected = []
        for element in comlist:
            connected.append(element)
        for connection in connected:
            print(connection.manufacturer)
            if connection.manufacturer == 'Prolific':
                # COM port where mark 10 is connected
                self.com = connection.device
                self.found = True                                # Connection flag

    def run(self):

        # self.s = self.connect_com()                             ### Call for setup
        start = time.time()  # Start time
        while self.should_read:  # Loop will start for reading the data
            if self.click_zero:
                print("self.click_zero...mark10_force_gauge 177 ",self.click_zero)
                time.sleep(0.1)
                self.s.write(b'Z\r\n')
                self.click_zero = False
                print("self.click_zero...mark10_force_gauge 181 ",self.click_zero)
                time.sleep(0.1)
                pass

            try:
                # self.update_set_unit()

                # print("self.change_unit_024",self.change_unit)
                # time.sleep(1)

                if self.change_unit == True:
                    print("self.change_unit_034",self.change_unit)
                    self.load_para()
                    if self.setunit == "kgf vs mm":
                        self.s.write(b'KG\r\n')
                    else:
                        self.s.write(b'N\r\n')
                    self.change_unit = False
                    print("self.change_unit_034",self.change_unit)


                # if self.setunit == "kgf vs mm":
                #     self.s.write(b'KG\r\n')
                # else:
                #     self.s.write(b'N\r\n')

                # Sending signal to force gauge to get current force value
                self.s.write(b'?\r\n')
                # time.sleep(0.01)                                  ### Wait for 10 ms
                available_bytes = self.s.in_waiting
                if available_bytes >= 8:
                    try:
                        # print("readline",self.s.readline())
                        self.read_value = float(self.s.readline()[:5])
                        # print("self.read_value",self.read_value)
                        # Present value variable
                        self.present_reading = abs(
                            round((self.read_value - self.zero_value), 4))
                        # print("self.present_reading",self.present_reading)
                    except:
                        pass
            except:
                self.s.close()
                self.should_read = False
                print('getting out')
                self.mark10_connection_lost_signal.emit()
                break
        pass

    def start_recording(self, record_time):
        self.record_starting_time = time.time()
        self.record_time = record_time
        self.record = True

    def stop(self):
        self.should_read = False  # This will toggle the flag and stop the force reading
        time.sleep(0.1)
        self.s.close()  # break com connection and then leave the thread

    def set_zero(self):
        # self.zero_value = self.read_value                		    ### This will give a new zero value
        print("Came to set zero",self)
        print("self.zero_01 mark10_force_gauge 242",self.click_zero)
        try:
            self.click_zero = True
        except:
            pass
        print("self.zero_02 mark10_force_gauge 247",self.click_zero)


class save_to_file(QtCore.QThread):

    d_all_signal = QtCore.pyqtSignal(list, list)

    def __init__(self, ui):
        super(save_to_file, self).__init__()
        self.set_all_none()
        # self.ui = Ui_Form()                       #   this is not working like main.py why??? plz check
        self.ui = ui

        # self.seepdm = int(self.ui.speed_of_motor.text())
        # # print("i am here in mark10 235",int(self.ui.speed_of_motor.text()))
        # print("i am here in mark10 235",self.seepdm)

    def set_all_none(self):
        self.file_name = None
        self.p_f_data = []
        self.d_f_data = []
        self.t_data = []
        self.dis_data = []
        self.push_data = []
        self.which_test = None

    def run(self):

        print("i am here in Run_152_mark10")

        self.load_para()

        if self.which_test == "proximal":
            self.write_proximal_data()
        elif self.which_test == "distal":
            self.write_distal_data()
        elif self.which_test == "both":
            self.write_both_data()
        else:
            print("Did not know which file to write")
        pass

    def write_proximal_data(self):
        print("i am here in write_proximal_data")
        # print(self.file_name)
        with open(self.file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            for i in range(len(self.keysList)):
                data_to_write = [self.keysList[i],
                                 self.ValueList[i]]
                csvwriter.writerow(data_to_write)


            heads = ["Time", "Displacement", "Proximal Force(N)"]
            csvwriter.writerow(heads)

            print("len(self.t_data)",len(self.t_data))
            print("")
            print("self.t_data",self.t_data)

            for i in range(len(self.t_data)):
                data_to_write = [self.t_data[i],
                                 self.dis_data[i], self.p_f_data[i]]
                csvwriter.writerow(data_to_write)

        self.set_all_none()
        pass

    def write_distal_data(self):
        print("i am here in write_distal_data")
        print("t_data",self.t_data)
        with open(self.file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            heads = ["Time", "Displacement", "Distal Force(N)"]
            csvwriter.writerow(heads)
            for i in range(len(self.t_data)):
                data_to_write = [self.t_data[i],
                                 self.dis_data[i], self.d_f_data[i]]
                csvwriter.writerow(data_to_write)
        self.set_all_none()
        pass

    def write_both_data(self):
        print("i am here in write_both_data")
        print("t_data",self.t_data)
        with open(self.file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            heads = ["Time", "Displacement",
                     "Proximal Force(N)", "Distal Force(N)", "Pushability (%)"]
            csvwriter.writerow(heads)
            for i in range(len(self.t_data)):
                data_to_write = [self.t_data[i], self.dis_data[i], self.p_f_data[i],
                                 self.d_f_data[i], self.push_data[i]]
                csvwriter.writerow(data_to_write)
        self.set_all_none()
        pass

    #######################################################################################################################################################
    #   edited by dev

    def load_para(self):
        try:
            print("Load para in mark10 226")
            with open("parameters.pkl",'rb') as para_file:
                self.all_parameters = pickle.load(para_file)
            # print("i am here in mark10 229",self.all_parameters)
            # print("i am here in mark10 230",type(self.all_parameters))

            self.keysList = list(self.all_parameters.keys())
            self.ValueList = list(self.all_parameters.values())
            self.keysList.append("Speed (mm/s)")
            # print("i am here in mark10 235",int(self.ui.speed_of_motor.text()))
            self.ValueList.append(int(self.ui.speed_of_motor.text()))
            print(self.keysList)
            print(self.ValueList)

            self.proximal_baude.setText(str(self.all_parameters['proximal_baude']))
            self.distal_baude.setText(str(self.all_parameters['distal_baude']))
            self.Arduino_baude.setText(str(self.all_parameters['Arduino_baude']))
            self.roller_dia.setText(self.all_parameters['roller_dia'])
            self.roller_steps.setText(self.all_parameters['roller_steps'])
            self.axis_pitch.setText(self.all_parameters['axis_pitch'])
            self.axis_steps.setText(self.all_parameters['axis_steps'])
            self.buttonBox.accepted.connect(self.accept) # type: ignore

        except:
            pass


    #######################################################################################################################################################


# class random_generator(QtCore.QThread):         #   main.py self.random_thread = random_generator(self.prox.proximal_thread)
#     sig = QtCore.pyqtSignal(list, list)

#     def __init__(self, gg):
#         super(random_generator, self).__init__()
#         self.times = []
#         self.val = []
#         self.gg = gg
#         self.emp = 1
#         print("self.gg",self.gg)

#     def run(self):
#         print("i am here in Run_208_mark10")
#         self.times = []
#         self.val = []
#         i = 0
#         start = time.time()
#         s_t = time.time()
#         while True:
#             self.emp = self.gg.present_reading
#             temp = random.randint(1, 100)
#             self.times.append(time.time()-s_t)
#             self.val.append(temp)
#             i = i+1
#             if (time.time()-start) >= 0.1:
#                 self.sig.emit(self.times, self.val)
#                 start = time.time()
#             if (time.time()-s_t) >= 10:
#                 break
#             time.sleep(0.1)

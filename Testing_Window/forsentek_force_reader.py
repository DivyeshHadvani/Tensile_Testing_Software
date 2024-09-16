from PyQt5 import QtCore
import time
import serial
import serial.tools.list_ports
import pickle


class forsentek_f_values(QtCore.QThread):
    # Signal which indicates failing of mark10 fourge gauge
    forsentek_connection_fail_signal = QtCore.pyqtSignal()
    # Signal which indicates with the given manufacturer, forsentek was not found
    forsentek_not_found_signal = QtCore.pyqtSignal()
    # Signal for connection inturrption or lost
    forsentek_connection_lost_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(forsentek_f_values, self).__init__()
        # self.com = "COM5"
        self.should_read = False  # Flag which will decide should stop or not
        self.zero_value = 0
        self.found = True
        self.present_reading = 0
        self.record_starting_time = 0
        self.record = False
        self.s = None
        self.record_time = 0
        self.time_record = []
        self.force_record = []
        self.read_value = 0
        self.reading = 0

    def find_com(self):
        comlist = serial.tools.list_ports.comports()
        connected = []
        for element in comlist:
            connected.append(element)
        for connection in connected:
            if connection.manufacturer == 'Prolific':
                self.com = connection.device
                self.found = True

    def load_para(self):
        try:
            print("1")
            with open("parameters.pkl", 'rb') as para_file:
                print("2")
                self.all_parameters = pickle.load(para_file)
                print("3")
            # print(self.all_parameters)
            self.com = self.all_parameters['distal_port']
            print(self.com)
            self.baude = int(self.all_parameters['distal_baude'])
            print(self.baude)
        except:
            print("Parameters file is not available")
            self.com = "COM5"
            self.baude = 9600
            pass

    def connect_com(self):  # This function returns mark 10 object
        self.load_para()
        if self.found:                                          # checking flag
            # self.s = serial.Serial(self.com, self.baude)
            try:
                print("self.com",self.com)
                print("self.baude",self.baude)
                self.s = serial.Serial(self.com, self.baude)
                print("Connected successfully")
                self.should_read = True
                return True  # Set force unit to Newton
            except:
                print("distal locha hua")
                self.forsentek_connection_fail_signal.emit()
                return False
        else:
            self.forsentek_not_found_signal.emit()
            print("Didn't found Forsentek load cell")
            return False

    def run(self):
        start = time.time()
        # print("start_initial",start)
        while self.should_read:
            try:
                # print("self.s.in_waiting",self.s.in_waiting)                                              #   This is very useful
                if self.s.in_waiting >= 16:
                    if (time.time() - start) > 0.01:
                        _ = self.s.readline()
                        
                        present_reading = self.s.readline()
                        # print("present_reading",present_reading)                                              #   This is very useful
                        # print("present_reading[5]",chr(present_reading[5]))                                              #   This is very useful
                        
                        if chr(present_reading[5]) == 'A' or chr(present_reading[5]) == '@':
                            self.read_value = '+' + \
                                str(round(
                                    int(present_reading[6:-2]) * 0.00001, 5))
                            # print("self.read_value",type(self.read_value))                                              #   This is very useful
                        else:
                            self.read_value = '-' + \
                                str(round(
                                    int(present_reading[6:-2]) * 0.00001, 5))
                            # print("self.read_value",type(self.read_value))                                              #   This is very useful
                        # self.s.flushInput()
                        self.reading_ = float(self.read_value)*9.81
                        # print("self.reading_",self.reading_)                                              #   This is very useful
                        self.reading = round(
                            (self.reading_ - self.zero_value), 2)
                        start = time.time()
                        # print("start_Final",start)
            except KeyboardInterrupt:
                self.s.close()
                print('getting out')
                break
        pass

    def stop(self):
        self.should_read = False  # This will toggle the flag and stop the force reading
        time.sleep(10)
        self.s.flushInput()
        self.s.close()

    def set_zero(self):
        print("came to set zero Distal")
        try:
            self.zero_value = self.reading_  # This will give a new zero value
        except:
            pass

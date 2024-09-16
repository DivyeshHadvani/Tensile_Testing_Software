###################################################################
######## Made for mototr controller using arduino #################
###################################################################
import serial
import serial.tools.list_ports
from numpy import pi
from errors import show_error
import pickle
from colors import colors
import time


class motor_controller():
    def __init__(self, ui):
        # Controller manufacturer
        self.controller_manu = ["FTDI" ,"Arduino LLC (www.arduino.cc)", "wch.cn"]   #  ["Arduino LLC (www.arduino.cc)", "wch.cn"]      #   "Microsoft" 
        # print("controller_manu",self.controller_manu)
        self.found = False
        self.com = None
        self.controller_connected = False
        self.errors_ = show_error()
        self.Arduino_connected = False
        self.colors = colors()
        self.ui = ui
    
    """

    # This function finds the com port where arduino is connected  using manufacturer
    def find_com(self):
        # gives list of active COM ports
        comlist = serial.tools.list_ports.comports()
        connected = []
        port_name = []
        for element in comlist:
            connected.append(element)
            # print("com_list_dev",connected)
        
        rank_of_port = 0;
        # print("element connected",connected)

        for connection in connected:
            rank_of_port = rank_of_port + 1
            print("rank_of_port_",rank_of_port)
            print("com port",connection)
            print(connection.manufacturer)
            print("     ")
            # for items in self.controller_manu:
            #     if connection.manufacturer == items:                         #   if connection.manufacturer == self.controller_manu:
            #         print("items",items)
            #         print("connection.manufacturer",connection.manufacturer)
            #         print("connection",connection)
            #         print("rank_of_port",rank_of_port)
            #         # COM port where mark 10 is connected
            #         self.com = connection.device
            #         self.found = True
            #         break
            
            # Both are same for loop and if loop
                
            if connection.manufacturer in self.controller_manu:                         #   if connection.manufacturer == self.controller_manu:
                # print("connection.manufacturer",connection.manufacturer)
                # print("connection",connection)
                # print("rank_of_port",rank_of_port)
                # COM port where mark 10 is connected
                self.com = connection.device    
                port_name.append(connection.device)
                print("port_name",port_name)
                self.found = True

    def connect_com(self):  # This function returns controller connected object
        self.find_com()
        print("self.found_last",self.found)
        print("self.com",self.com)
        if self.found:                                          # checking flag
            try:
                self.s = serial.Serial(self.com, 9600)
                print("connected port", self.com)
            except:
                print("connection problem")
            try:
                # self.s = serial.Serial(self.com, 9600)
                print("Controller is connected successfully")
                print("I am here, connect_com Dev")  # devediting
                self.controller_connected = True
                return True
            except:
                print("Unable to connect controller")

                self.errors_.controller_connection_problem()
                return False
        else:
            print("Didn't found controller")
            self.errors_.controller_not_found()
            return False
    """
    
    ########################################################################################################################################################################
    
    def connect_com(self):  # This function returns Arduino controller object
        self.load_para()
        if self.found:                                          # checking flag
            try:
                print("self.com",self.com)
                print("self.baude",self.baude)
                self.s = serial.Serial(self.com, self.baude)
                print("Connected successfully")
                self.controller_connected = True
                return True  # Set force unit to Newton
            except:
                print("Arduino locha hua")
                self.errors_.controller_connection_problem()
                return False
        else:
            print("Didn't found Arduino controller")
            self.errors_.controller_not_found()
            return False
        
    ########################################################################################################################################################################

    # def rotate_axis_signal(self, speed, distance,nam):
    #     self.nam = nam 
    #     print(self.nam)
    #     stpPrev = 10000                         #   51200
    #     roller_dia = 4
    #     steps = int(stpPrev*abs(distance)/(roller_dia))  # pi*
    #     time = float(abs(distance))/speed
    #     tps = int(float(time*(10**6))/float(steps))
    #     ###########################################################################################
    #     ################ Format of command is ---- axis/roller,number of steps,delay time #########
    #     ###########################################################################################
    #     command = 'a,'+str(tps)+","+str(steps)+","+str(distance/abs(distance))
    #     # print(command)
    #     print("rotate_axis_signal",command)
    #     if self.controller_connected:
    #         self.s.write(command.encode('utf-8'))
    #         print("I am here, Dev010")  # devediting
    #         # print(command.encode('utf-8'))															# write by me
    #         if self.s.in_waiting > 0:
    #             print(self.s.read(self.s.in_waiting))
    #             # print(command.encode('utf-8'))															# write by me
    #         else:
    #             pass
    #     else:
    #         print("Controller is not connected")
    #         self.errors_.cannot_move_motor()

    def rotate_roller_signal(self, speed, distance):
        stpPrev = 10000                         #   51200
        roller_dia = 25  # 25
        steps = int(stpPrev*abs(distance)/(roller_dia*pi))  # pi*                  
        time1 = float(abs(distance))/speed
        
        tps = int(float(time1*(10**6))/float(steps))
        command = 'r,'+ str(tps) + "," + str(round(time1*1000)) + \
            ","+str(distance/abs(distance))
            
        # print("rotate_roller_signal steps",steps)
        # print("rotate_roller_signal time",time1)
        # print("rotate_roller_signal tps",tps)
        # print("rotate_roller_signal distance",distance)
        # print("rotate_roller_signal command",command)
        if self.controller_connected:
            self.s.write(command.encode('utf-8'))
            print("yupee i am sending code")
            # time.sleep(2)                                         #   self.s.in_waiting > 0: takes 2 sec means arduino gives reply between 1 and 2 sec
            # print(command.encode('utf-8'))															# write by me
            if self.s.in_waiting > 0:
                print("yupee i am waiting for reply")
                print("roller read",self.s.read(self.s.in_waiting))
            else:
                pass
        else:
            print("Controller is not connected")
            self.errors_.cannot_move_motor()

    # def rotate_axis_one_left(self):
    #     if self.controller_connected:
    #         command = 'a,100,10000,-1'                                                                   #   'a,10,51200,-1'
    #         self.s.write(command.encode('utf-8'))
    #         if self.s.in_waiting > 0:
    #             print("axis read left",self.s.read(self.s.in_waiting))
    #         else:
    #             pass
    #     else:
    #         print("Controller is not connected")
    #         self.errors_.cannot_move_motor()

    # def rotate_axis_one_right(self):
    #     if self.controller_connected:
    #         command = 'a,100,10000,-1'                                                                   #   'a,10,51200,1'
    #         self.s.write(command.encode('utf-8'))
    #         if self.s.in_waiting > 0:
    #             print("axis read right",self.s.read(self.s.in_waiting))
    #         else:
    #             pass
    #     else:
    #         print("Controller is not connected")
    #         self.errors_.cannot_move_motor()

    def stop_rotations(self):
        # self.s.write(b'stop\r\n')
        self.s.write(b'stop,,,')
        # time.sleep(2)                                         #   self.s.in_waiting > 0: takes 2 sec means arduino gives reply between 1 and 2 sec
        # print(command.encode('utf-8'))															# write by me
        if self.s.in_waiting > 0:
            print("yupee i am waiting for reply in stop")
            print("roller read in stop",self.s.read(self.s.in_waiting))
        else:
            pass

    def stop(self):
        self.s.close()
        print("Disconnected successfully")
          
    def load_para(self):
        try:
            with open("parameters.pkl", 'rb') as para_file:
                self.all_parameters = pickle.load(para_file)
            # print(self.all_parameters)
            self.com = self.all_parameters['Arduino_port']
            self.baude = int(self.all_parameters['Arduino_baude'])
            self.found = True
        except:
            print("Parameters file is not available")
            self.com = "COM5"
            self.baude = 9600
            pass
        
    def connect_Ardunio(self):
        print(self.colors.colors[0])
        print("Clicked")
        print("Arduino_connected",self.Arduino_connected)
        print("self.controller_connected",self.controller_connected)
        
        if self.Arduino_connected == True:
            self.Arduino_connected = False
            print("i am here false Arduino")
            # self.proximal_thread.stop()
            self.ui.Arduino_Start_Stop.setStyleSheet(
                "background-color: rgb(255, 170, 0);")
            self.ui.Arduino_Start_Stop.setText(
                "Arduino_Start")
            self.controller_connected = False
            self.s.close()

        elif self.Arduino_connected == False:
            self.connect_com()
            if self.controller_connected == True:           
                self.Arduino_connected = True
                print("i am here True Arduino")
                # self.proximal_thread.start()
                self.ui.Arduino_Start_Stop.setStyleSheet(
                    "background-color: rgb(99, 255, 138);")
                self.ui.Arduino_Start_Stop.setText(
                    "Arduino_Stop")
                
                print("i am here in mark10 235",self.ui.speed_of_motor.text())

            # if self.proximal_thread.connect_com():
            #     self.Arduino_connected = True
            #     # print("i am here false")
            #     # self.proximal_thread.start()
            #     self.ui.Arduino_Start_Stop.setStyleSheet(
            #         "background-color: rgb(99, 255, 138);")
            #     self.ui.Arduino_Start_Stop.setText(
            #         "Arduino_Stop")

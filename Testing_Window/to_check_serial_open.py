# import serial
# import time

# ser = serial.Serial()
# ser.braudrate = 9600
# ser.port = "/dev/ttyUSB0"
# ser.open()

# print(ser.name)
# if ser.isOpen():
#     print("serial is open!")

# ser.close()

import serial

# ser = serial

# ser = serial.Serial("COM21", 115200, timeout=10)

ser = serial.Serial("COM5", 9600, timeout=10)

try:
  ser = serial.Serial("COM21", 115200, timeout=10)

  while ser.read():
    print ('serial open')

  print ('serial closed')
  ser.close()

except serial.serialutil.SerialException:
  print ('exception')
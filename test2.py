import serial

if serial.Serial('COM9', 9600).isOpen() == False:
    ser = serial.Serial('COM9', 9600)
    print("here")

arduino_output = ser.readline()
string_n = arduino_output.decode()
string = string_n.rstrip()

print(string)
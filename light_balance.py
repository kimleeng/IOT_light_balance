import serial
arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
while True:
    if(arduinoSerialData.inWaiting()>0):
        arduino_data = arduinoSerialData.readline()
        print(arduino_data)

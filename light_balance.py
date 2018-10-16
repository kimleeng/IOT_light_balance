#/usr/bin/python3
import serial
import phue

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

hue_bridge = phue.Bridge('192.168.1.3')
hue_bridge.connect()

while True:
    if(arduinoSerialData.inWaiting()>0):
        arduino_data = arduinoSerialData.readline()
        print(arduino_data)
        analog_value = int(arduino_data.strip())
        if analog_value < 100:
            hue_bridge.set_light([5,6], 'bri', 1)
        elif analog_value > 400:
            hue_bridge.set_light([5,6], 'bri', 254)
        else:
            hue_bridge.set_light([5,6], 'bri', 100)


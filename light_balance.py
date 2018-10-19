#/usr/bin/python3
import serial
import phue
import math
import random

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

hue_bridge = phue.Bridge('192.168.1.3')
hue_bridge.connect()

while True:
    if(arduinoSerialData.inWaiting()>0):
        arduino_data = arduinoSerialData.readline()
        print(arduino_data)
        analog_value = int(arduino_data.strip())
        norm = ((max(min(analog_value, 550), 100) - 100.0)/450)
        print("norm",norm)
        hue_val = int(math.floor(norm*253) + 1)
        print("hue_val",hue_val)
        hue_bridge.set_light([5,6], 'bri', hue_val)
        hue = math.floor(random.random()*65535)
        hue_bridge.set_light([5], 'hue', hue)
        hue = math.floor(random.random()*65535)
        hue_bridge.set_light([6], 'hue', hue)
        # if analog_value < 100:
        # elif analog_value > 400:
        #     hue_bridge.set_light([5,6], 'bri', 254)
        # else:
        #     hue_bridge.set_light([5,6], 'bri', 100)


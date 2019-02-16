import serial
import csv
import time

ser = serial.Serial('COM3', 9600)

print('Wrting to file')
while True:
    with open('moistvals.txt', 'a') as csvfile:
        value = str(ser.readline()).strip("b'\\r\\n")
        print(value)
        csvfile.write(value + '\n')
    
    time.sleep(60*5)


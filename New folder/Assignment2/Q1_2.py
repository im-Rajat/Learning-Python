"""
Send message from arduino and print it on a computer using only python on the computer
"""

import serial

if __name__ == "__main__":
    Serial = serial.Serial('com3', 9600)
    print(Serial.readline())
    print("Enter 1 to ON LED and 0 to OFF LED : ")

    while 1:
        input_data = input()

        if input_data == '1':
            Serial.write(str.encode('1'))
            print("LED ON")

        if input_data == '0':
            Serial.write(str.encode('0'))
            print("LED OFF")

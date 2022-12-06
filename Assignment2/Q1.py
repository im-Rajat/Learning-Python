"""
Send message from arduino and print it on a computer using only python on the computer
"""

# First upload StandartFirmate program to ardrino which can be found in examples

import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

if __name__ == "__main__":
    while True:
        # board.digital[13].write(1)
        # time.sleep(1)
        # board.digital[13].write(0)
        # time.sleep(1)
        x = int(input("Enter 1 to On LED and Enter 0 to Off LED : "))
        if x == 1:
            board.digital[13].write(1)
        elif x == 0:
            board.digital[13].write(0)

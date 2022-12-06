"""
2. Read an mp3 file from a usb mass storage device with a particular label and play the audio file on powered speaker or headphone.
"""

from playsound import playsound

# playsound('C:\\Users\\rajatkumar\\Music\\timer.wav')
# playsound('E:timer.wav')

import win32api
from ctypes import windll


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    letter = ord('A')
    while bitmask > 0:
        if bitmask & 1:
            drives.append(chr(letter) + ':\\')
        bitmask >>= 1
        letter += 1

    return drives


if __name__ == '__main__':
    drives = get_drives()
    # print(drives)
    drive_names = {}

    for i in range(len(drives)):
        name = (win32api.GetVolumeInformation(drives[i]))
        drive_names[name[0]] = drives[i]

    print(drive_names)

    label = input("Enter Label : ")
    d = drive_names[label]
    d = d[:-1]
    file_name = input("Enter File Name : ")
    # file_name = "timer.wav"
    file_name = d + file_name
    print("This file is going to Play", file_name)
    try:
        playsound(file_name)
    except:
        print("File not Found")

import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # Select Default Camera

def make_1080p():
    cap.set(3, 1920)        # 3 is for Width
    cap.set(4, 1080)        # 4 is for Height

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
    ret, frame = cap.read()     # Capture every frame

    frame30 = rescale_frame(frame, percent=30)
    frame140 = rescale_frame(frame, percent=140)

    # cv2.imshow('frame', frame)  # Display the resulting frame (imgshow)
    cv2.imshow('frame30', frame30)
    cv2.imshow('frame140', frame140)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
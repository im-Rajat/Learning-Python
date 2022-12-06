import numpy as np
import cv2

cap = cv2.VideoCapture(0)       # Select Default Camera

while True:
    ret, frame = cap.read()     # Capture every frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)  # Display the resulting frame (imgshow)
    cv2.imshow('gray', gray)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

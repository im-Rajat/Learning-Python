# Reference : https://www.youtube.com/watch?v=WQeoO7MI0Bs

"""
Read (Images, Videos, Webcam)
"""
import cv2

# Read WebCam

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150) # Set Brightness
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# # Read Video
# import cv2
# frameWidth = 640
# frameHeight = 480
#
# cap = cv2.VideoCapture("timer.mp4")
#
# while True:
#     success, frame = cap.read()
#     # img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Video", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# # Read Image
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("R.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)
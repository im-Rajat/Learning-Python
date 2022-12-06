"""
Resizing and Cropping
"""

from cv2 import cv2
import numpy as np

img = cv2.imread("R.jpg")
print(img.shape)

imgResize = cv2.resize(img, (95, 100))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]


cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
"""
Uses cv2 Canny edge detection to get outline of key.
Outputs to an image file (out_gradient.png)
Authors: Lucas Donovan, John Larcinese
"""

import cv2
import os

# Input image 
input_img = "out_capture.png"
#input_img = "Reference_Key.png" # Reference image for testing

# Read in image and convert to greyscale
img = cv2.imread(input_img, 0)
img = cv2.rotate(img, cv2.ROTATE_180)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (7, 7), 0)

# Detect edges
edge = cv2.Canny(blur, 150, 255)

# Output image to file
#outpath = os.path.join(os.getcwd(), "out_gradient.png")
#cv2.imwrite(outpath, edge)

# Output image to screen
cv2.imshow('New image', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()










"""
This program is to be run with a specific key to store values and set values for the primary translator

Requirements: has lowest possible key depth, has highest possible key depth
 - User must enter the number of possible key depths to console
 - Teeth must be selected from left to right
 - User must only select each tooth once, attempting to center the selection at each tooth\
 - Press any key after selection is done to close the window

Storage file format:
1  int (count)     Output code size
2  int (pixels)    X value of first tooth
3  int (pixels)    X value of last tooth
4  int (pixels)    Shallowest cut / highest tooth
5  int (pixels)    Deepest cut / lowest tooth

Author: John Larcinese
"""

import cv2

values = [0] * 6
def start_values():
    global values
    values = [0] * 6

def check_point(x, y):
    global values

    if values[1] == 0:  # if no data stored, set first tooth
        values[1] = x

    if values[3] == 0:  # if no data stored, set deepest/shallowest to current
        values[3] = y
        values[4] = y

    values[0] += 1      # iterate tooth count
    values[2] = x       # set new last tooth

    for i in range(y+10, y-10, -1):     # finds lowest white pixel at cursor's X coord
        if keyImage[i, x].all(0):
            y = i
            break


    if y < values[3]:   # if y is smaller, set new shallowest cut
        values[3] = y
    if y > values[4]:   # if y is bigger, set new deepest cut
        values[4] = y

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        check_point(x, y)
        cv2.drawMarker(keyImage, (x, y), (255, 10, 10), 4, 10, 2)
        cv2.imshow("Key", keyImage)

# Opens image and storage files, displays image and starts click tracking
storage = open("value_storage.txt", "w")
keyImage = cv2.imread("out_gradient.png")
cv2.imshow("Key", keyImage)
cv2.setMouseCallback("Key", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writes all stored values to .txt file after selection is complete
for k in range(5):
    storage.write(str(values[k]) + "\n")
storage.close()


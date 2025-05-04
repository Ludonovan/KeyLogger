"""
Uses the values from the initialized key to measure the heights of key cuts.
Stores the values to an excel file as a packed integer and sends it to dropbox for use in GUI. 

Author: John Larcinese, Lucas Donovan
"""

import os
import cv2
import pandas
from upload_excel import append_key_data
from datetime import datetime

#os.system("rclone copy dropbox:shared-folder/data_storage.xlsx /home/cmpe499/key-logger/")

# Click tracker function for checking positions
#def click_event(event, x, y, flags, params):
#    if event == cv2.EVENT_LBUTTONDOWN:
#        print(x, ' ', y)

# Take in the image and create the window to display it
keyImage = cv2.imread("out_gradient.png")
#cv2.imshow("Key", keyImage)
#cv2.setMouseCallback("Key", click_event)

# Initialize variables from storage txt file
storage = open("value_storage.txt", "r")
keyCodeSize = int(storage.readline())        # Output code size
toothFirstXPos = int(storage.readline())     # X value of first tooth
toothLastXPos = int(storage.readline())      # X value of last tooth
toothShallowCut = int(storage.readline())    # Shallowest cut / highest tooth
toothDeepCut = int(storage.readline())       # Deepest cut / lowest tooth

toothDepthCount = 9                     # Must be set manually for each key set

keyCode = [0] * keyCodeSize
toothXStepSize = int((toothLastXPos - toothFirstXPos) / (keyCodeSize - 1))
keyCodeDivisor = (toothDeepCut - toothShallowCut) / toothDepthCount

for toothCount in range(0, keyCodeSize):
    toothXPos = toothFirstXPos + (toothCount * toothXStepSize)      # Iterates X search position
    for k in range(toothDeepCut, toothShallowCut, -1):              # Searches down for whitespace, shallowest cut is lowest value
    #for k in range(toothShallowCut, toothDeepCut):
        cv2.drawMarker(keyImage, (toothXPos + 10, k), (255, 10, 10), 4, 10, 2)
        if keyImage[k, toothXPos].all(0):                           # If whitespace, stores value and breaks
            cv2.drawMarker(keyImage, (toothXPos, k), (10, 10, 255), 4, 10, 2)
            #print("tooth: ", toothXPos, ' ', k)
            keyCode[toothCount] = int((k - toothDeepCut) / keyCodeDivisor) + 9
            break

#data = pandas.read_excel("data_storage.xlsx")       # Open Excel file
#df = pandas.DataFrame({str(keyCode)})               # Store KeyCode to dataframe

#print(data)

flattened = ""
for digit in keyCode:
    flattened += str(digit)
print(flattened)

# Used for uploading to dropbox. Must be uncommented to do so
'''
EXCEL_SHEET = "Key Scan Data"
EXCEL_TABLE = "Key_Scan_Data"
FILE_PATH = "/home/cmpe499/key-logger/data_storage.xlsx"

date_time = datetime.now()
formatted_date = date_time.strftime("%Y-%m-%d %H:%M:%S")
data = [formatted_date, "NEW", flattened]
append_key_data(EXCEL_TABLE, FILE_PATH, data, EXCEL_SHEET)

os.system("rclone copyto data_storage.xlsx dropbox:shared-folder/data_storage.xlsx")
'''

# Uncomment to save to an image rather than output to the screen
#outpath = os.path.join(os.getcwd(), "out_translator.png")
#cv2.imwrite(outpath, keyImage)

cv2.imshow("Key", keyImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

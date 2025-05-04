""" Uses a Picam2 to capture an image
Automatically runs gradient, initializer, and translator programs
Authors: Lucas Donovan, John Larcinese
"""

from picamera2 import Picamera2, Preview
import time
import os

# Initialize camera
picam2 = Picamera2() 

# Set camera settings
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (1920, 1080)}, display="lores")
picam2.configure(camera_config)

# Uncomment to see what the camera sees
#picam2.start_preview(Preview.QTGL1) 

# Start the camera
picam2.start()

# Set autofocus settings
picam2.set_controls({"AfMode": 0, "LensPosition": 15})

# Required for camera focus
time.sleep(1) 

# Capture image
picam2.capture_file("out_capture.png")

# Run gradient progam
os.system("python3 gradient.py")

# Run initializer if system is not initialized
with open("value_storage.txt", "r") as file_obj:
    first_char = file_obj.read(1)
    if not first_char:
        os.system("python3 initializer.py")

# Run translator program
os.system("python3 translator.py")

picam2.close()

# CMPE 499 Key Logger Project
This project was created for the Senior Design (Capstone) course at Shippensburg University. The goal of the project was to solve a societal problem. As two of the three members in the group were resident assistants, the focus on the project gravitated towards streamlining the current key auditing system. This project aims to digitize the key assignment and returns at the beginning and end of each semester by using computer vision to map the unique features of each key, specifically the key bittings, to the assigned student's name and contact information. This ensures that if a lost key is found, it can quickly and eaisly be returned to its assignee. 

## How to use this program

On Raspberry Pi:
Start server: python3 server.py
    - This is the http server used to communicate with the GUI. When the capture button is pressed on the web app GUI, it sends a request to the server, and it runs capture.py.
If not using GUI web app, run capture: python3 capture.py
    - This will automatically run the gradient, initializer (if the system is not initialized), and translation programs.
If using web app:
    - Click the capture button, the extracted values should display within a few seconds.

If not using Raspberry Pi:
    - ** If running on non-Pi hardware, the reference images in the repo can be used. The images stored are primarily from previous testing runs. The code should not have to be altered to take in different values. **
    - The gradient, initializer, and translator can be run in sequence to demonstrate the software without using the Raspberry Pi.
    - Ensure there is a clean picture to use for the gradient.
    - Run gradient program: python3 gradient.py
        - The output of this program is used for the translator.
    - The values in value_storage.txt should be accurate enough for a static image, so long as the image was taken from the device.
    - The initializer program *can* be ran, but it is strongly discouraged. The initializer is the heart of the translation software, as the translation software uses the values in the intializer to find the key bittings. The initializer **MUST** be run with a special key that has the highest and lowest bitting values. 
        - The initializer must be run with the key in the repo labeled "Reference_Key.png".
        - If the intializer is run, a window should pop up with the gradient of the key.
        - When the image appears, carefully click on each bitting (flat spots on cut of key), paying close attention to the first and last bittings, as well as the highest and lowest bittings. When all 7 bittings are clicked, press any button on your keyboard to save and exit. 
    - Once you have the gradient and the values from the initializer, you can run the translation software.
        - python3 translator.py
        - This will either output to the screen or to a .png file, depending on which lines are commented out in the translator program. 

## Python Files

### capture.py

Uses the hardware (rPi4B and picam3) to take a picture of a key. The image is stored, and the program then runs the gradient, initializer (if the system is uninitialized), and translator programs.


### gradient.py

Takes an input image and outputs an image file of the gradient of the input image.


### initializer.py

Takes in a gradient image and stores values denoted by user clicks to a txt file, which is used by translator.py for coordinate scanning. The key used for initialization must have both the highest and lowest bitting values. Once the reference key is initialized and the values are stored, the system does not need to be reinitialized. The user performing the initialization should pay close attention to the X values of the first and last cuts, and the Y values of the shallowest and deepest cuts. This program also creates the .xlsx file used for data storage.  


### translator.py

Uses the initialized variables in value_storage.txt to determine the depth of each cut on the input key. Outputs an int array denoting key bitting to the .xlxs file created in initializer.py, ensuring no duplicate keycodes are entered. 


### server.py

This is the server used for the GUI to communicate with the Raspberry Pi.


### upload_excel.py

This file contains functions used in the translation software for uploading the data directly to dropbox. 


## /KeyLogger Directory
This directory contains the Web App. 


## Areas of Improvement

There are a few issues that occurred during the testing phases of our project.
    - The capture program is very slow. This is for two main reasons:
        - The camera takes at least a full second to focus.
            - We opted to not use the autofocus, as that took even longer. Setting the focus manually still takes about a second, but we had some issues where it would take longer in some instances.
        - The gradient software is slow
            - Throughout the project we used two different types of edge detection, a morphological gradient and cv2.Canny. We decided that using cv2.Canny was a better option, as it gave a thinner line, and sometimes an image with less noise.
            - This time can be significantly lowered if we use C++ for the gradient instead of python. 


**Eye Blink Detection using OpenCV and Dlib**
=============================================
This project captures real-time video from a webcam and calculates the number of blinks using **Eye Aspect Ratio (EAR)**. The script leverages `OpenCV` for video processing and face detection, `Dlib` for facial landmarks detection, and `SciPy` for calculating distances to measure the blink threshold.

* * * * *

**Table of Contents**
---------------------

1.  [Requirements](#requirements)
2.  [Description](#description)
3.  [Installation](#installation)
4.  [How It Works](#how-it-works)
    -   [Eye Aspect Ratio (EAR)](#eye-aspect-ratio-ear)
    -   [Landmarks](#landmarks)
5.  [Code Structure](#code-structure)
6.  [Usage](#usage)
7.  [Output](#output)

* * * * *

**Requirements**
----------------

To run this project, you'll need the following libraries:

-   `OpenCV`
-   `Dlib`
-   `Imutils`
-   `Scipy`
-   `Matplotlib`

Additionally, you'll need a **facial landmark model**:

-   `shape_predictor_68_face_landmarks.dat`

* * * * *

**Description**
---------------

This script detects eye blinks in real-time by capturing video from a webcam and analyzing eye movements. The script calculates the **Eye Aspect Ratio (EAR)** for both eyes and detects a blink if the EAR falls below a certain threshold.

### **Key Features:**

-   Real-time blink detection using webcam or from Video.
-   Displays the current FPS (frames per second) on the video feed.
-   Counts the number of blinks and displays it live.

* * * * *

**Installation**
----------------

1.  Install the required Python libraries:

    `pip install opencv-python dlib imutils scipy matplotlib`

* * * * *

**How It Works**
----------------

### **Eye Aspect Ratio (EAR)**

The **EAR** is calculated to determine whether a person is blinking. The formula for EAR is as follows:

![](data:image/png;base64,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)

Where:

-   P1 to 𝑃6 represent the landmarks around the eye.

The EAR remains constant when the eyes are open but drops when a blink occurs.

### **Landmarks**

The script uses the **68-point facial landmark model** to detect key points around the eyes:

-   Left Eye: Landmarks 36 to 41
-   Right Eye: Landmarks 42 to 47

If the average EAR falls below the set threshold (`0.5` in this case), the script detects a blink.

* * * * *

**Code Structure**
------------------

### **Imports:**
import cv2 

import dlib

import time

from imutils import face_utils

from scipy.spatial import distance as dist

import matplotlib.pyplot as plt`

### **Webcam Capture Or Video Input:**

`cam = cv2.VideoCapture(0)  # Opens the webcam for real-time video capture`

`cam = cv2.VideoCapture('your-video-location.mp4') # Passing video as input.`


### **Eye Blink Detection Logic:**

-   Set the EAR threshold:

    `blink_thresh = 0.5  # Threshold for detecting a blink`

    `tt_frame = 3  # Number of frames to confirm a blink`

-   Detect landmarks using Dlib's frontal face detector:

    `detector = dlib.get_frontal_face_detector()
    lm_model = dlib.shape_predictor('Model/shape_predictor_68_face_landmarks.dat')`

-   Calculate the EAR:


def EAR_cal(eye):

        v1 = dist.euclidean(eye[1], eye[5])

        v2 = dist.euclidean(eye[2], eye[4])

        h1 = dist.euclidean(eye[0], eye[3])

        ear = (v1 + v2) / h1

        return ear

### **FPS Calculation:**

`ptime = time.time()
fps = 1 / (time.time() - ptime)  # Calculate frames per second`

### **Blink Detection and Visualization:**

-   Check the EAR for each eye and calculate the average EAR.
-   If the EAR falls below the threshold for a certain number of frames, a blink is counted.

### **Display:**

-   The script draws rectangles around detected faces and circles on eye landmarks.
-   It displays FPS and the blink count on the video feed.

### **Breaking the Loop:**

`if cv2.waitKey(1) & 0xFF == ord('q'):
    break  # Press 'q' to exit the video feed`

* * * * *

**Usage**
---------

1.  Ensure your webcam is connected.
2.  Run the script:

    `python basic.py` #for video as input
    
    `python new.py` #for camera as input

3.  The video feed from your webcam will appear in a new window with FPS and blink count displayed.

### **Customization:**

-   **Blink Threshold:** Adjust the `blink_thresh` variable to make the blink detection more or less sensitive.
-   **Frame Count Threshold:** Change the `tt_frame` variable to modify how many consecutive frames are required to detect a blink.

* * * * *

**Output**
----------

-   **Live Video Feed**: The webcam feed will display the following information:
    -   **FPS**: Frames per second on the top-left corner.
    -   **Blink Count**: The total number of blinks detected on the top-left corner.
    -   **Facial and Eye Landmarks**: A rectangle around the face and circles around eye landmarks to show the detection in action.

* * * * *


**License**
-----------

This project is licensed under the MIT License. See the LICENSE file for more information.

* * * * *

### **Contact**

For any inquiries or issues, feel free to open an issue or contact the project contributor.
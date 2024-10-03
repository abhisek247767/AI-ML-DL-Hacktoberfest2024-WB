import cv2 as cv # pip install pycaw library is used for 
import mediapipe as mp
import numpy as np
import time
import os

# Disable oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initialize video capture
capture = cv.VideoCapture(0)

# Initialize MediaPipe Hands and Drawing utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(False)
mpdraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

if not capture.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("End of video or error reading frame.")
        break

    # Convert the frame to RGB
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Process the frame and extract hand landmarks
    results = hands.process(frameRGB)

    # If landmarks are found, draw them on the frame
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark): #id = index number of finger and lm is landmark
               #print(id,lm)
               h, w, c= frame.shape
               cx, cy = int(lm.x*w), int(lm.y*h) #position and we do this to get the pixel value 
               print(id, cx, cy)
               if id == 4:
                   cv.circle(frame,(cx,cy),15,(255,8,255),cv.FILLED)
            mpdraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)
    
    

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv.putText(frame, str(int(fps)),(18,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),2)

    # Display the frame
    cv.imshow('Video', frame)

    # Exit the loop when 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv.destroyAllWindows()

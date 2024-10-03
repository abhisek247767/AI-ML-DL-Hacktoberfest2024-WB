import cv2 as cv
import numpy as np
import pyautogui
import time
import mediapipe as mp
import os
import handtrackingmodule as htm

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Create a folder for screenshots
screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

wCam, hCam = 648, 488
capture = cv.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)

detector = htm.handDetector(detectCon=0.7)


def recognize_gesture(lmList):
    if len(lmList) == 21:
        thumb_tip = lmList[4][2]
        index_tip = lmList[8][2]
        middle_tip = lmList[12][2]
        ring_tip = lmList[16][2]
        pinky_tip = lmList[20][2]

        thumb_mcp = lmList[2][2]
        index_dip = lmList[7][2]
        middle_dip = lmList[11][2]
        ring_dip = lmList[15][2]
        pinky_dip = lmList[19][2]

        if (thumb_tip < thumb_mcp and
                index_tip < index_dip and
                middle_tip < middle_dip and
                ring_tip < ring_dip and
                pinky_tip < pinky_dip):
            return True
    return False


gesture_detected = False
pause_duration = 10
pause_start_time = 0
screenshot_counter = 1  # Counter to save screenshots with unique names

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)

    if recognize_gesture(lmList) and not gesture_detected:
        gesture_detected = True
        pause_start_time = time.time()

        # Display the message "Ready to take screenshot"
        cv.putText(frame, "Ready to take screenshot", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1,
                   (0, 255, 0), 2)
        cv.imshow('Video', frame)

        # Wait a moment to give visual feedback
        cv.waitKey(1000)  # Pause for 1 second

        # Take and save the screenshot
        screenshot = pyautogui.screenshot()
        screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)

        # Generate a unique filename for each screenshot
        screenshot_filename = f"screenshot_{screenshot_counter}.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_filename)

        # Save the screenshot in the folder
        cv.imwrite(screenshot_path, screenshot)

        # Display message that the screenshot has been saved
        cv.putText(frame, "Screenshot saved!", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1,
                   (0, 255, 255), 2)

        # Increment the counter for the next screenshot
        screenshot_counter += 1

    if gesture_detected:
        current_time = time.time()
        elapsed_time = current_time - pause_start_time

        # During the waiting period, display "Wait for some time"
        if elapsed_time < pause_duration:
            cv.putText(frame, "Wait for some time...", (50, 150), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 255), 2)
        else:
            gesture_detected = False

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

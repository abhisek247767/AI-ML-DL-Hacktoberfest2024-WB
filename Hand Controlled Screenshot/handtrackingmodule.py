import cv2 as cv
import mediapipe as mp
import time
import os

# Disable oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectCon=0.5, trackCon=0.5):
        """
        Initialize the hand detector with the given parameters.
        :param mode: Whether to treat the input images as a video stream.
        :param maxHands: Maximum number of hands to detect.
        :param detectCon: Minimum detection confidence.
        :param trackCon: Minimum tracking confidence.
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectCon = detectCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        # Corrected instantiation of Hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                                        max_num_hands=self.maxHands, 
                                        min_detection_confidence=self.detectCon, 
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        """
        Process the frame to find hands and optionally draw the landmarks.
        :param frame: The input frame from the video feed.
        :param draw: Whether to draw hand landmarks on the frame.
        :return: The processed frame with or without drawn landmarks.
        """
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert the frame to RGB
        self.results = self.hands.process(frameRGB)  # Process the frame to detect hands

        # If landmarks are found, optionally draw them on the frame
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)
        return frame

    def findPosition(self, frame, handNo=0, draw=True):
        """
        Find the position of hand landmarks and optionally draw a specific landmark.
        :param frame: The input frame from the video feed.
        :param handNo: The hand number to detect (default is the first hand).
        :param draw: Whether to draw a circle on the specified landmark.
        :return: List of landmark positions.
        """
        lmList = []  # List to store landmark positions

        # If landmarks are found, extract their positions
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # Convert normalized coordinates to pixel values
                lmList.append([id, cx, cy])
                if draw and id == 4:  # Draw a circle on the thumb tip (landmark with id 4)
                    cv.circle(frame, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        return lmList

def main():
    pTime = 0  # Previous time for FPS calculation
    cTime = 0  # Current time for FPS calculation
    capture = cv.VideoCapture(0)  # Initialize video capture

    # Create an instance of handDetector
    detector = handDetector()

    if not capture.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        isTrue, frame = capture.read()  # Read a frame from the video capture
        if not isTrue:
            print("End of video or error reading frame.")
            break

        frame = detector.findHands(frame)  # Detect hands and draw landmarks
        lmList = detector.findPosition(frame)  # Get positions of hand landmarks
        if lmList:
            print(lmList[4])  # Print the position of the thumb tip

        # Calculate FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display FPS on the frame
        cv.putText(frame, f'FPS: {int(fps)}', (18, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 2)

        # Display the processed frame
        cv.imshow('Video', frame)

        # Exit the loop when 'd' key is pressed
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()  # Release the video capture object
    cv.destroyAllWindows()  # Close all OpenCV windows

# Entry point of the script
if __name__ == "__main__":
    main()

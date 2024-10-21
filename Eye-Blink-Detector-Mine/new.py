import cv2
import dlib
import time
from imutils import face_utils
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt



#This code is for capturing realtime videos and calculating eyeblink. 
#The code is same as the basic.py but with the addition of capturing the video from the webcam
cam = cv2.VideoCapture(0)


#------------Variables---------#
blink_thresh=0.5
tt_frame = 3
blink_count = 0
count=0
avg_values = []

#------#
detector = dlib.get_frontal_face_detector()
lm_model = dlib.shape_predictor('Eye-Blink-Detector-Mine\Model\shape_predictor_68_face_landmarks.dat')

#--Eye ids ---#
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
print(L_start,L_end)
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

ptime = 0

def EAR_cal(eye):
    #----verticle-#
    v1 = dist.euclidean(eye[1],eye[5])
    v2 = dist.euclidean(eye[2],eye[4])

    #-------horizontal----#
    h1 = dist.euclidean(eye[0],eye[3])

    ear = (v1+v2)/h1
    return ear



while 1 :

    if cam.get(cv2.CAP_PROP_POS_FRAMES) == cam.get(cv2.CAP_PROP_FRAME_COUNT) :
        cam.set(cv2.CAP_PROP_POS_FRAMES,0)

    _,frame = cam.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #--------fps --------#
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime= ctime
    cv2.putText(
        frame,
        f'FPS:{int(fps)}',
        (50,50),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (0,0,100),
        1
    )
    #-----facedetection----#
    faces = detector(img_gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2= face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(200),2)

        #---------Landmarks------#
        shapes = lm_model(img_gray,face)
        shape = face_utils.shape_to_np(shapes)

        #-----Eye landmarks---#
        lefteye = shape[L_start:L_end]
        righteye = shape[R_start:R_end]

        for Lpt,rpt in zip(lefteye,righteye):
            cv2.circle(frame,Lpt,2,(200,200,0),2)
            cv2.circle(frame, rpt, 2, (200, 200, 0), 2)

        left_EAR = EAR_cal(lefteye)
        right_EAR= EAR_cal(righteye)

        avg =( left_EAR+right_EAR)/2
        print(avg)
        avg_values.append(avg)
        if avg<blink_thresh :
            count+=1

        else :
            if count>tt_frame:
                # cv2.putText(frame,f'BLINK Detected',(frame.shape[1]//2 - 300,frame.shape[0]//2),cv2.FONT_HERSHEY_SIMPLEX,2,(0,200,0),2)
                blink_count+=1
                count=0
            else :
                count=0
    cv2.putText(frame,f'Blink Count: {blink_count}',(50,100),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,100),1)
    frame = cv2.resize(frame,(1080,640))

    cv2.imshow("Video" ,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()


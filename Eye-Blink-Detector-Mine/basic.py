#Importing the required dependencies
import cv2                                     #for video rendering
import dlib                                    #for face and landmark detection
import imutils
from scipy.spatial import distance as dist     #for calculating dist b/w the eye landmarks
from imutils import face_utils                 #to get the landmark ids of the left and right eyes ----you can do this manually too


#This code is for calculating the eye blink from a video 

cam = cv2.VideoCapture('assets/Video.mp4')

#------defining a function to calulate the EAR-----------#
def calculate_EAR(eye) :
    #---calculate the verticle distances---#
    y1 = dist.euclidean(eye[1] , eye[5])
    y2 = dist.euclidean(eye[2] , eye[4])

    #----calculate the horizontal distance---#
    x1 = dist.euclidean(eye[0],eye[3])

    #----------calculate the EAR--------#
    EAR = (y1+y2) / x1
    return EAR

#---------Mark the eye landmarks-------#
def mark_eyeLandmark(img , eyes):
    for eye in eyes:
        pt1,pt2 = (eye[1] , eye[5])
        pt3,pt4 = (eye[0],eye[3])
        cv2.line(img,pt1,pt2,(200,00,0),2)
        cv2.line(img, pt3, pt4, (200, 0, 0), 2)
    return img

#---------Variables-------#
blink_thresh = 0.5
succ_frame = 2
count_frame = 0

#-------Eye landmarks------#
(L_start, L_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(R_start, R_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

#------Initializing the Models for Landmark and face Detection---------#
detector = dlib.get_frontal_face_detector()
landmark_predict = dlib.shape_predictor('Eye-Blink-Detector-Mine\Model\shape_predictor_68_face_landmarks.dat')


while 1 :

    #------If the video ends Reset it to start-----#
    if cam.get(cv2.CAP_PROP_POS_FRAMES) == cam.get(cv2.CAP_PROP_FRAME_COUNT) :
        cam.set(cv2.CAP_PROP_POS_FRAMES, 0)

    #-------Reading the frame from the video--------#
    _,frame = cam.read()
    frame = imutils.resize(frame,width=640)
    #---converting frame to gray scale to pass to detector----#
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #---detecting the faces---#
    faces = detector(img_gray)
    for face in faces :
        #----landmark detection-----#
        shape = landmark_predict(img_gray,face)
        #----converting the shape class directly to a list of (x,y) cordinates-----#
        shape = face_utils.shape_to_np(shape)
        for lm in shape:
            cv2.circle(frame,(lm),3,(10,2,200))
        #----parsing the landmarks list to extract lefteye and righteye landmarks--#
        lefteye = shape[L_start : L_end]
        righteye = shape[R_start:R_end]

        #-----Calculate the EAR---#
        left_EAR = calculate_EAR(lefteye)
        right_EAR = calculate_EAR(righteye)
        img = frame.copy()
        #----mark the landmarks----#
        img = mark_eyeLandmark(img,[lefteye,righteye])

        #-----Avg of left and right eye EAR----#
        avg = (left_EAR+right_EAR)/2
        if avg<blink_thresh :
            count_frame+=1
        else:
            if count_frame >= succ_frame :
                cv2.putText(img, 'Blink Detected',(30,30) , cv2.FONT_HERSHEY_DUPLEX , 1,(0,200,0),1)
            else:
                count_frame=0

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cam.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import os
import time
import posemodule as pm
import math

def crunches(frame_window,img):
    pTime = 0
    path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'crunches 1.mp4'
    detector = pm.poseDetector()

    #up3 y500
    # down 1000
    # up15 1100
    #  down 1100
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


    count = 0
    calories = 0
    f=0
    time.sleep(5)
   
    img = detector.findPose(img)
    lmlist = detector.getPosition(img)
        #print(lmlist[3])
        
    if len(lmlist)!=0:
            #cv2.circle(img,(lmlist[15][1],lmlist[15][2]),10,(0,0,255),cv2.FILLED)
            #cv2.circle(img,(lmlist[3][1],lmlist[3][2]),10,(0,0,255),cv2.FILLED) 
        x1 = lmlist[0][1]
        x2 = lmlist[12][1]
            
        length = x1-x2
        if length>=0 and f==0:
            f=1
        elif length<0 and f==1:
            f=0
            count=1

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
            #cv2.putText(img,"Total Number of Crunches  "+str(int(count)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
            #(60,100,255),3)
            #cv2.putText(img,"Calories Burnt  "+str(int(count)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
            #(60,100,255),3)
        img = cv2.resize(img, (600,600))                    # Resize image
            
            
        calories = 0.15*count
        
        
        
    return frame_window.image(img, channels='BGR'),count,calories


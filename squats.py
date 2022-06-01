import cv2
import mediapipe as mp
import os
import time
import posemodule as pm
import math
import streamlit as st

def squats(FRAME_WINDOW,img):
    pTime = 0
    cap = cv2.VideoCapture(0)
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
    
    img = detector.findPose(img)
    lmlist = detector.getPosition(img,draw=False)
        
        # if u want all dots then put draw= true and comment out the cv2.circle part in the if part below
        
    if len(lmlist)!=0:
            #cv2.circle(img,(lmlist[25][1],lmlist[25][2]),10,(0,0,255),cv2.FILLED)
            #cv2.circle(img,(lmlist[23][1],lmlist[23][2]),10,(0,0,255),cv2.FILLED) 
            #print(lmlist[23])
        y1 = lmlist[25][2]
        y2 = lmlist[23][2]
            
        length = y2-y1
        if length>=0 and f==0:
            f=1
        elif length<-50 and f==1:
            f=0
            count=1



        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
            #cv2.putText(img,"Total Number of Squats  "+str(int(count)),(70,50),cv2.FONT_HERSHEY_DUPLEX,1,
            #(60,100,255),3)
            #cv2.putText(img,"Calories Burnt  "+str(int(count)*0.32),(70,150),cv2.FONT_HERSHEY_DUPLEX,1,
            #(60,100,255),3)
            #img = cv2.resize(img, (900,900))                    # Resize image
            
        calories = 0.32*count
        
    return FRAME_WINDOW.image(img, channels='BGR'), count,calories


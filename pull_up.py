from fractions import Fraction
import imp
import cv2
import mediapipe as mp
import streamlit as st
import os
import time
import posemodule as pm
import math


def pullup(frame_window,img):
    pTime = 0
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
        #print(lmlist[3])
        
    if len(lmlist)!=0:
            #cv2.circle(img,(lmlist[15][1],lmlist[15][2]),10,(0,0,255),cv2.FILLED)
            #cv2.circle(img,(lmlist[3][1],lmlist[3][2]),10,(0,0,255),cv2.FILLED) 
        y1 = lmlist[3][2]
        y2 = lmlist[20][2]
            
        length = y2-y1
        if length>=0 and f==0:
            f=1
        elif length<0 and f==1:
            f=0
            count = 1
            

            #print(length)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
            #cv2.putText(img,"Total Number of Pullups  "+str(int(count)),(70,250),cv2.FONT_HERSHEY_DUPLEX,3,
            #(60,100,255),3)
            #cv2.putText(img,"Calories Burnt  "+str(int(count)*1),(70,350),cv2.FONT_HERSHEY_DUPLEX,3,
            #(60,100,255),3)
        img = cv2.resize(img, (600,600))                    # Resize image

            
        calories = 1*count
    return frame_window.image(img, channels='BGR'),count,calories

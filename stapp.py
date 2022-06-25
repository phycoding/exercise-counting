

import streamlit as st 
import cv2
import mediapipe as mp
import PoseModule1 as pm
import numpy as np
import time
import math
import os
dir = 0

pTime = 0

detector = pm.poseDetector()
squat_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'squats3.mp4'
pushup_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'pushup2.mp4'
biceps_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'weight lifting 1.mp4'

st.set_page_config(
    page_title="Care-o-Diabetic",
    page_icon="🩺"
)
st.title("Your Personal Trainer 🩺")
FRAME_WINDOW = st.image([], width = 300,channels='BGR')
SIDE_WINDOW = st.sidebar.image([], width=100, channels='BGR')
st.sidebar.title("Please tick the exercise video you want to watch")
check_box = st.sidebar.checkbox("Show Video", False)
if check_box == True:
    st.sidebar.subheader("Select your workout video")
    video = st.sidebar.selectbox("Squats", ["Squats", "Pushups", "Pullups", "Biceps"])
    if video == "Squats":
        st.video(squat_path)
    if video == "Pushups":
        st.video(pushup_path)
    if video == "Biceps":
        st.video(biceps_path)
    st.warning("Please UNTICK the checkbox before starting the exercise")
status_text = st.empty()
place_holder = st.empty()

count = 0
calories = 0
pTime = 0
dir = 0
color = (255, 0, 255)


exercise_list =  ["Pushup", "Squat","Curl"]
exercise = st.sidebar.selectbox("Select Your Exercise", exercise_list)

def img_fun(img):
    #img = cv2.resize(img, (1280, 720))
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    return img, lmList

def exercise_counts(img,per,bar):
        global count, calories, pTime,color,dir
        img = cv2.resize(img, (1280, 720))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        if len(lmList) != 0:
            color = (255, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw Curl Count
        #cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        #cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    #(255, 0, 0), 25)
        cTime = time.time()
        #fps = 1 / (cTime - pTime)
        #pTime = cTime
        #cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                #(255, 0, 0), 5)
        return img, count



#Live Dashboard
# create three columns
placeholder = st.empty()
def dashboard(count,calories,label1,label2):
    with placeholder:
        st.container():
                kpi1, kpi2 = st.columns(2)
            # fill in those three columns with respective metrics or KPIs
                kpi1.metric(
                    label=label1,
                    value=round(count, 2),
                    delta=round(count)+1,
                    )

                kpi2.metric(
                    label=label2,
                    value=int(calories),
                    delta= calories,
                    )

if st.button('Exercise'):
    if exercise == "Pushup":
        cap = cv2.VideoCapture(pushup_path)
        while True:
         _, img = cap.read()
         
        # Right Arm
         img1,lmList = img_fun(img)
         angle = detector.findAngle(img1, 12, 14, 16)
            # # Left Arm
         angle = detector.findAngle(img1, 11, 13, 15)

            # print(angle, per)
            # legs
         angle = detector.findAngle(img1, 24, 26, 28)
         angle = detector.findAngle(img1, 23, 25, 27)

            # # Left Arm
         angle = detector.findAngle(img1, 11, 13, 15)
         per = np.interp(angle, (60, 130), (0, 100))
         bar = np.interp(angle, (60, 130), (650, 100))
         img, pushup_count = exercise_counts(img, per, bar)
         FRAME_WINDOW.image(img)
         dashboard(pushup_count,calories,"Pushup Count","Calories Burned")
         
    if exercise == "Squat":
      cap = cv2.VideoCapture(squat_path)
      while True:
        _, img = cap.read()
        img1,lmList = img_fun(img)
        angle = detector.findAngle(img1, 12, 24, 28)
        per = np.interp(angle, (100, 170), (0, 100))
        bar = np.interp(angle, (100, 170), (650, 100))
        img, squat_count = exercise_counts(img, per, bar)
        FRAME_WINDOW.image(img)
        dashboard(squat_count,calories,"Squat Count","Calories Burned")

    if exercise == "Curl":
        cap = cv2.VideoCapture(biceps_path)
        while True:
            img = cap.read()[1]
            img1,lmList = img_fun(img)
            
            # Right Arm
            angle = detector.findAngle(img1, 12, 14, 16)
            # # Left Arm
            angle = detector.findAngle(img1, 11, 13, 15)
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            img, curl_count = exercise_counts(img, per, bar)
            FRAME_WINDOW.image(img)
            dashboard(curl_count,calories,"Curl Count","Calories Burned")
#status_text.title("Calories Burned %s" %calories)
#status_text.title("No of Pullups %s" %pullup_count)


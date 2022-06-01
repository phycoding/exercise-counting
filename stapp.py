from turtle import width
from push_up import pushup
from pull_up import pullup
from squats import squats
from weight_lifting import biceps
import streamlit as st 
import cv2
import mediapipe as mp
import posemodule as pm
import time
import math
import os


squat_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'squats3.mp4'
pushup_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'pushup1.mp4'
pullup_path = os.path.dirname(os.path.realpath(__file__))+'/videos/'+'pullup1.mp4'
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
    if video == "Pullups":
        st.video(pullup_path)
    if video == "Biceps":
        st.video(biceps_path)
    st.warning("Please UNTICK the checkbox before starting the exercise")
status_text = st.empty()
place_holder = st.empty()

calories = 0
pullup_counts = 0
pullup_calories = 0
pushup_counts = 0
pushup_calories = 0
weightlift_counts = 0
weightlift_calories = 0
squat_counts = 0
squat_calories = 0

#video capturing
cap = cv2.VideoCapture(0)
exercise = st.sidebar.selectbox("Select Your Exercise", ["Pullup", "Pushup", "Squat","Weight Lifting"])

#Live Dashboard
# create three columns
placeholder = st.empty()

if st.button('Exercise'):
    if exercise == "Pullup":
        while True:
            img = cap.read()[1]
            pullup_img, pullup_count, pullup_calorie = pullup(FRAME_WINDOW,img)
            pullup_counts = pullup_counts + pullup_count
            pullup_calories = pullup_calories+pullup_calorie
            calories = calories + pullup_calories

            with placeholder.container():
                kpi1, kpi2 = st.columns(2)
            # fill in those three columns with respective metrics or KPIs
                kpi1.metric(
                    label="Pullups",
                    value=round(pullup_counts, 2),
                    delta=round(pullup_counts)+1,
                    )

                kpi2.metric(
                    label="Pullups Calories",
                    value=int(pullup_calories),
                    delta= pullup_calories,
                    )
            status_text.title("Calories Burned %s" %calories)
    if exercise == "Pushup":
        pushup_calorie,pushup_count = pushup(FRAME_WINDOW,status_text)
        pushup_counts = pushup_counts + pushup_count
        pushup_calories = pushup_calories + pushup_calorie
        calories = calories + pushup_calories
        with placeholder.container():
                kpi1, kpi2 = st.columns(2)
            # fill in those three columns with respective metrics or KPIs
                kpi1.metric(
                    label="Pushups",
                    value=round(pushup_counts, 2),
                    delta=round(pushup_counts)+1,
                    )

                kpi2.metric(
                    label="Pullups Calories",
                    value=int(pushup_calories),
                    delta= pullup_calories,
                    )
        status_text.title("Calories Burned %s" %calories)
        
    if exercise == "Squat":
        squat_calorie,squat_count = squats(1000, FRAME_WINDOW,status_text)
        squat_counts = squat_counts + squat_count
        squat_calories = squat_calories + squat_calorie
        calories = calories + squat_calories
        with placeholder.container():
                kpi1, kpi2 = st.columns(2)
            # fill in those three columns with respective metrics or KPIs
                kpi1.metric(
                    label="Squats",
                    value=round(squat_counts, 2),
                    delta=round(squat_counts)+1,
                    )

                kpi2.metric(
                    label="Squats Calories",
                    value=int(squat_calories),
                    delta= squat_calories,
                    )
        status_text.title("Calories Burned %s" %calories)

    if exercise == "Weight Lifting":
        weightlift_calorie,weightlift_count = biceps(1000, FRAME_WINDOW,status_text)
        weightlift_counts = weightlift_counts + weightlift_count
        weightlift_calories = weightlift_calories + weightlift_calorie
        calories = calories+weightlift_calories
        with placeholder.container():
                kpi1, kpi2 = st.columns(2)
            # fill in those three columns with respective metrics or KPIs
                kpi1.metric(
                    label="Weight Lifting",
                    value=round(weightlift_counts, 2),
                    delta=round(weightlift_counts)+1,
                    )

                kpi2.metric(
                    label="Weight Lifting Calories",
                    value=int(weightlift_calories))
        status_text.title("Calories Burned %s" %calories)
        
#status_text.title("Calories Burned %s" %calories)
#status_text.title("No of Pullups %s" %pullup_count)


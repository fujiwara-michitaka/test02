import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

# MediaPipe Pose instance
mp_pose = mp.solutions.pose

# Streamlit page layout
st.set_page_config(
    page_title="Pose Detection with Streamlit",
    layout="wide",
)

# Title and description
st.title("Pose Detection with Streamlit")
st.write("This is an example of Pose Detection using MediaPipe in Streamlit.")

# Initialize MediaPipe Pose
pose = mp_pose.Pose()

# Video capture
cap = cv2.VideoCapture(0)

# Set video width and height
cap.set(3, 640)
cap.set(4, 480)

stframe = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        # Draw pose landmarks on the frame
        mp.drawing_utils.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )

    # Display the frame with landmarks using st.image
    stframe.image(frame, channels="BGR")

cap.release()

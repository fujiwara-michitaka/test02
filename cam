import streamlit as st
import cv2
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def main():
    st.title("Hand Distance App")
    
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            _, frame = cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(frame)
            
            if results.pose_landmarks:
                left_wrist = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST]
                right_wrist = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST]
                
                if left_wrist and right_wrist:
                    # Calculate the distance between left and right wrists
                    distance = ((right_wrist.x - left_wrist.x) ** 2 + (right_wrist.y - left_wrist.y) ** 2) ** 0.5
                    st.write("Distance between wrists:", distance)
                    
                    # Draw circles based on the distance
                    num_circles = int(distance * 10)
                    for _ in range(num_circles):
                        cv2.circle(frame, (int(right_wrist.x * frame.shape[1]), int(right_wrist.y * frame.shape[0])), 5, (0, 255, 0), -1)
                
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            st.image(frame, channels="BGR", use_column_width=True)
                
if __name__ == "__main__":
    main()

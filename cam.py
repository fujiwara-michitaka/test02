import streamlit as st
import cv2
import mediapipe as mp

# Mediapipeを使って姿勢と手首の位置を検出するためのライブラリのインポート
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def main():
    # Streamlitアプリケーションのタイトルを設定
    st.title("Hand Distance App")
    
    # カメラを初期化
    cap = cv2.VideoCapture(0)
    
    # Mediapipeを使って姿勢検出のためのモデルを初期化
    holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    
    while True:
        # Streamlitウィジェットを使用してカメラフレームを表示
        frame = st.image([])
        
        # カメラからフレームを取得
        _, frame_data = cap.read()
        
        # OpenCVのカラースペースからRGBに変換
        frame_data = cv2.cvtColor(frame_data, cv2.COLOR_BGR2RGB)
        
        # Mediapipeを使って姿勢と手首の位置を検出
        results = holistic.process(frame_data)
        
        if results.pose_landmarks:
            # 左手首と右手首の位置を取得
            left_wrist = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_WRIST]
            right_wrist = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_WRIST]
            
            if left_wrist and right_wrist:
                # 左手首と右手首の距離を計算
                distance = ((right_wrist.x - left_wrist.x) ** 2 + (right_wrist.y - left_wrist.y) ** 2) ** 0.5
                
                # 距離を表示
                st.write("Distance between wrists:", distance)
                
                # 距離に応じて円を描画
                num_circles = int(distance * 10)
                for _ in range(num_circles):
                    # 右手首の位置に円を描画
                    cv2.circle(frame_data, (int(right_wrist.x * frame_data.shape[1]), int(right_wrist.y * frame_data.shape[0]), 5, (0, 255, 0), -1))

        # OpenCVのBGRカラースペースに戻す
        frame_data = cv2.cvtColor(frame_data, cv2.COLOR_RGB2BGR)

        # Streamlitウィジェットに新しいフレームを設定
        frame.image(frame_data, channels="BGR")
                
if __name__ == "__main__":
    main()


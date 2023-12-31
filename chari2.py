import streamlit as st
import random

# Streamlitアプリのタイトルを設定
st.title("アラームシステム")

# 15m以内に人がいるかの情報をカメラで取得
def check_for_person():
    # 仮の実装としてランダムに人がいるかどうかをシミュレート
    return random.choice([True, False])

# 時速を速度センサーから入力
def get_speed_from_sensor():
    # 仮の実装としてランダムな速度を生成
    return random.uniform(0, 15)

# 画像処理AIのAPIを利用してアラームのレベルを判定
def detect_alarm_level():
    if check_for_person():
        speed = get_speed_from_sensor()
        if speed >= 10:
            return 3
        elif 5 <= speed < 10:
            return 2
        else:
            return 1
    else:
        return 0

# アラームのレベルを判定
alarm_level = detect_alarm_level()

# Streamlitアプリ内でアラームを表示
st.write(f"アラームレベル: {alarm_level}")
if alarm_level > 0:
    if alarm_level == 3:
        st.write("レベル3のアラームを鳴らす（音量：高音）")
        # スピーカーから高音を出力するコードを追加
    elif alarm_level == 2:
        st.write("レベル2のアラームを鳴らす（音量：中音）")
        # スピーカーから中音を出力するコードを追加
    elif alarm_level == 1:
        st.write("レベル1のアラームを鳴らす（音量：低音）")
        # スピーカーから低音を出力するコードを追加
else:
    st.write("アラームは鳴りません")

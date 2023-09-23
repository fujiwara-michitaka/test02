import streamlit as st
import random

# 西暦年と対応する出来事のデータ
years_to_events = {
    1492: "コロンブスがアメリカを発見",
    1776: "アメリカ独立宣言",
    1969: "アポロ11号の月面着陸",
    2000: "新千年紀の到来",
    2020: "新型コロナウイルスの世界的な流行",
}

# クイズのカウンターを初期化
quiz_count = 0
correct_answers = 0
max_quiz_count = 5  # クイズの最大数

# アプリのタイトル
st.title("クイズアプリ")

# 5つのクイズを表示
while quiz_count < max_quiz_count:
    st.sidebar.markdown(f"問題 {quiz_count + 1}")
    
    # ランダムな年と対応する出来事を選択
    random_year = random.choice(list(years_to_events.keys()))
    event = years_to_events[random_year]
    
    st.write(f"問題 {quiz_count + 1}: {event}")

    # ユーザーの回答を取得
    user_answer = st.radio("正しいかどうかを選んでください", options=["〇", "×"])

    # 正誤を判定
    if random_year in years_to_events and user_answer == "〇":
        st.success("正解！")
        correct_answers += 1
    elif random_year not in years_to_events and user_answer == "×":
        st.success("正解！")
        correct_answers += 1
    else:
        st.error("不正解。")

    # 次の問題へ進むかどうかを確認
    quiz_count += 1
    if quiz_count < max_quiz_count:
        next_question = st.button("次の問題へ進む")
        if not next_question:
            break

# 最終的な結果を表示
st.title("クイズ結果")
st.write(f"正解した問題数: {correct_answers} / {max_quiz_count}")

if correct_answers == max_quiz_count:
    st.success("おめでとうございます！すべての問題に正解しました。")
else:
    st.error("不正解があります。もう一度挑戦してみてください。")

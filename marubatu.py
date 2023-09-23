import streamlit as st

# 西暦年と対応する出来事のデータ
years_to_events = {
    1492: "コロンブスがアメリカを発見",
    1776: "アメリカ独立宣言",
    1969: "アポロ11号の月面着陸",
    2000: "新千年紀の到来",
    2020: "新型コロナウイルスの世界的な流行",
}

# クイズ用の問題と正解のデータ
quiz_data = [
    {"year": 1492, "event": "コロンブスがアメリカを発見", "answer": "〇"},
    {"year": 1776, "event": "アメリカ独立宣言", "answer": "〇"},
    {"year": 1969, "event": "アポロ11号の月面着陸", "answer": "〇"},
    {"year": 2000, "event": "新千年紀の到来", "answer": "〇"},
    {"year": 2020, "event": "新型コロナウイルスの世界的な流行", "answer": "〇"},
]

# アプリのタイトル
st.title("クイズアプリ")

# クイズのカウンターを初期化
quiz_count = 0
correct_answers = 0

# 5つのクイズを表示
for quiz in quiz_data:
    st.sidebar.markdown(f"問題 {quiz_count + 1}")
    selected_year = st.sidebar.selectbox("西暦年を選択してください", list(years_to_events.keys()))
    st.write(f"問題 {quiz_count + 1}: {quiz['event']}")

    # ユーザーの回答を取得
    user_answer = st.radio("正しいかどうかを選んでください", options=["〇", "×"])

    # 正誤を判定
    if user_answer == quiz["answer"]:
        st.success("正解！")
        correct_answers += 1
    else:
        st.error("不正解。正解は" + quiz["answer"])

    # 次の問題へ進むかどうかを確認
    quiz_count += 1
    if quiz_count < len(quiz_data):
        next_question = st.button("次の問題へ進む")
        if not next_question:
            break

# 最終的な結果を表示
st.title("クイズ結果")
st.write(f"正解した問題数: {correct_answers} / 5")

if correct_answers == 5:
    st.success("おめでとうございます！すべての問題に正解しました。")
else:
    st.error("不正解があります。もう一度挑戦してみてください。")


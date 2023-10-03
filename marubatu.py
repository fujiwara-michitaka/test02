import streamlit as st
import random

# カードの数字と対応する雑学クイズ
card_data = {
    1: "雑学クイズ1: 地球上で最も高い山は何か？",
    2: "雑学クイズ2: 北極圏に生息する動物は何か？",
    3: "雑学クイズ3: 日本の首都はどこか？",
    4: "雑学クイズ4: 北海道の最高気温は何度ぐらいになることがあるか？",
    5: "雑学クイズ5: 酸素の化学記号は何か？",
    6: "雑学クイズ6: イタリアの首都はどこか？",
    7: "雑学クイズ7: 水の沸点は何度か？",
    8: "雑学クイズ8: アメリカの国旗には何本の縞があるか？",
}

# カードを初期化
cards = list(card_data.keys()) * 2
random.shuffle(cards)

# ゲーム状態を管理する変数
selected_cards = []
found_pairs = 0
game_over = False

# アプリのタイトル
st.title("神経衰弱ゲーム")

# ゲームボードを表示
for i in range(4):
    for j in range(4):
        card_index = i * 4 + j
        if not game_over and st.button(f"カード {card_index + 1}"):
            if card_index not in selected_cards:
                selected_cards.append(card_index)
        
        if card_index in selected_cards or game_over:
            card_number = cards[card_index]
            st.image(f"card_{card_number}.png", use_container_width=True, key=f"card_{card_number}")

# ゲームロジック
if len(selected_cards) == 2 and not game_over:
    if cards[selected_cards[0]] == cards[selected_cards[1]]:
        st.success("正解！")
        found_pairs += 1
        selected_cards = []

        # ゲームクリア判定
        if found_pairs == len(card_data):
            game_over = True
            st.success("ゲームクリア！すべてのカードをゲットしました。")

    else:
        st.error("不正解")

# クイズ表示
if len(selected_cards) == 2 and not game_over:
    card_number = cards[selected_cards[0]]
    quiz_question = card_data[card_number]
    user_answer = st.text_input(quiz_question)
    
    if user_answer.lower() == "ok":
        selected_cards = []

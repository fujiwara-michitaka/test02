import streamlit as st
import random

# カードの数字
cards = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(cards)

# ゲーム状態を管理する変数
selected_cards = []
found_pairs = 0
game_over = False

# アプリのタイトル
st.title("神経衰弱ゲーム")

# カードを表示
for i in range(4):
    for j in range(4):
        card_index = i * 4 + j
        if not game_over and card_index not in selected_cards:
            if st.button(f"カード {card_index + 1}"):
                selected_cards.append(card_index)
        
        if card_index in selected_cards or game_over:
            card_number = cards[card_index]
            st.write(f"カード {card_index + 1}: {card_number}")

# ゲームロジック
if len(selected_cards) == 2 and not game_over:
    if cards[selected_cards[0]] == cards[selected_cards[1]]:
        st.success("正解！")
        found_pairs += 1
        selected_cards = []

        # ゲームクリア判定
        if found_pairs == len(cards) / 2:
            game_over = True
            st.success("ゲームクリア！すべてのカードをゲットしました。")
    else:
        st.error("不正解")

# リセットボタン
if game_over:
    if st.button("リセット"):
        selected_cards = []
        found_pairs = 0
        game_over = False
        random.shuffle(cards)

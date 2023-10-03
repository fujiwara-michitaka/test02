import streamlit as st
import random

# カードの数字
cards = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(cards)

# ゲーム状態を管理する変数
selected_cards = []
first_card = None
flip_timer_id = None

# アプリのタイトル
st.title("神経衰弱ゲーム")

# カードを表示
for i in range(4):
    for j in range(4):
        card_index = i * 4 + j
        if card_index not in selected_cards:
            if first_card is None or len(selected_cards) % 2 == 0:
                if st.button(f"カード {card_index + 1}"):
                    selected_cards.append(card_index)

# ゲームロジック
if len(selected_cards) % 2 == 0:
    card1 = selected_cards[-2]
    card2 = selected_cards[-1]
    if cards[card1] == cards[card2]:
        st.success("正解！")
        selected_cards.pop()
        selected_cards.pop()
        if len(selected_cards) == 16:
            st.success("ゲームクリア！すべてのカードをゲットしました。")
    else:
        st.error("不正解")
        flip_timer_id = st.empty()

        def reset_error():
            st.error("")
            flip_timer_id.empty()

        st.experimental_set_timeout(1, reset_error)

# リセットボタン
if len(selected_cards) == 16:
    if st.button("リセット"):
        selected_cards = []
        random.shuffle(cards)

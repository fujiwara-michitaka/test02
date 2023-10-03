import streamlit as st
import random

# スペード, ダイヤ, ハート, クローバー
suits = ["s", "d", "h", "c"]

# カード情報を配列に格納
cards = []
for suit in suits:
    for num in range(1, 14):
        cards.append((suit, num))

# シャッフルする関数
def shuffle(cards):
    shuffled = cards.copy()
    random.shuffle(shuffled)
    return shuffled

# Streamlitアプリケーションの開始
st.title("神経衰弱ゲーム")

# シャッフルボタン
if st.button("カードをシャッフル"):
    shuffled_cards = shuffle(cards)
    # シャッフルしたカードを表示
    for i, (suit, num) in enumerate(shuffled_cards):
        st.write(f"カード {i+1}: {suit}{num}")

st.text("カードをクリックして遊びましょう！")

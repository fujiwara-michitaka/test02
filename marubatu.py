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
    # シャッフルしたカードを表示（ダミー画像を使用）
    for i in range(0, len(cards), 13):
        row = st.beta_columns(13)
        for j in range(13):
            with row[j]:
                # ダミーのカード画像を表示
                st.image("https://via.placeholder.com/80x120.png", use_container_width=True, caption="カード")

st.text("カードをクリックして遊びましょう！")


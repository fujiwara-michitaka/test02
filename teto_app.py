import streamlit as st
import random

# ブロックの形状をランダムに生成
def random_shape():
    shapes = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1, 1], [0, 0, 1]],
    ]
    return random.choice(shapes)

# マトリックスを回転
def rotate_matrix(matrix):
    return [[row[i] for row in matrix][::-1] for i in range(len(matrix[0]))]

# ゲームボードの初期化
def create_grid(grid_rows, grid_cols):
    return [[0] * grid_cols for _ in range(grid_rows)]

# Streamlitアプリケーションの設定
st.title("テトリス")

grid_cols = 10
grid_rows = 20
block_size = 30
grid = create_grid(grid_rows, grid_cols)
player_block = None
player_x = 0
player_y = 0

st.set_canvas_update_mode("after")

def draw():
    global player_block, player_x, player_y

    st.clear()
    
    if player_block is None:
        player_block = random_shape() or [[1]]
        player_x = (grid_cols // 2) - (len(player_block[0]) // 2)
        player_y = 0
    
    player_y += 1
    
    for r in range(grid_rows):
        for c in range(grid_cols):
            if player_y <= r < player_y + len(player_block) and player_x <= c < player_x + len(player_block[0]):
                if player_block[r - player_y][c - player_x]:
                    st.rect(c * block_size, r * block_size, block_size, block_size)

draw()

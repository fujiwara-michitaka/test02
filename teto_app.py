import streamlit as st
import random

# テトリスのゲームボードサイズ
board_width = 10
board_height = 20
block_size = 30  # ブロックのサイズ

# テトリスのブロック形状
tetrominos = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [0, 0, 1]],  # L
    [[1, 1, 1], [1, 0, 0]],  # J
    [[1, 1], [1, 1]],  # Z
    [[1, 1], [0, 1, 1]]  # S
]

# テトリスの初期設定
board = [[0] * board_width for _ in range(board_height)]
current_tetromino = None
current_tetromino_x = 0
current_tetromino_y = 0

# ブロックをランダムに生成
def new_tetromino():
    global current_tetromino, current_tetromino_x, current_tetromino_y
    current_tetromino = random.choice(tetrominos)
    current_tetromino_x = board_width // 2 - len(current_tetromino[0]) // 2
    current_tetromino_y = 0

# ブロックを描画
def draw_tetromino():
    for y, row in enumerate(current_tetromino):
        for x, cell in enumerate(row):
            if cell:
                st.rect(
                    (current_tetromino_x + x) * block_size,
                    (current_tetromino_y + y) * block_size,
                    block_size,
                    block_size,
                )

# ゲームボードの表示
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                st.rect(x * block_size, y * block_size, block_size, block_size)

# ブロックを移動
def move_tetromino(dx, dy):
    global current_tetromino_x, current_tetromino_y
    current_tetromino_x += dx
    current_tetromino_y += dy

# ブロックが衝突したかどうかの判定
def is_collision():
    for y, row in enumerate(current_tetromino):
        for x, cell in enumerate(row):
            if cell:
                if (
                    current_tetromino_x + x < 0
                    or current_tetromino_x + x >= board_width
                    or current_tetromino_y + y >= board_height
                    or board[current_tetromino_y + y][current_tetromino_x + x]
                ):
                    return True
    return False

# ブロックを固定する
def lock_tetromino():
    for y, row in enumerate(current_tetromino):
        for x, cell in enumerate(row):
            if cell:
                board[current_tetromino_y + y][current_tetromino_x + x] = 1

    # 行が揃ったら削除
    for y in range(board_height - 1, -1, -1):
        if all(board[y]):
            del board[y]
            board.insert(0, [0] * board_width)

# テトリスのメインループ
def tetris_game():
    st.title("シンプルなTetris")

    st.sidebar.write("操作方法:")
    st.sidebar.write("左矢印キー: ブロックを左に移動")
    st.sidebar.write("右矢印キー: ブロックを右に移動")
    st.sidebar.write("下矢印キー: ブロックを下に移動")

    if current_tetromino is None:
        new_tetromino()

    st.set_canvas_update_mode("before")

    draw_board()
    draw_tetromino()

    st.set_canvas_update_mode("after")

    if is_collision():
        lock_tetromino()
        new_tetromino()

    move_tetromino(0, 1)

# Streamlitアプリを実行
if __name__ == "__main__":
    tetris_game()

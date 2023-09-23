import random

def pull_gacha(input_number):
    result = ""
    prize_image = ""
    
    if input_number < 0 or input_number > 100:
        result = "0から100の数値を入力してください"
    elif input_number <= 30:
        result = "ガチャが引けません"
    elif input_number <= 70:
        random_value = random.uniform(0, 100)
        if random_value < 74:
            result = "ノーマルが当たりました！"
        elif random_value < 99:
            result = "レアが当たりました！"
        else:
            result = "スーパーレアが当たりました！"
        prize_image = 'ノーマル/レア/スーパーレアの画像ファイル名'  # 各景品の画像ファイル名を設定
    else:
        random_value = random.uniform(0, 100)
        if random_value < 60:
            result = "ノーマルが当たりました！"
        elif random_value < 95:
            result = "レアが当たりました！"
        else:
            result = "スーパーレアが当たりました！"
        prize_image = 'ノーマル/レア/スーパーレアの画像ファイル名'  # 各景品の画像ファイル名を設定
    
    return result, prize_image

input_number = int(input("0から100の数値を入力してください: "))
result, prize_image = pull_gacha(input_number)

print(result)
if prize_image:
    print(f"景品画像: {prize_image}")


# 選択した数字を表示
st.write(f'あなたが選んだ数字は「{number}」です。')

# 選択した数値を2進数に変換
binary_representation = bin(number)[2:]  # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 10進数の「{number}」を2進数で表現すると「{binary_representation}」になります。 🔢')  # 2進数の表示をハイライト

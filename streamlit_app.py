import streamlit as st
import random

# 歴史的人物のデータ
historical_figures = [
    {"レアリティ": "SR", "人物名": "孔子", "説明": "中国の思想家で、儒教の創始者。倫理や教育についての教えを広めた。"},
    {"レアリティ": "R", "人物名": "嬴政（秦始皇）", "説明": "秦朝の始皇帝で、中国を統一した人物。万里の長城や兵馬俑を建設した。"},
    {"レアリティ": "R", "人物名": "劉備", "説明": "三国志の英雄で、蜀漢の創始者。仲間と共に魏と呉に抗戦した。"},
    {"レアリティ": "N", "人物名": "諸葛亮", "説明": "三国志の蜀漢の軍師で、睿智な策略家。龍のような器の持ち主とされた。"},
    {"レアリティ": "N", "人物名": "玄奘三蔵", "説明": "唐代の僧侶で、西域への仏典取り寄せの旅を記録した「大唐西域記」の著者。"},
    {"レアリティ": "N", "人物名": "李白", "説明": "唐代の詩人で、「詩仙」とも称される。酒や自然に詠嘆した詩が有名。"},
    {"レアリティ": "N", "人物名": "曹操", "説明": "三国志の魏の軍事家で、魏の建国者。策略に優れ、英雄との戦いを繰り広げた。"},
    {"レアリティ": "N", "人物名": "王羲之", "説明": "書道の名手で、東晋時代の書家。楷書や行書の創始者とされる。"},
    {"レアリティ": "N", "人物名": "呉承恩", "説明": "明代の医師で、『本草綱目』という薬物学の百科事典を著した。"},
    {"レアリティ": "SR", "人物名": "岳飛", "説明": "南宋時代の軍人で、岳家軍の指導者。抗金戦争で名声を馳せた英雄。"},
    {"レアリティ": "R", "人物名": "武則天", "説明": "唐代の皇帝で、唯一の女帝。政治改革と文化の発展を推進した。"},
    {"レアリティ": "R", "人物名": "蔡倫", "説明": "東漢時代の宮廷画家で、中国絵画史上の重要な人物。墨絵や山水画を得意とした。"},
    {"レアリティ": "R", "人物名": "范仲淹", "説明": "宋代の政治家で、政治改革や財政改革を実行し、新法の立案者として知られる。"},
    {"レアリティ": "N", "人物名": "張良", "説明": "前漢時代の軍師で、劉邦の重要な顧問。計略や策略に優れた智者として尊敬された。"},
    {"レアリティ": "N", "人物名": "王献之", "説明": "東晋時代の書家で、草書の大家。『蘭亭序』という名作を書いた。"},
    {"レアリティ": "N", "人物名": "范文正", "説明": "五胡十六国時代の政治家で、北魏の太尉。文化振興と国内安定に貢献した。"}


# ガチャを引く関数
def pull_gacha():
    random_figure = random.choice(historical_figures)
    return random_figure

# Streamlitアプリケーション
st.title("中国史の歴史的人物ガチャ")
st.write("ボタンをクリックしてガチャを引いて、ランダムな歴史的人物を入手しよう！")

if st.button("ガチャを引く"):
    result = pull_gacha()
    st.write(f"レアリティ: {result['レアリティ']}")
    st.write(f"人物名: {result['人物名']}")
    st.write(f"説明: {result['説明']}")

import streamlit as st
import pandas as pd
from scipy import stats

# Streamlitアプリのタイトルを設定
st.title("対応のないt検定アプリ")

# データ入力フォーム
st.header("データ入力")
n1 = st.number_input("第一群のデータの個数", min_value=1, step=1)
n2 = st.number_input("第二群のデータの個数", min_value=1, step=1)

data_group1 = []
data_group2 = []

st.write("第一群のデータ:")
for i in range(n1):
    data_group1.append(st.number_input(f"データ{i + 1}", step=0.01))

st.write("第二群のデータ:")
for i in range(n2):
    data_group2.append(st.number_input(f"データ{i + 1}", step=0.01))

# t検定を実行
if st.button("分析！"):
    # t検定を実行
    t_stat, p_value = stats.ttest_ind(data_group1, data_group2)
    
    # 結果を表示
    st.header("結果")
    st.write(f"第一群の平均値: {round(pd.Series(data_group1).mean(), 2)}")
    st.write(f"第一群の標準誤差: {round(pd.Series(data_group1).sem(), 2)}")
    st.write(f"第一群の標準偏差: {round(pd.Series(data_group1).std(), 2)}")
    
    st.write(f"第二群の平均値: {round(pd.Series(data_group2).mean(), 2)}")
    st.write(f"第二群の標準誤差: {round(pd.Series(data_group2).sem(), 2)}")
    st.write(f"第二群の標準偏差: {round(pd.Series(data_group2).std(), 2)}")
    
    st.write(f"t統計量: {round(t_stat, 2)}")
    st.write(f"p値: {p_value}")
    
    # 危険率による判定
    alpha = 0.05  # 有意水準 (0.05をデフォルトとしますが、必要に応じて変更してください)
    if p_value < alpha:
        st.write("結果: 統計的に有意な差があります！")
    else:
        st.write("結果: 統計的に有意な差はありません。")

# Streamlitアプリを起動
if __name__ == '__main__':
    st.set_page_config(layout="wide")
    st.sidebar.title("サイドバー")
    st.sidebar.info("このアプリは対応のないt検定を実行します。")
    st.write("このアプリはユーザーが第一群と第二群のデータを入力し、t検定の結果を表示します。")

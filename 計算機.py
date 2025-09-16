import streamlit as st

st.title("🧮 シンプル電卓")

# 入力
a = st.number_input("1つ目の数字を入力してください", value=0)
b = st.number_input("2つ目の数字を入力してください", value=0)

# 演算子を選択
op = st.selectbox("演算子を選んでください", ["+", "-", "*", "/"])

# 計算ボタン
if st.button("計算する"):
    if op == "+":
        st.write("結果:", a + b)
    elif op == "-":
        st.write("結果:", a - b)
    elif op == "*":
        st.write("結果:", a * b)
    elif op == "/":
        if b != 0:
            st.write("結果:", a / b)
        else:
            st.write("⚠️ 0では割れません")

import streamlit as st

st.title("簡単な電卓アプリ")

# 数字入力
number1 = st.number_input("1つめの数字を入力", step=1)
number2 = st.number_input("2つめの数字を入力", step=1)

# 演算子選択
hugou = st.selectbox("四則演算を選んでください", ["+", "-", "*", "/"])

# 計算と出力
if hugou == "+":
    st.write("結果:", number1 + number2)
elif hugou == "-":
    st.write("結果:", number1 - number2)
elif hugou == "*":
    st.write("結果:", number1 * number2)
elif hugou == "/":
    if number2 == 0:
        st.error("0では割れません")
    else:
        st.write("結果:", number1 / number2)

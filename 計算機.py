import streamlit as st

st.title("🧮 シンプル電卓")

number1=int(input("1つめ"))
number2=int(input("2つめ"))
hugou=input("四則演算")
if hugou=="+":
    print(number1+number2)
elif hugou=="-":
        print(number1-number2)
elif hugou=="*":
        print(number1*number2)
elif hugou=="/":
        print(number1/number2)
else:
    print("条件の見直し")
    elif op == "/":
        if b != 0:
            st.write("結果:", a / b)
        else:
            st.write("⚠️ 0では割れません")

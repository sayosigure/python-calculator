import streamlit as st

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

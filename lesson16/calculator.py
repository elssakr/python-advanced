import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Substraction":
        result = num1+ num2

    elif operation =="Multiplication":
        result = num1 + num2

    elif operation =="Division":
        try:
            result = num1/num2
        except ZeroDivisionError:
            result = "Cannot divide by zero"
        return result

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=1)

    operation = st.radio("Select operation", [])




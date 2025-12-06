import streamlit as st
from sympy.core.random import choice
from torchvision import message


def main():
    st.title("Hello, World")
    # st.button("Click me")

    if st.button("Click me"):
        st.write("Button Click")

    st.checkbox("Check me")

    if st.checkbox("Check me to show some text"):
        st.write("You have checked")

    user_input =st.text_input("Enter text", "Sample text")
    st.write("You entered:", user_input)

    age=st.number_input("Enter your age",min_value=0,max_value=100)
    st.write(f"Your age is: {age}")

    message=st.text_area("Enter your message")
    st.write(f"Your message: {message}")

    choice = st.radio("Pick one", ["choice 1","choice 2","choice 3"])
    st.write(f"You chose:{choice}")

    if st.button("success"):
        st.success("Operation was succesful")

    try:
        1/0
    except Exception as e:
        st.exception(e)


if __name__ =="__main__":
    main()
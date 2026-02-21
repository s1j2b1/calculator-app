

import streamlit as st

# عنوان الصفحة
st.set_page_config(page_title="Simple Calculator")

st.title("🧮 Simple Calculator")

# إدخال الأرقام
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# اختيار العملية
operation = st.selectbox(
    "Choose operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# زر الحساب
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None

    if result is not None:
        st.success(f"Result: {result}")


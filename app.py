import streamlit as st

# App Title
st.title("Simple Calculator")

# User Input
st.header("Enter two numbers")
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# Operation Selection
operation = st.selectbox(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate Button
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
            result = "Error! Division by zero."

    st.success(f"The result of {operation} is: {result}")

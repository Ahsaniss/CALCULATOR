import streamlit as st

# Set up the title of the app
st.title("Simple Calculator")

# Get user input
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division"))
number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)

# Perform the calculation based on the selected operation
if operation == "Addition":
    result = number1 + number2
elif operation == "Subtraction":
    result = number1 - number2
elif operation == "Multiplication":
    result = number1 * number2
elif operation == "Division":
    if number2 != 0:
        result = number1 / number2
    else:
        st.error("Error: Division by zero is not allowed.")
        result = None

# Display the result
if result is not None:
    st.success(f"The result of {operation} is: {result}")

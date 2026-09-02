import streamlit as st

# Task 2: Price Calculator

st.title("Price Calculator")

# 1. Takes product price (number input)
original_price = st.number_input("Enter product price:", min_value=0.0, step=10.0)

# 2. Takes discount percentage (slider from 0 to 50%)
discount = st.slider("Select discount percentage:", 0, 50, 0)

# 3. On button click, calculates discounted price
if st.button("Calculate Discount"):
    discount_amount = original_price * (discount / 100)
    final_price = original_price - discount_amount
    
    # 4. Shows result using st.success()
    st.success(f"Original Price: {original_price}")
    st.success(f"Discount: {discount}%")
    st.success(f"Final Price: {final_price}")
    
    # Extra (optional): Show comparison in a small table
    st.write("### Comparison")
    table_data = [
        ["Before", original_price],
        ["After", final_price]
    ]
    st.table(table_data)

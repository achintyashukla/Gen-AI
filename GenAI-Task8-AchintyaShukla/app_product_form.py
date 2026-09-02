import streamlit as st

# Task 3: Product Form

st.title("Product Form")

# 1. Use Streamlit sidebar to enter product details
product_name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Furniture", "Books", "Other"])
price = st.sidebar.number_input("Price", min_value=0.0, step=1.0)

# 2. When user clicks "Add Product" button in sidebar
if st.sidebar.button("Add Product"):
    # Show a success message in the main area
    st.success("Product added successfully!")
    
    # Show the product details in a clean format
    st.write("### Product Details")
    st.write(f"**Name:** {product_name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ${price:.2f}")

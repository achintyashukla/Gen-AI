import streamlit as st

# Task 4: Mini Dashboard

# 1. Title + Description
st.title("Simple Sales Dashboard")
st.write("This dashboard displays monthly sales data.")

# 2. A selectbox with months
months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select Month", months)

# 3. A static dictionary of monthly sales
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# 4. Display selected month's sales using st.metric()
st.metric(label=f"Sales in {selected_month}", value=f"${sales[selected_month]}")

# 5. Display a bar chart
# To keep order, we extract the values in the order of the months list
sales_values = [sales[month] for month in months]
st.write("### Monthly Sales Overview")
st.bar_chart(sales_values)

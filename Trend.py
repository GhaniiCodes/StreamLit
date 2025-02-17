
# Practice Questions for Streamlit

# Basic Data Display
# Display the first few rows of the dataset in a table using st.dataframe() or st.table().

# Filtering Data
# Create a sidebar filter to let users filter purchases by:
# Category (Clothing, Footwear, etc.)
# Season (Winter, Summer, etc.)
# Gender
# Display the filtered results dynamically.

# Data Visualization
# Bar Chart: Show the total purchase amount by category using st.bar_chart().
# Pie Chart: Display the percentage of purchases made by gender.
# Histogram: Show the distribution of review ratings.
# Statistical Insights

# Calculate and display:
# The average purchase amount.
# The most popular item purchased.
# The most common payment method.
# The correlation between previous purchases and purchase amount.
# User Interaction

# Let users select a "Customer ID" and display their details, including:
# Their total purchases.
# The most frequently purchased category.
# Their preferred payment method.
# Advanced Features

# Implement a search function where users enter an item name, and relevant purchases are displayed.
# Create a discount impact analysis, showing how discounts affect purchase amounts. ####



import pandas as pd
import numpy as np
import streamlit as st
import matplotlib as plt
import plotly.express as px


st.title("Shopping Trends")
st.write ("Here we Will be doing Analysis and Visulations of Shopping Trend Data")

Data = pd.read_csv("D:\PYTHON\Machine Learning\StreamLit\shopping_trends.csv")

st.write("Information Of Data")
st.write(Data.columns)

st.write(f"Head of Data")
st.write(Data.head())

st.write(f"Tail of Data")
st.write(Data.head())

st.header("Sales Per Category")


Category = Data.groupby("Category")["Purchase Amount (USD)"].sum()
Choices = Category.index

st.bar_chart(Category)

Selected_Category = st.selectbox("Select The Category " , Choices)
filtered_sales = Data[Data["Category"] == Selected_Category]["Purchase Amount (USD)"].sum()
st.write(f"{Selected_Category} has {filtered_sales} Sales")


st.header("Sales Data")

Sales = Data.groupby(["Category" , "Gender" , "Season"])["Purchase Amount (USD)"].sum().reset_index()


st.subheader(f"Break Down Of Sales in {Selected_Category}")

Selected_Sales = Sales[Sales["Category"] == Selected_Category]
st.dataframe(Selected_Sales)

Gender_Sales = Data.groupby("Gender")["Purchase Amount (USD)"].sum().reset_index()

Pie_Chart = px.pie(Gender_Sales,
             names="Gender", 
             values="Purchase Amount (USD)",
             title="Total Purchase Amount by Gender")

st.plotly_chart(Pie_Chart)


Histogram = px.histogram(Data , x=Data["Review Rating"] , title="Review Rating Distribution")
Histogram.update_traces(marker_line_color='black', marker_line_width=4)

st.plotly_chart(Histogram)

Average_Sales = Data.groupby("Category")["Purchase Amount (USD)"].mean()

Choices = Average_Sales.index
 
Selected_Category = st.selectbox("Select A Category" , Choices)
Filtered_Mean = Data[Data["Category"] == Selected_Category]["Purchase Amount (USD)"].mean()
st.write(f"{Selected_Category} has {Filtered_Mean} Average Sale")

st.header("Customer Details")

Customer_ID = st.text_input("Enter Your Customer ID")

if Customer_ID.isdigit():
    Customer_ID = int(Customer_ID)
    Customer_Data = Data[Data["Customer ID"] == Customer_ID]

    if not Customer_Data.empty:
        st.write(f"Customer ID : {Customer_ID}")
        st.write(f"Gender : {Customer_Data['Gender'].values[0]}")
        st.write(f"Age : {Customer_Data['Age'].values[0]}")
        st.write(f"Location : {Customer_Data['Location'].values[0]}")
        st.write(f"Total Sales : {Customer_Data['Purchase Amount (USD)'].sum()}")
        st.write(f"Subscription Status : {Customer_Data['Subscription Status'].values[0]}")
        st.write(f"Preferred Payment Method : {Customer_Data['Payment Method'].values[0]}")
        st.write(f"Previous Purchases : {Customer_Data['Previous Purchases'].values[0]}")
        st.write(f"Average Review Rating : {Customer_Data['Review Rating'].mean()}")
        
    else:
        st.write("No data found for this Customer ID.")
else:
    st.write("Please enter a valid numeric Customer ID")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

# Page Title
st.title('E-Commerce Dashboard')

# Showing Logo
st.image('logo.png', width=150) 

# Load the datasets
df = pd.read_csv('main_data.csv')

# Sidebar for navigation
st.sidebar.title('Navigation')
option = st.sidebar.selectbox('Select a page:', ['Home', 'Product Categories', 'Customer Transactions'])

# Home Page
if option == 'Home':
    st.header('E-Commerce Data Overview')
    st.write("This dashboard provides an analysis of e-commerce data including product categories and customer transactions.")

# Product Categories Analysis
if option == 'Product Categories':
    st.header('Most Sold Product Categories')

    top_categories = df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

    # Show bar plot of the top categories
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=top_categories.values, y=top_categories.index, ax=ax)
    ax.set_title('Top 10 Most Sold Product Categories')
    ax.set_xlabel('Number of Items Sold')
    ax.set_ylabel('Product Category')
    
    st.pyplot(fig)

# Customer Transactions Analysis
if option == 'Customer Transactions':
    st.header('Customer Transactions Over Time')
    
    # Convert order_purchase_timestamp to datetime
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])


    # Plot distribution of customer transactions over time
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['order_purchase_timestamp'], bins=50, kde=True, ax=ax)
    ax.set_title('Distribution of Customer Transactions Over Time')
    ax.set_xlabel('Transaction Date')
    ax.set_ylabel('Frequency')
    
    st.pyplot(fig)
    
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])

    # Streamlit title
    st.title('Distribusi Waktu Pengiriman Pesanan')

    # Create the figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the histogram
    sns.histplot(df['order_delivered_customer_date'], bins=50, kde=True, ax=ax)
    ax.set_title('Distribusi Waktu Pengiriman Pesanan')
    ax.set_xlabel('Tanggal Pengiriman')
    ax.set_ylabel('Frekuensi')

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Show the latest transaction for some customers
    st.write('### Sample of Recent Transactions')
    recent_transaction = df.groupby('customer_id')['order_purchase_timestamp'].max().reset_index()
    st.write(recent_transaction.sample(10))
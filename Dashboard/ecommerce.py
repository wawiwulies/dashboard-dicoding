import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

# Page Title
st.title('E-Commerce Dashboard')

# Showing Logo
st.image('Data/logo2.png', width=150) 

# Load the datasets
customers_df = pd.read_csv('Data/customers_dataset.csv')
order_items_df = pd.read_csv('Data/order_items_dataset.csv')
order_payments_df = pd.read_csv('Data/order_payments_dataset.csv')
product_category_df = pd.read_csv('Data/products_dataset.csv')
orders_df = pd.read_csv('Data/orders_dataset.csv')

# Sidebar for navigation
st.sidebar.title('Navigation')
option = st.sidebar.selectbox('Select a page:', ['Home', 'Product Categories', 'Customer Transactions'])

# Home Page
if option == 'Home':
    st.header('E-Commerce Data Overview')
    st.write("This dashboard provides an analysis of e-commerce data including product categories and customer transactions.")
    
    st.write("### Dataset Information:")
    st.write("Customers dataset has:", customers_df.shape[0], "rows and", customers_df.shape[1], "columns")
    st.write("Orders dataset has:", orders_df.shape[0], "rows and", orders_df.shape[1], "columns")

# Product Categories Analysis
if option == 'Product Categories':
    st.header('Most Sold Product Categories')
    
    # Merge order_items with product_category_df
    merged_df = pd.merge(order_items_df, product_category_df, on='product_id', how='left')

    # Group by product category and count the number of products sold in each category
    top_categories = merged_df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

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
    orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

    # Plot distribution of customer transactions over time
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(orders_df['order_purchase_timestamp'], bins=50, kde=True, ax=ax)
    ax.set_title('Distribution of Customer Transactions Over Time')
    ax.set_xlabel('Transaction Date')
    ax.set_ylabel('Frequency')
    
    st.pyplot(fig)

    # Show the latest transaction for some customers
    st.write('### Sample of Recent Transactions')
    recent_transaction = orders_df.groupby('customer_id')['order_purchase_timestamp'].max().reset_index()
    st.write(recent_transaction.sample(10))

# # Running Streamlit
# if _name_ == "_main_":
#     st.run()
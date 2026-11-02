import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("🍗 KFC Menu Analysis & ML App")
st.write("Welcome to the KFC Menu interactive web application!")

# Load dataset
file_path = 'kfc_menu_price_reference_2026.csv'
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.success("Dataset loaded successfully!")
    
    # Show dataframe
    st.subheader("📊 KFC Menu Dataset")
    st.dataframe(df)
    
    # Visualizations
    st.subheader("📈 Price Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['Base Price (PKR)'], kde=True, color='#E4002B', bins=8, ax=ax)
    ax.set_title("Distribution of Prices (PKR)")
    st.pyplot(fig)
else:
    st.error("Dataset file (kfc_menu_price_reference_2026.csv) not found in the repository!")

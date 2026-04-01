import pandas as pd
import streamlit as st

# Set up the Streamlit app
st.title("Data Visualization with Plotly and Streamlit")


# Load the dataset
def load_data():
    dt = "C:\\Users\\sudha\\Downloads\\Cleaned_dataset.csv\\Cleaned_dataset.csv"
    data = pd.read_csv(dt)
    st.write("Dataset Loaded Successfully!")
    st.dataframe(data.head(10))  # Display the first few rows of the dataset


if __name__ == "__main__":
    load_data()
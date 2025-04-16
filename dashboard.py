import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simple Dashboard", layout="wide")

st.title("📊 Streamlit Test Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")
num_rows = st.sidebar.slider("Number of rows", min_value=10, max_value=1000, value=100)

# Simulated data
@st.cache_data
def load_data(n):
    np.random.seed(42)
    data = pd.DataFrame({
        "Category": np.random.choice(["A", "B", "C"], n),
        "Value": np.random.randint(1, 100, size=n),
        "Score": np.random.normal(loc=50, scale=15, size=n)
    })
    return data

data = load_data(num_rows)

# Show data
st.subheader("📄 Raw Data")
st.dataframe(data)

# Simple Plot
st.subheader("📈 Value Distribution by Category")
chart_data = data.groupby("Category")["Value"].sum().reset_index()
st.bar_chart(chart_data.set_index("Category"))

# Histogram
st.subheader("📊 Score Distribution")
fig, ax = plt.subplots()
ax.hist(data["Score"], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)

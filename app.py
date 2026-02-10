import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")
st.title("Market Forecasting Dashboard")

# -----
# Load data ONCE
# -----
@st.cache_data
def load_data():
    df = pd.read_csv("NIFTY50_all.csv")
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df.sort_values(['Symbol', 'Date'])
    return df

df = load_data()

# -----
# Symbol selector
# -----
symbols = sorted(df['Symbol'].unique())
symbol = st.selectbox("Select Symbol", symbols)

# -----
# Filter selected stock
# -----
df_sym = df[df['Symbol'] == symbol].copy()
df_sym = df_sym.set_index('Date')

# -----
# Indicators
# -----
df_sym['SMA_50'] = df_sym['Close'].rolling(50).mean()
df_sym['SMA_200'] = df_sym['Close'].rolling(200).mean()

# -----
# Charts
# -----
st.subheader(f"{symbol} – Price Trend")
st.line_chart(df_sym['Close'])

st.subheader("Market Regime (Trend)")
st.line_chart(df_sym[['SMA_50', 'SMA_200']])

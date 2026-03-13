import yfinance as yf
import streamlit as st

@st.cache_data(ttl=3600)
def get_data(symbol):

    df = yf.download(
        symbol,
        period="1y",
        interval="1d",
        progress=False
    )

    return df

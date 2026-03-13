
import streamlit as st
from data.nse_symbols import get_nse_symbols
from data.search_symbols import search_stocks
from scanners.momentum import momentum_scan
from scanners.pattern_scanner import pattern_scan
from scanners.ai_multibagger import ai_scan

symbols = get_nse_symbols()

st.set_page_config(layout="wide")

st.title("AI Multibagger Research Terminal")

tabs = st.tabs([
"Stock Analyzer",
"Momentum Scanner",
"Pattern Scanner",
"AI Multibagger"
])

with tabs[0]:
    q = st.text_input("Search stock")
    if q:
        matches = search_stocks(q)
        s = st.selectbox("Select", matches)
        st.write(s)

with tabs[1]:
    st.subheader("Momentum")
    res = momentum_scan(symbols)
    for r in res[:10]:
        st.write(r)

with tabs[2]:
    st.subheader("Pattern Scanner")
    res = pattern_scan(symbols)
    for r in res[:10]:
        st.write(r)

with tabs[3]:
    st.subheader("AI Multibagger Candidates")
    res = ai_scan(symbols)
    for r in res[:10]:
        st.write(r)

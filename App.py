import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="御風東都全球資訊網（測試版）")
st.title("御風東都全球資訊網（測試版）")
#st.header("")

st.sidebar.header("網站分頁")
tab1, tab2, tab3 = st.tabs(["📊 回報清查", "📖 使用說明", "✉️ 聯絡資訊"])

with tab1:
    st.title("政務院")

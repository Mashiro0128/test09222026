import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="御風東都全球資訊網（測試版）")
st.title("御風東都全球資訊網（測試版）")

st.write("
    廢土伺服器第九分流/n
    御風東都社區/n
    歡迎你
")
st.sidebar.divider()  # 加一條分隔線
st.sidebar.header("網站分頁")
# 初始化預設分頁
if "page" not in st.session_state:
    st.session_state.page = "東都總府"

# 建立獨立按鈕
if st.sidebar.button("🏛️ 東都總府", use_container_width=True):
    st.session_state.page = "東都總府"
if st.sidebar.button("📜 政務院", use_container_width=True):
    st.session_state.page = "政務院"
if st.sidebar.button("⚖️ 協議院", use_container_width=True):
    st.session_state.page = "協議院"
if st.sidebar.button("📊 主計院", use_container_width=True):
    st.session_state.page = "主計院"

# 根據按鈕狀態顯示內容
page = st.session_state.page
if page == "東都總府":
    st.title("🏛️ 東都總府")
    st.write("這裡是東都總府頁面...")
elif page == "政務院":
    st.title("📜 政務院")
    st.write("這裡是政務院頁面...")
elif page == "協議院":
    st.title("⚖️ 協議院")
    st.write("這裡是協議院頁面...")
elif page == "主計院":
    st.title("📊 主計院")
    st.write("這裡是主計院頁面...")

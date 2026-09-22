import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="御風東都全球資訊網（測試版）")
st.title("御風東都全球資訊網（測試版）")

# 在側邊欄建立選單
st.sidebar.header("網站分頁")
page = st.sidebar.radio(
    "請選擇分頁",
    ["📊 回報清查", "📖 使用說明", "✉️ 聯絡資訊"],
    label_visibility="collapsed",  # 隱藏預設標題，畫面更整潔
)

# 根據側邊欄選擇顯示對應內容
if page == "📊 回報清查":
    st.title("政務院")
    # 放置回報清查的內容...

elif page == "📖 使用說明":
    st.header("使用說明")
    st.write("歡迎使用本系統，以下為操作指引...")

elif page == "✉️ 聯絡資訊":
    st.header("聯絡資訊")
    st.write("如有任何問題，請聯絡管理員。")

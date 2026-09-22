import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="御風東都全球資訊網（測試版）")
st.title("御風東都全球資訊網（測試版）")
st.sidebar.divider()  # 加一條分隔線

# 在側邊欄建立選單
st.sidebar.header("網站分頁")
st.sidebar.divider()  # 加一條分隔線
page = st.sidebar.radio(
    "請選擇分頁",
    ["東都總府", "政務院", "協議院","主計院"],
    label_visibility="collapsed",  # 隱藏預設標題，畫面更整潔
)

# 根據側邊欄選擇顯示對應內容
if page == "東都總府":
    st.header("御風東都中央行政委員會")
    # 放置回報清查的內容...

elif page == "政務院":
    st.header("政務院")
    st.write("歡迎使用本系統，以下為操作指引...")

elif page == "協議院":
    st.header("協議院")
    st.write("如有任何問題，請聯絡管理員。")

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="御風東都全球資訊網（測試版）", layout="wide")

# 1. 圖片路徑（Streamlit 讀取專案內圖片作為 HTML 背景的標準寫法）
img_url = "app/static/2025-05-19_21.37.15.jpg"

# 2. Hero Banner (全寬背景圖 + 壓字大標題)
st.markdown(
    f"""
    <div style="
        background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{img_url}');
        background-size: cover;
        background-position: center;
        height: 280px;
        border-radius: 12px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
    ">
        <h1 style="
            color: white;
            font-size: 2.8rem;
            font-weight: bold;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
            text-align: center;
            margin: 0;
        ">
            御風東都全球資訊網（測試版）
        </h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------- 側邊欄設定 (Sidebar) -------------------
st.sidebar.markdown("""
    廢土伺服器第九分流\n
    **御風東都社區**\n
    歡迎你
""")
st.sidebar.divider()  # 加一條分隔線

# 初始化預設分頁
if "page" not in st.session_state:
    st.session_state.page = "首頁"

# 【選單群組 1：行政機關】
st.sidebar.header("行政機關")
if st.sidebar.button("🏠 首頁", use_container_width=True):
    st.session_state.page = "首頁"
if st.sidebar.button("🏛️ 東都總府", use_container_width=True):
    st.session_state.page = "東都總府"
if st.sidebar.button("📜 政務院", use_container_width=True):
    st.session_state.page = "政務院"
if st.sidebar.button("⚖️ 協議院", use_container_width=True):
    st.session_state.page = "協議院"
if st.sidebar.button("📊 主計院", use_container_width=True):
    st.session_state.page = "主計院"

st.sidebar.divider()  # 分隔線

# 【選單群組 2：認識御風】
st.sidebar.header("認識御風")
if st.sidebar.button("📖 介紹", use_container_width=True):
    st.session_state.page = "介紹"
if st.sidebar.button("📜 御風歷史", use_container_width=True):
    st.session_state.page = "御風歷史"
if st.sidebar.button("🗺️ 御風東都地理", use_container_width=True):
    st.session_state.page = "御風東都地理"
if st.sidebar.button("⚖️ 御風東都法律", use_container_width=True):
    st.session_state.page = "御風東都法律"
if st.sidebar.button("📢 各類公告", use_container_width=True):
    st.session_state.page = "各類公告"

# ------------------- 主畫面內容顯示區 -------------------
page = st.session_state.page

if page == "首頁":
    st.title("🏠 歡迎蒞臨御風東都社區")
    st.write("這裡是御風東都全球資訊網的主頁面。")

elif page == "東都總府":
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

elif page == "介紹":
    st.title("📖 介紹")
    st.write("這裡是御風東都的簡介...")

elif page == "御風歷史":
    st.title("📜 御風歷史")
    st.write("這裡是御風東都的歷史記載...")

elif page == "御風東都地理":
    st.title("🗺️ 御風東都地理")
    st.write("這裡是地理資訊與地圖介紹...")

elif page == "御風東都法律":
    st.title("⚖️ 御風東都法律")
    st.write("這裡是御風東都的法律與規範...")

elif page == "各類公告":
    st.title("📢 各類公告")
    st.write("這裡是最新公告與消息列表...")

import streamlit as st

# 網址：https://windoftown.streamlit.app/

# 匯入首頁與各個獨立的機關檔案
import page_home
import page_gov10
# import page_gov11
# import page_gov12
# import page_gov13
# import page_info
import page_info_his
# import page_info_geo
# import page_info_law
# import page_anno

st.set_page_config(page_title="御風東都全球資訊網（測試版）", layout="wide")

# 1. 頂部 Hero Banner（全寬圖片 + 標題）
img_url = "2025-05-19_21.37.15.jpg"
st.markdown(
    f"""
    <div style="
        background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('{img_url}');
        background-size: cover;
        background-position: center;
        height: 250px;
        border-radius: 12px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 25px;
    ">
        <h1 style="
            color: white;
            font-size: 2.5rem;
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

# 2. 側邊欄抬頭資訊
# 側邊欄頂部
st.sidebar.image("your_handwritten_title.png", use_container_width=True)

# 2. 圖片下方放一個回到首頁的按鈕
if st.sidebar.button("🏠 返回首頁", use_container_width=True):
    st.session_state.page = "首頁"

st.sidebar.divider() # 加分隔線
st.sidebar.markdown("""
    廢土伺服器第九分流  
    **御風東都社區**  
    歡迎你
""")
st.sidebar.divider()  # 加一條分隔線

# 【修改處 1】將預設頁面設定為「首頁」
if "page" not in st.session_state:
    st.session_state.page = "首頁"

# 3. 側邊欄按鈕：行政機關區塊（不包含首頁按鈕）
st.sidebar.header("🏛️ 行政機關")
if st.sidebar.button("東都總府", use_container_width=True):
    st.session_state.page = "東都總府"
if st.sidebar.button("政務院", use_container_width=True):
    st.session_state.page = "政務院"
if st.sidebar.button("協議院", use_container_width=True):
    st.session_state.page = "協議院"
if st.sidebar.button("主計院", use_container_width=True):
    st.session_state.page = "主計院"

st.sidebar.divider()

# 4. 側邊欄按鈕：認識御風區塊
st.sidebar.header("📖 認識御風")
if st.sidebar.button("介紹", use_container_width=True):
    st.session_state.page = "介紹"
if st.sidebar.button("御風歷史", use_container_width=True):
    st.session_state.page = "御風歷史"
if st.sidebar.button("御風東都地理", use_container_width=True):
    st.session_state.page = "御風東都地理"
if st.sidebar.button("御風東都法律", use_container_width=True):
    st.session_state.page = "御風東都法律"
if st.sidebar.button("各類公告", use_container_width=True):
    st.session_state.page = "各類公告"


current_page = st.session_state.page

# 【修改處 2】進入網頁預設顯示「首頁」
if current_page == "首頁":
    page_home.render()

# 中央機關 [1, y]
elif current_page == "東都總府":
    page_gov10.render()

elif current_page == "政務院":
    # page_gov11.render()
    st.info("📜 政務院頁面建置中...")

elif current_page == "協議院":
    # page_gov12.render()
    st.info("⚖️ 協議院頁面建置中...")

elif current_page == "主計院":
    # page_gov13.render()
    st.info("📊 主計院頁面建置中...")

# 認識御風類
elif current_page == "介紹":
    # page_info.render()
    st.info("📖 介紹頁面建置中...")

elif current_page == "御風歷史":
    page_info_his.render()

elif current_page == "御風東都地理":
    # page_info_geo.render()
    st.info("🗺️ 御風東都地理頁面建置中...")

elif current_page == "御風東都法律":
    # page_info_law.render()
    st.info("⚖️ 御風東都法律頁面建置中...")

elif current_page == "各類公告":
    # page_anno.render()
    st.info("📢 各類公告頁面建置中...")

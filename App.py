import streamlit as st
#網址：https://windoftown.streamlit.app/
# 匯入各個獨立的機關檔案
import page_gov10
#import page_gov11
#import page_gov12
#import page_gov13
#import page_home
#import page_info

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
st.sidebar.markdown("""
    廢土伺服器第九分流  
    **御風東都社區**  
    歡迎你
""")
try:
    st.sidebar.image("螢幕擷取畫面 2025-09-18 171217.webp") 
except:
    pass
st.sidebar.divider()  # 加一條分隔線

# 3. 側邊欄按鈕：行政機關區塊
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

# 中央機關 [1, y]
elif current_page == "東都總府":
    page_gov10.render()  # 如果檔案專屬於東都總府，這裡甚至不需要傳參，直接呼叫 render() 即可
elif current_page == "政務院":
    page_gov11.render()
elif current_page == "協議院":
    page_gov12.render()
elif current_page == "主計院":
    page_gov13.render()

# 認識御風類
elif current_page in ["介紹", "御風歷史", "御風東都地理", "御風東都法律", "各類公告"]:
    page_info.render_info(current_page)

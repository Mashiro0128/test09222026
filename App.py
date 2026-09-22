import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="御風東都全球資訊網（測試版）")
st.title("御風東都全球資訊網（測試版）")
st.sidebar.divider()  # 加一條分隔線

page = st.sidebar.segmented_control(
    "頁面切換",
    ["東都總府", "政務院", "協議院", "主計院"],
    default="東都總府",
    label_visibility="collapsed"
)

if page == "東都總府":
    st.title("東都總府")
elif page == "政務院":
    st.title("政務院")
elif page == "協議院":
    st.title("協議院")
elif page == "主計院":
    st.title("主計院")

import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

col1, mid, col2= st.columns([1,1,20])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/5999/5999248.png", width=100)
with col2:
    st.markdown("# Meet Tina: Your Life, Business, and Career Coach")
    st.markdown("###### Chat in any language")

# embed in a streamlit app
st.components.v1.iframe("https://ora.sh/embed/614cf6db-1c92-4960-8e73-45dc4ef98460", width=1450, height=500, scrolling=True)

st.caption("Powered by")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/1280px-OpenAI_Logo.svg.png", width=50)

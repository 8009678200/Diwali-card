import streamlit as st

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide"
)

html_code = """
<h1 style='text-align:center;color:orange;'>
✨ Happy Diwali ✨
</h1>

<h2 style='text-align:center;color:white;'>
Swati & Shyam Family
</h2>
"""

st.components.v1.html(html_code, height=700)

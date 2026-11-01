import streamlit as st

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide"
)

html_code = """
<div style="
height:700px;
background:linear-gradient(135deg,#000000,#0b0f19,#111827);
display:flex;
justify-content:center;
align-items:center;
text-align:center;
color:white;
font-family:Arial,sans-serif;
">

<div>

<h1 style="
font-size:80px;
color:#ffb347;
text-shadow:0 0 20px orange;
">
✨ Happy Diwali ✨
</h1>

<h2 style="
font-size:40px;
color:white;
">
Swati & Shyam Family
</h2>

<p style="
font-size:24px;
line-height:1.8;
">
May every diya illuminate new dreams,<br>
every celebration create beautiful memories,<br>
and every sparkle bring happiness,
prosperity and endless blessings.
</p>

</div>

</div>
"""

st.components.v1.html(html_code, height=750)

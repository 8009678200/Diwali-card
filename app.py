import streamlit as st

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide"
)

# =========================
# LUXURY CSS
# =========================

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#000000,
#1a1200,
#332200,
#000000
);
color:white;
}

/* Sparkling Background */

.sparkles{
position: fixed;
top:0;
left:0;
width:100%;
height:100%;
pointer-events:none;
z-index:-1;
}

.sparkles span{
position:absolute;
display:block;
width:4px;
height:4px;
background:#FFD700;
border-radius:50%;
box-shadow:0 0 10px #FFD700;
animation:sparkle 8s linear infinite;
}

@keyframes sparkle{
0%{
transform:translateY(100vh) scale(0);
opacity:0;
}
50%{
opacity:1;
}
100%{
transform:translateY(-100vh) scale(1.5);
opacity:0;
}
}

/* Title */

.title{
text-align:center;
font-size:70px;
font-weight:bold;
color:#FFD700;
text-shadow:
0 0 15px #FFD700,
0 0 25px orange,
0 0 50px orange;
animation:glow 2s infinite alternate;
}

@keyframes glow{
from{
transform:scale(1);
}
to{
transform:scale(1.05);
}
}

/* Family */

.family{
text-align:center;
font-size:32px;
font-weight:bold;
color:white;
margin-bottom:20px;
}

/* Fireworks */

.fireworks{
text-align:center;
font-size:45px;
animation:fire 1s infinite alternate;
}

@keyframes fire{
from{
transform:scale(1);
}
to{
transform:scale(1.2);
}
}

/* Glass Card */

.glass{
background:rgba(255,255,255,.06);
padding:25px;
border-radius:20px;
backdrop-filter:blur(10px);
border:1px solid rgba(255,215,0,.4);
box-shadow:0 0 25px rgba(255,215,0,.5);
}

/* Diyas */

.diya{
text-align:center;
font-size:70px;
animation:float 2.5s ease-in-out infinite;
}

@keyframes float{
50%{
transform:translateY(-15px);
}
}

/* Quote */

.quote{
text-align:center;
font-size:24px;
color:#FFD700;
padding:15px;
}

/* Footer */

.footer{
text-align:center;
font-size:26px;
font-weight:bold;
color:white;
padding-top:30px;
}

</style>

<div class="sparkles">
<span style="left:5%"></span>
<span style="left:15%"></span>
<span style="left:25%"></span>
<span style="left:35%"></span>
<span style="left:45%"></span>
<span style="left:55%"></span>
<span style="left:65%"></span>
<span style="left:75%"></span>
<span style="left:85%"></span>
<span style="left:95%"></span>
</div>

""", unsafe_allow_html=True)

# =========================
# FIREWORKS
# =========================

st.markdown("""
<div class='fireworks'>
🎆 ✨ 🎇 ✨ 🎆 ✨ 🎇 ✨ 🎆
</div>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown("""
<div class='title'>
🪔 HAPPY DIWALI 🪔
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='family'>
❤️ Swati & Shyam Family ❤️
</div>
""", unsafe_allow_html=True)

# =========================
# DIYAS
# =========================

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.markdown("<div class='diya'>🪔</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='diya'>🪔</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='diya'>🪔</div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='diya'>🪔</div>", unsafe_allow_html=True)

with c5:
    st.markdown("<div class='diya'>🪔</div>", unsafe_allow_html=True)

# =========================
# QUOTES
# =========================

st.markdown("""
<div class='quote'>
✨ May every diya you light bring happiness,
success and prosperity into your life. ✨
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='quote'>
🪔 Celebrate the festival of lights with love,
joy and unforgettable memories. 🪔
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# PHOTO SECTION
# =========================

st.subheader("📸 Family Photo Upload")

photo = st.file_uploader(
    "Upload Family Photo",
    type=["jpg","jpeg","png"]
)

if photo:
    st.image(photo, use_container_width=True)

st.divider()

# =========================
# MUSIC SECTION
# =========================

st.subheader("🎵 Diwali Music")

audio = st.file_uploader(
    "Upload MP3 Song",
    type=["mp3","wav"]
)

if audio:
    st.audio(audio)

st.divider()

# =========================
# GREETING CARD
# =========================

st.subheader("💌 Personalized Greeting Card")

name = st.text_input(
    "Recipient Name",
    "Dear Friend"
)

message = f"""
🪔 HAPPY DIWALI 🪔

Dear {name},

May this Diwali bring
happiness,
prosperity,
good health,
success
and endless joy into your life.

Wishing you and your family
a wonderful Festival of Lights.

Best Wishes,
❤️ Swati & Shyam Family ❤️
"""

st.text_area(
    "Preview Card",
    message,
    height=250
)

# =========================
# DOWNLOAD CARD
# =========================

st.download_button(
    "📥 Download Greeting Card",
    data=message,
    file_name="Happy_Diwali_Greeting.txt",
    mime="text/plain"
)

# =========================
# CELEBRATION EFFECTS
# =========================

st.balloons()

# =========================
# FOOTER
# =========================

st.markdown("""
<div class='footer'>
🎇 Wishing You A Very Happy Diwali 🎇

<br>

🪔 With Love From Swati & Shyam Family 🪔
</div>
""", unsafe_allow_html=True)

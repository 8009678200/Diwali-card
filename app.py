import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide"
)

# ---------------------------
# AUTO PLAY MUSIC
# ---------------------------

music_file = "alex-morgan-diwali-festival-lights-celebration-575884.mp3"

if Path(music_file).exists():
    with open(music_file, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode()

    st.markdown(
        f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# LUXURY CSS
# ---------------------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(135deg,
#000000,
#1a1200,
#362404,
#000000);
color:white;
}

/* Golden Glow */
.main-title{
text-align:center;
font-size:70px;
font-weight:bold;
color:#FFD700;
text-shadow:
0 0 20px gold,
0 0 40px orange,
0 0 80px gold;
animation:zoom 2s infinite alternate;
}

@keyframes zoom{
from{transform:scale(1);}
to{transform:scale(1.05);}
}

/* Family Name */
.family{
text-align:center;
font-size:32px;
font-weight:bold;
color:white;
margin-bottom:20px;
}

/* Glass Card */
.glass{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:20px;
backdrop-filter:blur(15px);
box-shadow:0 0 25px gold;
border:1px solid gold;
}

/* Firework */
.firework{
font-size:50px;
text-align:center;
animation:blast 1s infinite alternate;
}

@keyframes blast{
from{transform:scale(1);}
to{transform:scale(1.25);}
}

/* Avatar */
.avatar{
display:flex;
justify-content:center;
margin-top:20px;
}

/* Quote */
.quote{
text-align:center;
font-size:24px;
color:#FFD700;
padding:10px;
font-weight:bold;
}

/* Footer */
.footer{
font-size:28px;
text-align:center;
font-weight:bold;
padding-top:30px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# FIREWORKS
# ---------------------------

st.markdown("""
<div class='firework'>
🎆 ✨ 🎇 ✨ 🎆 ✨ 🎇 ✨ 🎆
</div>
""", unsafe_allow_html=True)

# ---------------------------
# TITLE
# ---------------------------

st.markdown("""
<div class='main-title'>
🪔 HAPPY DIWALI 🪔
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='family'>
❤️ Swati & Shyam Family ❤️
</div>
""", unsafe_allow_html=True)

# ---------------------------
# ANIMATED AVATAR
# ---------------------------

if Path("avatar.gif").exists():
    st.markdown("<div class='avatar'>", unsafe_allow_html=True)
    st.image("avatar.gif", width=220)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# FAMILY PHOTO
# ---------------------------

st.markdown("<br>", unsafe_allow_html=True)

if Path("Joyful Diwali Family Celebration.png").exists():
    st.image(
        "Joyful Diwali Family Celebration.png",
        caption="Our Happy Family",
        use_container_width=True
    )

# ---------------------------
# QUOTES
# ---------------------------

st.markdown("""
<div class='quote'>
✨ May every diya bring happiness,
success and prosperity. ✨
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='quote'>
🪔 Let the Festival of Lights
fill your life with joy and love. 🪔
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------------------------
# GREETING CARD
# ---------------------------
# =========================
# GREETING CARD
# =========================

st.subheader("💌 Personalized Greeting Card")

name = st.text_input(
    "Enter Recipient Name",
    "Dear Friend"
)

message = f"""
...
"""

st.text_area(
    "Greeting Preview",
    value=message,
    height=250
)

st.download_button(
    "📥 Download Greeting Card",
    message,
    file_name="Happy_Diwali_Greeting.txt",
    mime="text/plain"
)

# ---------------------------
# EFFECTS
# ---------------------------

st.balloons()

# ---------------------------
# FOOTER
# ---------------------------

st.markdown("""
<div class='footer'>
🎇 Wishing You A Very Happy Diwali 🎇
<br><br>
🪔 With Love From Swati & Shyam Family 🪔
</div>
""", unsafe_allow_html=True)








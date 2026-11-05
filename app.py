import base64
import html
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide",
)

# ---------------------------
# AUTO PLAY MUSIC
# ---------------------------

music_file = Path("alex-morgan-diwali-festival-lights-celebration-575884.mp3")

if music_file.is_file():
    audio_base64 = base64.b64encode(music_file.read_bytes()).decode("utf-8")
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# LUXURY CSS
# ---------------------------

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000, #1a1200, #362404, #000000);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 70px;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 0 0 20px gold, 0 0 40px orange, 0 0 80px gold;
        animation: zoom 2s infinite alternate;
    }

    @keyframes zoom {
        from { transform: scale(1); }
        to { transform: scale(1.05); }
    }

    .family {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    }

    .firework {
        font-size: 50px;
        text-align: center;
        animation: blast 1s infinite alternate;
    }

    @keyframes blast {
        from { transform: scale(1); }
        to { transform: scale(1.25); }
    }

    .avatar {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .quote {
        text-align: center;
        font-size: 24px;
        color: #FFD700;
        padding: 10px;
        font-weight: bold;
    }

    .footer {
        font-size: 28px;
        text-align: center;
        font-weight: bold;
        padding-top: 30px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# FIREWORKS AND TITLE
# ---------------------------

st.markdown(
    "<div class='firework'>🎆 ✨ 🎇 ✨ 🎆 ✨ 🎇 ✨ 🎆</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='main-title'>🪔 HAPPY DIWALI 🪔</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='family'>❤️ Swati &amp; Shyam Family ❤️</div>",
    unsafe_allow_html=True,
)

# ---------------------------
# ANIMATED AVATAR
# ---------------------------

avatar_file = Path("avatar.gif")
if avatar_file.is_file():
    st.markdown("<div class='avatar'>", unsafe_allow_html=True)
    st.image(str(avatar_file), width=220)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# FAMILY PHOTO
# ---------------------------

st.markdown("<br>", unsafe_allow_html=True)
family_photo = Path("family.png")
if family_photo.is_file():
    st.image(
        str(family_photo),
        caption="Our Happy Family",
        use_container_width=True,
    )

# ---------------------------
# QUOTES
# ---------------------------

st.markdown(
    """
    <div class='quote'>
    ✨ May every diya bring happiness, success and prosperity. ✨
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class='quote'>
    🪔 Let the Festival of Lights fill your life with joy and love. 🪔
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ---------------------------
# PERSONALIZED GREETING CARD
# ---------------------------

st.subheader("💌 Personalized Greeting Card")
name = st.text_input("Enter Recipient Name", "Dear Friend")
safe_name = html.escape(name.strip() or "Friend")

message = f"""Happy Diwali, {name.strip() or 'Friend'}!

May your life be filled with light, happiness, peace, prosperity, and love.
Wishing you and your family a joyful and blessed Diwali celebration.

With love,
Swati & Shyam Family"""

st.markdown(
    f"""
    <div style="
        background:linear-gradient(135deg,#ff9933,#ffcc00,#ff66cc,#9966ff);
        padding:30px;
        border-radius:25px;
        text-align:center;
        color:white;
        font-size:22px;
        font-weight:bold;
        box-shadow:0 0 30px gold;
        margin-top:20px;
    ">
        <h1>🪔 HAPPY DIWALI 🪔</h1>
        <h2>Dear {safe_name}</h2>
        <p>
            ✨ Happiness ✨<br>
            💰 Prosperity 💰<br>
            🌟 Success 🌟<br>
            ❤️ Love ❤️<br>
            😊 Good Health 😊<br>
            🎉 Endless Joy 🎉
        </p>
        <h3>❤️ Swati &amp; Shyam Family ❤️</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.download_button(
    "📥 Download Greeting Card",
    data=message,
    file_name="Happy_Diwali_Greeting.txt",
    mime="text/plain",
)

# ---------------------------
# EFFECTS AND FOOTER
# ---------------------------

st.balloons()
st.markdown(
    """
    <div class='footer'>
        🎇 Wishing You A Very Happy Diwali 🎇<br><br>
        🪔 With Love From Swati &amp; Shyam Family 🪔
    </div>
    """,
    unsafe_allow_html=True,
)

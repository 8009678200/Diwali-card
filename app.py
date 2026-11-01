import streamlit as st

st.set_page_config(
    page_title="Happy Diwali",
    page_icon="🪔",
    layout="wide"
)

html_code = """
<div id="diwali-card">

<style>

@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&family=Cinzel:wght@400;700;900&display=swap');

#diwali-card{
height:750px;
position:relative;
overflow:hidden;
text-align:center;
color:white;

background:
radial-gradient(circle at top left,
rgba(255,140,0,.10),
transparent 30%),

radial-gradient(circle at top right,
rgba(255,215,0,.08),
transparent 35%),

linear-gradient(
135deg,
#000000 0%,
#050505 20%,
#0b0f19 50%,
#111827 100%
);

animation:bgGlow 8s ease-in-out infinite;
}

@keyframes bgGlow{
0%,100%{
filter:brightness(1);
}
50%{
filter:brightness(1.08);
}
}

/* Glass Card */

.glass{
position:absolute;
top:50%;
left:50%;
transform:translate(-50%,-50%);
width:75%;
padding:40px;
background:rgba(255,255,255,0.04);
backdrop-filter:blur(20px);
-webkit-backdrop-filter:blur(20px);
border:1px solid rgba(255,215,0,.12);
border-radius:30px;
box-shadow:0 0 35px rgba(255,215,0,0.15);
z-index:2;
}

.title{
font-family:'Great Vibes', cursive;
font-size:90px;
font-weight:400;
color:#ffb347;
text-shadow:
0 0 5px #ffb347,
0 0 10px #ffb347,
0 0 20px #ff8c00,
0 0 40px #ff8c00;
animation: glow 2s ease-in-out infinite alternate;
}

.family{
font-family:'Great Vibes', cursive;
font-size:55px;
color:#ffd699;
margin-top:10px;
text-shadow:
0 0 5px #ffb347,
0 0 15px #ff8c00;
}

.quote{
font-family:'Poppins', sans-serif;
font-size:22px;
line-height:1.8;
color:white;
margin-top:20px;
}

.signature {
    font-family: 'Cinzel', serif;
    margin-top: 30px;
    font-size: 24px;
    color: #FFD700;
    letter-spacing: 2px;
}

@keyframes glow {
    50% {
        filter: drop-shadow(0 0 25px gold);
    }
}

/* DIYAS */
.diya {
    position: absolute;
    bottom: 30px;
    font-size: 60px;
    animation: flicker 1s infinite alternate;
    z-index: 3;
}

@keyframes flicker {
    from {
        transform: translateY(0px) scale(1);
        filter: drop-shadow(0 0 5px gold);
    }
    to {
        transform: translateY(-8px) scale(1.05);
        filter: drop-shadow(0 0 20px orange);
    }
}

/* STARS */
.star {
    position: absolute;
    width: 4px;
    height: 4px;
    background: gold;
    border-radius: 50%;
    animation: twinkle 2s infinite;
}

@keyframes twinkle {
    50% {
        opacity: .2;
        transform: scale(.4);
    }
}

/* FIREWORKS */
.firework {
    position: absolute;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    animation: explode 2s forwards;
}

@keyframes explode {
    0% {
        transform: scale(0);
        opacity: 1;
    }
    100% {
        transform: scale(20);
        opacity: 0;
    }
}

</style>

<div class="glass">
    <div class="title">Happy Diwali</div>
    <div class="family">✨ Swati & Shyam Family ✨</div>
    <div class="quote">
        “May every spark of Diwali illuminate your path,<br>
        every celebration bring cherished memories,<br>
        and every blessing fill your home with joy,<br>
        prosperity and endless happiness.”
    </div>
    <div class="signature">🪔 Wishing You Endless Blessings 🪔</div>
</div>

<!-- Diyas -->
<div class="diya" style="left: 5%;">🪔</div>
<div class="diya" style="left: 20%;">🪔</div>
<div class="diya" style="left: 35%;">🪔</div>
<div class="diya" style="right: 35%;">🪔</div>
<div class="diya" style="right: 20%;">🪔</div>
<div class="diya" style="right: 5%;">🪔</div>

</div>

<script>
const card = document.getElementById("diwali-card");

/* STARS */
for(let i = 0; i < 150; i++) {
    let star = document.createElement("div");
    star.className = "star";
    star.style.left = Math.random() * 100 + "%";
    star.style.top = Math.random() * 100 + "%";
    star.style.animationDelay = Math.random() * 3 + "s";
    card.appendChild(star);
}

/* FIREWORKS */
setInterval(() => {
    let fw = document.createElement("div");
    fw.className = "firework";
    fw.style.left = Math.random() * 90 + "%";
    fw.style.top = Math.random() * 45 + "%";

    const colors = ["#FFD700", "#FF4081", "#00E5FF", "#4CAF50", "#FF9800", "#FFFFFF"];
    fw.style.background = colors[Math.floor(Math.random() * colors.length)];
    card.appendChild(fw);

    setTimeout(() => {
        fw.remove();
    }, 2000);
}, 400);
</script>

st.components.v1.html(
    html_code,
    height=800,
    scrolling=False
)

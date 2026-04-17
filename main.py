import streamlit as st
import string
import random

# 1. KONFIGURATSIYA
st.set_page_config(page_title="L1GHTDREAM", layout="wide")

# 2. MATRIX FON VA CSS (FORCE TRANSPARENCY)
st.markdown("""
<style>
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background: transparent !important;
    }
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -2;
        background-color: black;
    }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 25px #00FF00;
        border-radius: 15px;
        padding: 40px;
        margin-top: 15px;
    }
    .header-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 65px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
        letter-spacing: 10px;
    }
    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        font-family: 'Courier New', monospace;
    }
</style>

<canvas id="matrix-canvas"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth; canvas.height = window.innerHeight;
    const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
    const fontSize = 16;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#0F0';
        ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < drops.length; i++) {
            const text = chars[Math.floor(Math.random() * chars.length)];
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
            drops[i]++;
        }
    }
    setInterval(draw, 35);
</script>
""", unsafe_allow_html=True)

# 3. VAQTNI FORMATLASH
def format_time(sec):
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 60: return f"{sec:.2f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

# 4. ASOSIY QISM
st.markdown("<div class='header-title'>L1GHTDREAM</div>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS CODE >", type="password")

if pwd:
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    t_html = "".join([f"<div class='token-box'>{c}</div>" for c in pwd])
    st.markdown(f"<div>{t_html}</div>", unsafe_allow_html=True)
    
    # MATEMATIK HISOB (100 mlrd urinish/sek)
    pool = 26
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    if has_upper: pool += 26
    if has_digit: pool += 10
    if has_special: pool += 32
    
    current_sec = (pool ** len(pwd)) / 10**11 if len(pwd) > 0 else 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div style='border: 1px solid #00FF00; padding: 15px; color:#00FF00;'> Uzunlik: {len(pwd)} ta | Katta: {sum(1 for c in pwd if c.isupper())} ta</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<b style='color:#00FF00;'>DINAMIK TAHLIL:</b>", unsafe_allow_html=True)
        # BU YERDA FAQAT REAL FARQ KO'RSATILADI
        if not has_upper:
            diff = (((pool + 26) ** len(pwd)) / 10**11) - current_sec
            st.info(f"💡 Katta harf qo'shilsa: +{format_time(diff)}")
        if not has_digit:
            diff = (((pool + 10) ** len(pwd)) / 10**11) - current_sec
            st.info(f"💡 Raqam qo'shilsa: +{format_time(diff)}")

    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {format_time(current_sec)}")

    # SUGGESTIONS
    st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(3):
        sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0,9))
        cols[i].code(sug)

with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<div style='color:#00FF00;'><b>Dasturchi:</b> Moxirxo'ja<br><b>Nickname:</b> LIMITLESS</div>", unsafe_allow_html=True)

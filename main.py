import streamlit as st
import string
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM", layout="wide")

# 2. MATRIX FON VA CSS (Shaffoflik va fonni qulflash)
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
        margin-top: 20px;
        color: #00FF00;
    }
    .header-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 65px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
        letter-spacing: 10px; margin-bottom: 30px;
    }
    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        font-family: 'Courier New', monospace;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border-right: 2px solid #00FF00;
    }
</style>

<canvas id="matrix-canvas"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵ';
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

# 3. ASOSIY QISM
st.markdown("<div class='header-title'>L1GHTDREAM</div>", unsafe_allow_html=True)
pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # --- 1. NEURAL TOKENIZATION ---
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    t_html = "".join([f"<div class='token-box'>{c}</div>" for c in pwd])
    st.markdown(f"<div>{t_html}</div>", unsafe_allow_html=True)
    
    # --- BUZISH VAQTI VA MATEMATIK HISOB ---
    pool = 0
    if any(c.islower() for c in pwd): pool += 26
    if any(c.isupper() for c in pwd): pool += 26
    if any(c.isdigit() for c in pwd): pool += 10
    if any(c in string.punctuation for c in pwd): pool += 32
    
    comb = (pool ** len(pwd)) if len(pwd) > 0 else 0
    sec = comb / 100_000_000_000 # 100 mlrd urinish/sek
    
    # --- STATISTIKA VA DINAMIK MASLAHATLAR ---
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style='border: 1px solid #00FF00; padding: 15px; background: rgba(0,255,0,0.05);'>
            > Jami: {len(pwd)} ta | Katta: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqam: {sum(1 for c in pwd if c.isdigit())} ta | Belgi: {sum(1 for c in pwd if c in string.punctuation)} ta
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        # Haqiqiy vaqt ortishini hisoblash (pool + qo'shimcha belgilar)
        if not any(c.isupper() for c in pwd):
            extra_sec = ((pool + 26) ** len(pwd) / 100_000_000_000) - sec
            st.info(f"💡 Katta harf qo'shilsa: +{extra_sec:.4f} sek")
        if len(pwd) < 12:
            st.warning("💡 Uzunlikni 12 taga yetkazish tavsiya etiladi!")

    brute = f"{sec:.4f} sek" if sec < 60 else f"{sec/60:.2f} min" if sec < 3600 else f"{int(sec/31536000)} yil"
    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")

    # --- 2. SMART SUGGESTIONS ---
    st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(3):
        sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0,9))
        cols[i].code(sug)

# 4. SIDEBAR (Faqat ism va nickname)
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"""
    <div style='color:#00FF00; font-family:monospace;'>
        <b>Dasturchi:</b> Moxirxo'ja<br><br>
        <b>Nickname:</b> LIMITLESS
    </div>
    """, unsafe_allow_html=True)

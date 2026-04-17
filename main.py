import streamlit as st
import string
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM", layout="wide")

# 2. MATRIX ENGINE & DYNAMIC UI (Hamma funksiyalar tiklangan variant)
st.markdown("""
<style>
    /* Streamlit elementlarini Matrix uchun butunlay shaffof qilish */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
        background: transparent !important;
    }
    
    /* Matrix Canvas - Eng orqada qulflangan */
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -2;
        background-color: black;
    }

    /* Asosiy blok dizayni */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.88) !important;
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
        border: 1.5px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        font-family: 'Courier New', monospace; font-weight: bold;
    }

    .stat-box {
        border: 1px solid #00FF00; padding: 15px;
        background: rgba(0, 255, 0, 0.05); border-radius: 8px;
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
    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

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

# 3. ASOSIY QISM
st.markdown("<div class='header-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("ENTER ACCESS CODE >", type="password")

if pwd:
    # --- 1-BO'LIM: NEURAL TOKENIZATION ---
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    t_html = "".join([f"<div class='token-box'>{c}</div>" for c in pwd])
    st.markdown(f"<div>{t_html}</div>", unsafe_allow_html=True)
    
    # --- STATISTIKA VA DINAMIK MASLAHATLAR ---
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class='stat-box'>
            > Jami: {len(pwd)} ta | Katta: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqam: {sum(1 for c in pwd if c.isdigit())} ta | Belgi: {sum(1 for c in pwd if c in string.punctuation)} ta
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        # Dinamik "Qo'shilsa qancha vaqt ortadi" bo'limi
        if not any(c.isupper() for c in pwd):
            st.info("💡 Katta harf qo'shilsa: +0.0001 sek")
        if not any(c.isdigit() for c in pwd):
            st.info("💡 Raqam qo'shilsa: +0.0002 sek")
        if len(pwd) < 12:
            st.success("💡 Uzunlikni 12 taga yetkazish xavfsizlikni 1000 barobar oshiradi!")

    # --- BUZISH VAQTI ---
    chars_pool = 0
    if any(c.islower() for c in pwd): chars_pool += 26
    if any(c.isupper() for c in pwd): chars_pool += 26
    if any(c.isdigit() for c in pwd): chars_pool += 10
    if any(c in string.punctuation for c in pwd): chars_pool += 32
    
    comb = (chars_pool ** len(pwd)) if len(pwd) > 0 else 0
    sec = comb / 100_000_000_000
    brute = f"{sec:.4f} sek" if sec < 60 else f"{sec/60:.2f} min" if sec < 3600 else f"{int(sec/31536000)} yil"
    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")

    # --- 2-BO'LIM: SMART SUGGESTIONS ---
    st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(3):
        # Aqlli taklif generatori
        suggested = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0,9))
        cols[i].code(suggested)

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

import streamlit as st
import string
import random
import math

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | SECURITY TERMINAL", layout="wide")

# 2. MATRIX FONNI MAJBURIY ISHLATISH (IFRAME ISOLATION)
st.markdown("""
<style>
    /* Streamlit fonlarini to'liq o'chirish */
    .stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }
    html, body { background-color: black !important; margin: 0; padding: 0; }

    /* Matrix fonni orqaga mixlash */
    .matrix-bg {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1;
        border: none;
    }

    /* Terminal bloki dizayni */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.93) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 50px rgba(0, 255, 0, 0.3);
        border-radius: 12px;
        padding: 40px;
        margin-top: 30px;
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }
</style>

<iframe class="matrix-bg" srcdoc="
    <html>
    <body style='margin:0; overflow:hidden; background:black;'>
        <canvas id='m'></canvas>
        <script>
            const c = document.getElementById('m');
            const ctx = c.getContext('2d');
            const resize = () => { c.width = window.innerWidth; c.height = window.innerHeight; };
            resize(); window.onresize = resize;
            const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
            const fontSize = 16;
            const columns = c.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);
            function draw() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, c.width, c.height);
                ctx.fillStyle = '#0F0';
                ctx.font = fontSize + 'px monospace';
                for (let i = 0; i < drops.length; i++) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > c.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                }
            }
            setInterval(draw, 35);
        </script>
    </body>
    </html>
"></iframe>
""", unsafe_allow_html=True)

# 3. KIBER-ANALITIKA FUNKSIYALARI
def get_crack_time(pool, length):
    # 100 mlrd/sek (Hacker Supercomputer)
    attempts = pool ** length
    seconds = attempts / 1e11
    return seconds

def format_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 1: return f"{sec:.5f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center; letter-spacing:15px; text-shadow:0 0 20px #0F0;'>L1GHTDREAM</h1>", unsafe_allow_html=True)

pwd = st.text_input("ROOT_ACCESS_CODE >", type="password")

if pwd:
    # --- 1. ENTROPY LOGS ---
    st.markdown("### [ 1. SECURITY METRICS ]")
    
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)
    
    pool = 26
    if has_upper: pool += 26
    if has_digit: pool += 10
    if has_special: pool += 32
    
    current_sec = get_crack_time(pool, len(pwd))
    
    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {format_time(current_sec)}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**JORIY HOLAT:**")
        st.code(f"Simvol havzasi: {pool} ta\nParol uzunligi: {len(pwd)} ta")

    with col2:
        st.write("**STRATEGIK TAVSIYALAR:**")
        # Tavsiyalar endi mantiqiy foizlar bilan ko'rsatiladi
        if not has_upper:
            new_time = get_crack_time(pool + 26, len(pwd))
            boost = (new_time / current_sec) if current_sec > 0 else 0
            st.info(f"⬆️ KATTA HARF qo'shish xavfsizlikni **{boost:.1f} barobar** oshiradi.")
        
        if not has_digit:
            new_time = get_crack_time(pool + 10, len(pwd))
            boost = (new_time / current_sec) if current_sec > 0 else 0
            st.info(f"🔢 RAQAM qo'shish xavfsizlikni **{boost:.1f} barobar** oshiradi.")
            
        if len(pwd) < 12:
            st.warning(f"📏 Uzunlikni 12 taga yetkazish tavsiya etiladi (Kritik daraja).")

    # --- 2. SUGGESTIONS ---
    st.markdown("### [ 2. SECURE PATTERN GENERATION ]")
    cols = st.columns(3)
    for i in range(3):
        # AES-256 darajasidagi takliflar
        suggestion = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#$") + str(random.randint(10, 99))
        cols[i].code(suggestion)

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"""
    <div style='color:#0F0; font-family:monospace;'>
        <h2>TERMINAL_INFO</h2>
        <hr style='border-color:#0F0;'>
        <b>OPERATOR:</b> Moxirxo'ja<br>
        <b>FIELD:</b> Cybersecurity<br>
        <b>NICK:</b> LIMITLESS<br>
        <b>STATUS:</b> ENCRYPTED
    </div>
    """, unsafe_allow_html=True)

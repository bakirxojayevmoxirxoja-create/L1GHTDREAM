import streamlit as st
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM", layout="wide")

# 2. MATRIX FON VA TOZA DIZAYN
def apply_theme():
    st.markdown("""
    <style>
    /* Matrix orqa fon */
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1;
    }
    .stApp { background: transparent; }
    
    /* Markaziy blok */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 25px #00FF00;
        border-radius: 15px;
        padding: 40px;
        margin-top: 30px;
        color: #00FF00;
    }
    
    .header-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 60px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
        margin-bottom: 25px;
    }
    
    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
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
    window.onresize = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    };
    </script>
    """, unsafe_allow_html=True)

apply_theme()

# 3. ASOSIY QISM
st.markdown("<div class='header-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. Tokenizatsiya (Xatosiz usul)
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    html_str = ""
    for t in list(pwd):
        html_str += f"<div class='token-box'>{t}</div>"
    st.markdown(f"<div>{html_str}</div>", unsafe_allow_html=True)
    
    # 2. Statistika
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style='border-left: 3px solid #00FF00; padding-left: 15px; background: rgba(0,255,0,0.05); padding: 10px;'>
            > Jami: {len(pwd)} ta<br>
            > Katta harf: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqamlar: {sum(1 for c in pwd if c.isdigit())} ta
        </div>
        """, unsafe_allow_html=True)
    
    # 3. Buzish vaqti
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    
    seconds = (charset ** len(pwd)) / 100_000_000_000 if len(pwd) > 0 else 0
    if seconds < 60:
        brute = f"{seconds:.4f} sek"
    elif seconds < 3600:
        brute = f"{seconds/60:.2f} min"
    else:
        brute = f"{int(seconds/31536000)} yil"
        
    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")

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

import streamlit as st
import string
import random

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | SECURITY TERMINAL", layout="wide")

# 2. MATRIX FON (IFRAME METHOD - BU QISM O'ZGARMADI)
st.markdown("""
<style>
    .stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }
    html, body { background-color: black !important; }
    .matrix-bg {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1; border: none;
    }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.93) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 50px rgba(0, 255, 0, 0.3);
        border-radius: 12px;
        padding: 40px; margin-top: 30px;
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    /* Tokenizatsiya uchun maxsus boxlar */
    .token-box {
        display: inline-block;
        border: 1px solid #00FF00;
        padding: 8px 15px;
        margin: 5px;
        background: rgba(0, 255, 0, 0.1);
        font-weight: bold;
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
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

# 3. YORDAMCHI FUNKSIYALAR
def format_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

def generate_strong_suggestion(base_pwd):
    # Katta harf, raqam va belgilar to'plami
    special = "!@#$%^&*"
    digits = string.digits
    uppers = string.ascii_uppercase
    
    # Parolga murakkablik qo'shish
    res = list(base_pwd)
    res.insert(random.randint(0, len(res)), random.choice(uppers))
    res.append(random.choice(special))
    res.extend([random.choice(digits) for _ in range(2)])
    
    # Uzunlikni kamida 12 taga yetkazish
    while len(res) < 12:
        res.append(random.choice(string.ascii_lowercase))
        
    random.shuffle(res)
    return "".join(res)

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center; letter-spacing:15px; text-shadow:0 0 20px #0F0;'>L1GHTDREAM</h1>", unsafe_allow_html=True)

pwd = st.text_input("ENTER ACCESS CODE >", type="password")

if pwd:
    # --- TOKENIZATION ---
    st.markdown("### [ 1. NEURAL TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    # --- ANALYSIS ---
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)
    
    pool = 26
    if has_upper: pool += 26
    if has_digit: pool += 10
    if has_special: pool += 32
    
    current_sec = (pool ** len(pwd)) / 1e11 if len(pwd) > 0 else 0
    
    st.error(f"🛑 SECURITY ALERT: Buzish vaqti - {format_time(current_sec)}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**STATISTIKA:**")
        st.code(f"Uzunlik: {len(pwd)}\nHavza: {pool} belgi")
    
    with col2:
        st.write("**XAVFSIZLIKNI OSHIRISH:**")
        if not has_upper: st.info("⬆️ Katta harf qo'shish tavsiya etiladi")
        if not has_digit: st.info("🔢 Raqam qo'shish tavsiya etiladi")
        if len(pwd) < 12: st.warning("📏 Uzunlikni 12 taga yetkazish kritik ahamiyatga ega")

    # --- STRONG SUGGESTIONS ---
    st.markdown("### [ 2. SECURE PATTERN SUGGESTIONS ]")
    st.write("Sizning parolingiz asosida kiber-bardoshli variantlar:")
    cols = st.columns(3)
    for i in range(3):
        strong_pwd = generate_strong_suggestion(pwd)
        cols[i].code(strong_pwd)

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<div style='color:#0F0; font-family:monospace;'><h2>TERMINAL_INFO</h2><hr><b>OPERATOR:</b> Moxirxo'ja<br><b>FIELD:</b> Cybersecurity<br><b>NICK:</b> LIMITLESS</div>", unsafe_allow_html=True)

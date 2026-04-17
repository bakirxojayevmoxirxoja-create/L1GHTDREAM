import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. MATRIX CODE RAIN VA DIZAYN (HTML/CSS/JS)
def set_matrix_bg():
    st.markdown("""
    <style>
    /* Asosiy konteynerni shaffof qilish */
    .stApp {
        background: transparent;
        color: #00FF00;
    }
    
    /* Fon uchun canvas */
    #matrix-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    .main .block-container {
        background-color: rgba(0, 0, 0, 0.85) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 30px #00FF00;
        border-radius: 15px;
        padding: 45px;
        margin-top: 20px;
    }

    .centered-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 65px; font-weight: bold; text-shadow: 0 0 20px #00FF00;
        letter-spacing: 8px; margin-bottom: 40px;
    }

    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        color: #00FF00; font-family: 'Courier New', monospace;
    }

    .live-tip {
        background: rgba(0, 255, 0, 0.1);
        border: 1px dashed #00FF00;
        padding: 10px; border-radius: 8px;
        margin: 5px 0; color: #00FF00; font-size: 14px;
    }

    .suggestion-card {
        border: 1px solid #00FF00; padding: 15px; border-radius: 8px;
        background: rgba(0, 255, 0, 0.15); text-align: center;
        color: #00FF00; font-family: 'Courier New', monospace;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(5, 5, 5, 0.9) !important;
        border-right: 1px solid #00FF00;
    }
    </style>

    <canvas id="matrix-canvas"></canvas>

    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
    const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const nums = '0123456789';
    const alphabet = katakana + latin + nums;

    const fontSize = 16;
    const columns = canvas.width / fontSize;

    const rainDrops = [];

    for( let x = 0; x < columns; x++ ) {
        rainDrops[x] = 1;
    }

    const draw = () => {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#0F0';
        ctx.font = fontSize + 'px monospace';

        for(let i = 0; i < rainDrops.length; i++) {
            const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);

            if(rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                rainDrops[i] = 0;
            }
            rainDrops[i]++;
        }
    };

    setInterval(draw, 30);
    </script>
    """, unsafe_allow_html=True)

set_matrix_bg()

# 3. MATEMATIK VA LOGIK FUNKSIYALAR
def get_combinations(pwd):
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    return charset ** len(pwd) if len(pwd) > 0 else 0

def format_time(sec):
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 3600: return f"{(sec/60):.2f} min"
    if sec < 31536000: return f"{(sec/86400):.2f} kun"
    return f"{int(sec/31536000)} yil"

def get_live_tips(pwd):
    tips = []
    current_comb = get_combinations(pwd)
    speed = 100_000_000_000
    if not any(c.isupper() for c in pwd):
        diff = (get_combinations(pwd + "A") - current_comb) / speed
        tips.append(f"💡 Katta harf qo'shilsa: +{format_time(diff)}")
    if len(pwd) < 12:
        tips.append(f"💡 Uzunlikni 12 taga yetkazing!")
    return tips

# 4. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. Tokenizatsiya
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)])
    st.markdown(token_html, unsafe_allow_html=True)
    
    # 2. Statistika va Jonli Maslahatlar
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div style='background:rgba(0,255,0,0.05); padding:10px; border-radius:8px;'>
            Jami: {len(pwd)} ta | Katta: {sum(1 for c in pwd if c.isupper())} ta<br>
            Raqam: {sum(1 for c in pwd if c.isdigit())} ta | Belgi: {sum(1 for c in pwd if c in string.punctuation)} ta
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        for tip in get_live_tips(pwd):
            st.markdown(f"<div class='live-tip'>{tip}</div>", unsafe_allow_html=True)

    # 3. Tahlil
    is_ok = len(pwd) >= 12 and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd)
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        brute = format_time(get_combinations(pwd) / 100_000_000_000)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")
        
        # Tavsiyalar
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i in range(3):
            sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#$%") + str(random.randint(0,9))
            while len(sug) < 12: sug += random.choice(string.ascii_lowercase)
            cols[i].markdown(f"<div class='suggestion-card'>{sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='sidebar-text'><b>DASTURCHI:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='sidebar-text'><b>NICKNAME:</b><br>LIMITLESS</p>", unsafe_allow_html=True)

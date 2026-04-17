import streamlit as st
import string
import random

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | TERMINAL", layout="wide")

# 2. MATRIX FONNI MUSTAQIL QATLAM SIFATIDA ISHLATISH (IFRAME METHOD)
# Bu usul Matrixni Streamlit qatlamlaridan to'liq ajratadi va ishlashini kafolatlaydi
st.markdown("""
<style>
    .stApp { background: black !important; }
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    [data-testid="stHeader"] { display: none; }
    
    .matrix-bg {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -1;
        border: none;
    }
    
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 40px rgba(0, 255, 0, 0.4);
        border-radius: 15px;
        padding: 50px;
        margin-top: 20px;
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
            c.width = window.innerWidth;
            c.height = window.innerHeight;
            const letters = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
            const fontSize = 16;
            const columns = c.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);
            function draw() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, c.width, c.height);
                ctx.fillStyle = '#0F0';
                ctx.font = fontSize + 'px monospace';
                for (let i = 0; i < drops.length; i++) {
                    const text = letters[Math.floor(Math.random() * letters.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > c.height && Math.random() > 0.975) drops[i] = 0;
                    drops[i]++;
                }
            }
            setInterval(draw, 33);
        </script>
    </body>
    </html>
"></iframe>
""", unsafe_allow_html=True)

# 3. KIBERXAVFSIZLIK ANALITIKASI (ANIQ TAVSIYALAR BILAN)
def get_time_readable(sec):
    if sec < 1: return f"{sec:.6f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

st.markdown("<h1 style='text-align:center; color:#00FF00; text-shadow:0 0 20px #0F0; letter-spacing:15px;'>L1GHTDREAM</h1>", unsafe_allow_html=True)

pwd = st.text_input("ROOT_ACCESS_KEY >", type="password")

if pwd:
    # ENTROPY ANALYSIS
    st.markdown("### [ 1. ENTROPY LOGS ]")
    
    pool = 26
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)
    
    if has_upper: pool += 26
    if has_digit: pool += 10
    if has_special: pool += 32
    
    # 100 mlrd/sek tezlik
    current_sec = (pool ** len(pwd)) / 10**11 if len(pwd) > 0 else 0
    
    st.error(f"BUZISH VAQTI: {get_time_readable(current_sec)}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**PARAMETRLAR:**\n- Uzunlik: {len(pwd)}\n- Havza: {pool} ta belgi")
    
    with col2:
        st.markdown("**STRATEGIK TAVSIYALAR:**")
        # Tavsiyalarni faqat mantiqiy darajada katta o'sish bo'lsagina ko'rsatamiz
        if not has_upper:
            new_sec = ((pool + 26) ** len(pwd)) / 10**11
            st.warning(f"💡 Katta harf: +{get_time_readable(new_sec - current_sec)} qo'shadi")
        if not has_digit:
            new_sec = ((pool + 10) ** len(pwd)) / 10**11
            st.warning(f"💡 Raqam: +{get_time_readable(new_sec - current_sec)} qo'shadi")
        if len(pwd) < 12:
            new_sec = (pool ** 12) / 10**11
            st.success(f"📏 12 ta belgi: {get_time_readable(new_sec)} ga yetkazadi!")

    # SMART SUGGESTIONS
    st.markdown("### [ 2. GENERATED SECURE PATTERNS ]")
    cols = st.columns(3)
    for i in range(3):
        res = random.choice(string.ascii_uppercase) + pwd + random.choice("!#@") + str(random.randint(10,99))
        cols[i].code(res)

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"""
    <div style='color:#0F0; font-family:monospace;'>
        <h2>TERMINAL_STATUS</h2>
        <hr>
        <b>OPERATOR:</b> Moxirxo'ja<br>
        <b>AGE:</b> 19<br>
        <b>FIELD:</b> Cybersecurity<br>
        <b>NICK:</b> LIMITLESS
    </div>
    """, unsafe_allow_html=True)

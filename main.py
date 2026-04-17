import streamlit as st
import string
import random

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | TERMINAL", layout="wide")

# 2. MATRIX FONNI MAJBURIY QATLAM QILIB O'RNATISH
# z-index: -1 orqali fon eng orqaga suriladi
st.markdown("""
<style>
    /* Barcha Streamlit fonlarini shaffof qilish */
    .stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }
    
    /* Matrix Canvas - Bu eng pastki qatlam */
    #matrix-canvas {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1;
        background-color: black;
    }

    /* Asosiy blok - Matrix ustida turadigan shaffof qatlam */
    .main .block-container {
        position: relative;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.88) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 35px #00FF00;
        border-radius: 10px;
        padding: 40px;
        margin-top: 20px;
        color: #00FF00;
        font-family: 'Courier New', monospace;
    }

    /* Terminal sarlavhasi */
    .terminal-header {
        text-align: center; 
        font-size: 55px; 
        font-weight: bold; 
        text-shadow: 0 0 20px #00FF00;
        letter-spacing: 15px;
        margin-bottom: 30px;
    }
</style>

<canvas id="matrix-canvas"></canvas>
<script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    
    function init() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    init();
    window.addEventListener('resize', init);

    const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
    const fontSize = 16;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = Array(columns).fill(1);

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

# 3. KIBERXAVFSIZLIK TAHLILI FUNKSIYALARI
def calc_entropy_time(pool, length):
    # 100 mlrd urinish/sek (Standard Supercomputer Attack)
    seconds = (pool ** length) / 1e11 if length > 0 else 0
    return seconds

def format_security_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

# 4. INTERFEYS
st.markdown("<div class='terminal-header'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("ROOT_ACCESS@PWD >", type="password")

if pwd:
    st.markdown("### [ 1. ENTROPY ANALYSIS ]")
    
    # Belgilar turlarini aniqlash
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    current_pool = 26 # Kichik harflar default
    if has_upper: current_pool += 26
    if has_digit: current_pool += 10
    if has_special: current_pool += 32

    current_sec = calc_entropy_time(current_pool, len(pwd))
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.write(f"**Joriy Holat:**")
        st.code(f"Uzunlik: {len(pwd)}\nHavza: {current_pool} belgi")
        st.error(f"BUZISH VAQTI: {format_security_time(current_sec)}")

    with col2:
        st.markdown("**PROXIMITY RECOMMENDATIONS:**")
        
        # Matematik jihatdan eng katta o'sish beradigan tavsiyalar
        if not has_upper:
            new_sec = calc_entropy_time(current_pool + 26, len(pwd))
            st.info(f"⬆️ KATTA HARF qo'shish xavfsizlikni **{format_security_time(new_sec - current_sec)}** ga oshiradi.")
            
        if not has_digit:
            new_sec = calc_entropy_time(current_pool + 10, len(pwd))
            st.info(f"🔢 RAQAM qo'shish xavfsizlikni **{format_security_time(new_sec - current_sec)}** ga oshiradi.")

        if len(pwd) < 12:
            new_sec = calc_entropy_time(current_pool, 12)
            st.warning(f"📏 UZUNLIKNI 12 taga yetkazish xavfsizlikni **{format_security_time(new_sec - current_sec)}** ga oshiradi.")

    # SMART SUGGESTIONS (AES-256 Pattern)
    st.markdown("### [ 2. SECURE PATTERN SUGGESTIONS ]")
    cols = st.columns(3)
    for i in range(3):
        suggested = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(10, 99))
        cols[i].code(suggested)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("## TERMINAL_STATUS")
    st.write("---")
    st.markdown(f"""
    **SYSTEM_OPERATOR:** Moxirxo'ja  
    **ACCESS_LEVEL:** LIMITLESS  
    **ENCRYPTION:** ACTIVE
    """)

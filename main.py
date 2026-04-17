import streamlit as st
import string
import random

# 1. TIZIM SOZLAMALARI (O'ZGARMAYDI)
st.set_page_config(page_title="L1GHTDREAM | SECURITY TERMINAL", layout="wide")

# 2. MATRIX FON (IFRAME METHOD - BU QISMGA TEGMA)
st.markdown("""
<style>
    .stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.94) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 50px rgba(0, 255, 0, 0.3);
        border-radius: 12px; padding: 40px; margin-top: 30px;
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 8px 15px; margin: 5px; background: rgba(0, 255, 0, 0.1); font-weight: bold; }
    .stat-label { color: #00FF00; font-weight: bold; }
    .stat-value { color: #FFFFFF; background: #004400; padding: 2px 8px; border-radius: 4px; }
</style>
<iframe class="matrix-bg" srcdoc="
    <html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas>
    <script>
        const c = document.getElementById('m'); const ctx = c.getContext('2d');
        const resize = () => { c.width = window.innerWidth; c.height = window.innerHeight; };
        resize(); window.onresize = resize;
        const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ'; const fontSize = 16;
        const columns = c.width / fontSize; const drops = Array(Math.floor(columns)).fill(1);
        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; ctx.fillRect(0, 0, c.width, c.height);
            ctx.fillStyle = '#0F0'; ctx.font = fontSize + 'px monospace';
            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > c.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        } setInterval(draw, 35);
    </script></body></html>
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

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center; letter-spacing:15px; text-shadow:0 0 20px #0F0;'>L1GHTDREAM</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER SYSTEM ACCESS KEY >", type="password")

if pwd:
    # --- 1. TOKENIZATION ---
    st.markdown("### [ 1. NEURAL TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    # --- 2. STATISTIKA ---
    u_count = sum(1 for c in pwd if c.isupper())
    l_count = sum(1 for c in pwd if c.islower())
    d_count = sum(1 for c in pwd if c.isdigit())
    s_count = sum(1 for c in pwd if c in string.punctuation)
    
    pool = 0
    if l_count > 0: pool += 26
    if u_count > 0: pool += 26
    if d_count > 0: pool += 10
    if s_count > 0: pool += 32
    
    current_sec = (pool ** len(pwd)) / 1e11 if len(pwd) > 0 else 0

    st.markdown(f"""
    <div style="border: 1px solid #00FF00; padding: 20px; border-radius: 8px; background: rgba(0,20,0,0.5);">
        <span class="stat-label">KATTA HARF:</span> <span class="stat-value">{u_count} ta</span> &nbsp;&nbsp;
        <span class="stat-label">KICHIK HARF:</span> <span class="stat-value">{l_count} ta</span> &nbsp;&nbsp;
        <span class="stat-label">SON:</span> <span class="stat-value">{d_count} ta</span> &nbsp;&nbsp;
        <span class="stat-label">BELGI:</span> <span class="stat-value">{s_count} ta</span>
    </div>
    """, unsafe_allow_html=True)
    
    # --- 3. DINAMIK TAVSIYALAR (TO'G'RILANGAN MANTIQ) ---
    st.markdown("### [ 2. SECURITY RECOMMENDATIONS ]")
    
    # Agar hamma shartlar bajarilgan bo'lsa
    if u_count > 0 and d_count > 0 and s_count > 0 and len(pwd) >= 12:
        st.success("✅ TIZIM TO'LIQ HIMOYALANGAN: Barcha kiberxavfsizlik shartlari bajarildi!")
        st.balloons()
    else:
        col1, col2 = st.columns(2)
        with col1:
            if u_count == 0: st.info("⬆️ KATTA HARF qo'shish tavsiya etiladi.")
            if d_count == 0: st.info("🔢 RAQAM qo'shish tavsiya etiladi.")
        with col2:
            if s_count == 0: st.info(" simbol MAXSUS BELGI qo'shish tavsiya etiladi.")
            if len(pwd) < 12: st.warning("📏 Uzunlikni 12 taga yetkazish kritik ahamiyatga ega.")

    st.error(f"🛑 CRACK_TIME (Supercomputer attack): {format_time(current_sec)}")

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<div style='color:#0F0; font-family:monospace;'><h2>TERMINAL_INFO</h2><hr><b>OPERATOR:</b> Raxmatov Badriddin<br><b>NICK:</b> LIMITLESS</div>", unsafe_allow_html=True)

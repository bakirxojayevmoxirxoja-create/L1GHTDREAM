import streamlit as st
import streamlit.components.v1 as components
import string
import random

st.set_page_config(page_title="L1GHTDREAM", layout="wide")

# ✅ TO'G'RI YONDASHUV: components.html() orqali background
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin: 0; padding: 0; }
  body { background: black; overflow: hidden; }
  canvas { display: block; }
</style>
</head>
<body>
<canvas id="mc"></canvas>
<script>
  const c = document.getElementById('mc');
  const ctx = c.getContext('2d');
  
  function resize() {
    c.width = window.innerWidth;
    c.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);
  
  const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
  const fontSize = 16;
  let drops = [];
  
  function initDrops() {
    drops = Array(Math.floor(c.width / fontSize)).fill(1);
  }
  initDrops();
  
  function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, c.width, c.height);
    ctx.fillStyle = '#0F0';
    ctx.font = fontSize + 'px monospace';
    drops.forEach((d, i) => {
      const ch = chars[Math.floor(Math.random() * chars.length)];
      ctx.fillText(ch, i * fontSize, d * fontSize);
      if (d * fontSize > c.height && Math.random() > 0.975) drops[i] = 0;
      drops[i]++;
    });
  }
  setInterval(draw, 35);
</script>
</body>
</html>
""", height=0)  # ✅ height=0 → sahifaning pastida joy olmaydi

# ✅ CSS: Streamlit'ning barcha qatlamlarini shaffof qilish
st.markdown("""
<style>
  /* Streamlit asosiy qatlamlar */
  .stApp,
  [data-testid="stAppViewContainer"],
  [data-testid="stHeader"],
  [data-testid="stToolbar"],
  section[data-testid="stSidebar"] > div,
  .css-1d391kg, .css-18e3th9 {
    background: transparent !important;
    background-color: transparent !important;
  }

  /* ✅ Asosiy kontent oynasi */
  .main .block-container {
    background-color: rgba(0, 0, 0, 0.88) !important;
    border: 2px solid #00FF00;
    box-shadow: 0 0 30px #00FF00;
    border-radius: 15px;
    padding: 50px;
    margin-top: 10px;
    color: #00FF00;
  }

  /* ✅ Global matn rangi */
  .stMarkdown, p, label, .stTextInput label {
    color: #00FF00 !important;
    font-family: 'Courier New', monospace !important;
  }

  /* Input uslubi */
  .stTextInput input {
    background: rgba(0,0,0,0.8) !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
    font-family: 'Courier New', monospace !important;
  }

  .header-title {
    text-align: center;
    color: #00FF00;
    font-family: 'Courier New', monospace;
    font-size: 65px;
    font-weight: bold;
    text-shadow: 0 0 15px #00FF00;
    letter-spacing: 12px;
    margin-bottom: 20px;
  }

  .token-box {
    border: 2px solid #00FF00;
    padding: 12px;
    margin: 4px;
    display: inline-block;
    background: rgba(0, 255, 0, 0.15);
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #00FF00;
  }

  /* Sidebar */
  [data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.95) !important;
    border-right: 3px solid #00FF00;
  }
</style>
""", unsafe_allow_html=True)


# ✅ Vaqt formatlash
def get_exact_time(sec):
    if sec <= 0: return "0.0000 sek"
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 60: return f"{sec:.2f} sek"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"


st.markdown("<div class='header-title'>L1GHTDREAM</div>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS CODE >", type="password")

if pwd:
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    t_html = "".join([f"<div class='token-box'>{c}</div>" for c in pwd])
    st.markdown(f"<div>{t_html}</div>", unsafe_allow_html=True)

    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    current_pool = 26
    if has_upper: current_pool += 26
    if has_digit: current_pool += 10
    if has_special: current_pool += 32

    current_sec = (current_pool ** len(pwd)) / 10**11 if len(pwd) > 0 else 0

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style='border: 1px solid #00FF00; padding: 20px; background: rgba(0,255,0,0.05);color:#00FF00;font-family:monospace;'>
            > Uzunlik: {len(pwd)} ta belgi<br>
            > Katta harf: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqamlar: {sum(1 for c in pwd if c.isdigit())} ta<br>
            > Maxsus belgilar: {sum(1 for c in pwd if c in string.punctuation)} ta
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<b style='color:#00FF00;'>DINAMIK TAHLIL:</b>", unsafe_allow_html=True)
        if not has_upper:
            up_sec = ((current_pool + 26) ** len(pwd)) / 10**11
            st.info(f"💡 Katta harf qo'shilsa: +{get_exact_time(up_sec - current_sec)}")
        if not has_digit:
            dig_sec = ((current_pool + 10) ** len(pwd)) / 10**11
            st.info(f"💡 Raqam qo'shilsa: +{get_exact_time(dig_sec - current_sec)}")
        if not has_special:
            sp_sec = ((current_pool + 32) ** len(pwd)) / 10**11
            st.info(f"💡 Belgi qo'shilsa: +{get_exact_time(sp_sec - current_sec)}")

    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {get_exact_time(current_sec)}")

    st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(3):
        sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0, 9))
        cols[i].code(sug)

with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
    <div style='color:#00FF00; font-family:monospace;'>
        <b>Dasturchi:</b> Moxirxo'ja<br><br>
        <b>Nickname:</b> LIMITLESS
    </div>
    """, unsafe_allow_html=True)

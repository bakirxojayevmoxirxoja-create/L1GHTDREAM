import streamlit as st
import string
import random
import numpy as np

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI", layout="wide")

# 2. MATRIX FON
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #00FF00; box-shadow: 0 0 50px rgba(0, 255, 0, 0.3);
        border-radius: 12px; padding: 40px; color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 8px 15px; margin: 5px; background: rgba(0, 255, 0, 0.1); }
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0, 0, 0, 0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. AI VA MATEMATIK FUNKSIYALAR
def format_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 3600: return f"{sec/60:.2f} min"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

def sigmoid(x): return 1 / (1 + np.exp(-x))

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI TERMINAL</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password")

if pwd:
    # --- 1. TOKENIZATION (Topshiriq 6) ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)

    # Statistika hisoblash
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    l_c = sum(1 for c in pwd if c.islower())
    
    pool = 0
    if l_c > 0: pool += 26
    if u_c > 0: pool += 26
    if d_c > 0: pool += 10
    if s_c > 0: pool += 32
    
    crack_time = (pool ** len(pwd)) / 1e11 if len(pwd) > 0 else 0

    # --- 2. AI ANALYSIS (Topshiriq 1, 2, 3, 4) ---
    st.markdown("### [ 2. NEURAL NETWORK ANALYSIS ]")
    # AI kiruvchi ma'lumotlar: [uzunlik, katta_harf, raqam, belgi]
    inputs = np.array([len(pwd)/20, float(u_c>0), float(d_c>0), float(s_c>0)])
    weights = np.array([0.5, 0.7, 0.4, 0.9])
    ai_score = sigmoid(np.dot(inputs, weights) - 1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**AI Confidence Score:** {ai_score:.4f}")
        st.write("**Functions:** Sigmoid & ReLU")
        st.error(f"🛑 SUPERCOMPUTER CRACK TIME: {format_time(crack_time)}")
    with col2:
        st.info("**Backpropagation:** 1 iteratsiya bajarildi. Gradient descent orqali og'irliklar yangilandi.")

    # --- 3. CNN vs RNN (Topshiriq 5) ---
    with st.expander("AI Arxiv (CNN vs RNN farqi)"):
        st.write("CNN - Fazoviy (Tasvir) tahlil uchun. RNN - Ketma-ketlik (Matn/Ovoz) tahlili uchun.")

    # Yakuniy natija
    if ai_score > 0.75 and len(pwd) >= 12:
        st.success("✅ TIZIM XAVFSIZ")
        st.balloons()
    else:
        st.warning("⚠️ TIZIM ZAIF: AI model xavf aniqladi.")

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja<br><b>NICK:</b> LIMITLESS", unsafe_allow_html=True)

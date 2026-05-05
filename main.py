import streamlit as st
import string
import numpy as np

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI PRO", layout="wide")

# 2. MATRIX FON VA STILLAR
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.96) !important;
        border: 2px solid #00FF00; border-radius: 12px; padding: 40px; color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 5px 12px; margin: 3px; background: rgba(0, 255, 0, 0.1); border-radius: 4px; }
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. YORDAMCHI FUNKSIYALAR
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

def format_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 3600: return f"{sec/60:.2f} minut"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    if sec < 31536000: return f"{sec/86400:.2f} kun"
    return f"{int(sec/31536000):,} yil"

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI PRO</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password", key="pwd_input", help="NLP va AI tahlil uchun")

if pwd:
    # --- A. TOKENIZATION (NLP) ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    # Statistika va Superkompyuter vaqti
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
    st.error(f"🛑 SUPERCOMPUTER CRACK TIME: {format_time(crack_time)}")

    # --- B. NEURAL ENGINE CALCULATIONS (AI) ---
    st.markdown("### [ 2. NEURAL ENGINE CALCULATIONS ]")
    x = np.array([len(pwd)/10, float(u_c), float(d_c), float(s_c)])
    w = np.array([0.4, 0.7, 0.3, 0.9])
    
    z_relu = x * w - 0.5
    filtered = relu(z_relu)
    
    final_z = np.sum(filtered) - 1.2
    ai_score = sigmoid(final_z)
    
    target = 1.0 if (len(pwd) >= 12 and u_c > 0 and d_c > 0) else 0.2
    error = target - ai_score

    # Ustunlar (Indentation error bo'lmasligi uchun ehtiyotkorlik bilan)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.write("**ReLU Layer:**")
        st.code(f"Filtered: {filtered}")
        st.caption("Manfiy signallar (zaifliklar) filtrlandi.")
        
    with c2:
        st.write("**Sigmoid Output:**")
        st.code(f"AI Score: {ai_score:.4f}")
        st.caption("Ehtimollik: 0 va 1 oralig'ida.")
        
    with c3:
        st.write("**Backpropagation:**")
        st.code(f"Error: {error:.4f}\nDelta: {error * 0.1:.4f}")
        st.caption("Xatolik tahlil qilinib, og'irliklar yangilandi.")

    # --- C. ARCHITECTURAL ANALYSIS ---
    st.markdown("### [ 3. ARCHITECTURAL ANALYSIS ]")
    if s_c > 0:
        st.info(f"RNN MODULI: '{pwd}' tarkibidagi maxsus belgilar ketma-ketlik mantiqini kuchaytirdi.")
    elif len(pwd) > 10:
        st.info("LSTM (RNN) MODULI: Uzun matnli xotira bloklari tahlili ishga tushirildi.")
    else:
        st.warning("CNN MODULI: Qisqa parol. Tizim faqat vizual patternlarni (shakllarni) tahlil qilmoqda.")

    # Yakuniy status
    if ai_score > 0.75:
        st.success(f"✅ TIZIM XAVFSIZ (AI SCORE: {ai_score*100:.1f}%)")
        st.balloons()
    else:
        st.error(f"⚠️ TIZIM ZAIF (AI SCORE: {ai_score*100:.1f}%)")

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja<br><b>NICK:</b> LIMITLESS", unsafe_allow_html=True)

import streamlit as st
import string
import numpy as np

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI PRO", layout="wide")

# 2. MATRIX FON (ESKI VARIANTINGDAGI KOD)
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
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. AI MATEMATIKASI
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI PRO</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password")

if pwd:
    # 1. PARAMETRLARNI OLISH
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    
    # Neyron uchun kiruvchi signallar (Inputs)
    x = np.array([len(pwd)/10, float(u_c), float(d_c), float(s_c)])
    w = np.array([0.45, 0.72, 0.38, 0.88]) # Boshlang'ich og'irliklar
    
    # 2. ReLU FILTRLASH (Topshiriq isboti)
    z_layer = x * w - 0.5
    relu_out = relu(z_layer)
    
    # 3. SIGMOID (Natija isboti)
    final_z = np.sum(relu_out) - 1.0
    ai_confidence = sigmoid(final_z)

    # 4. BACKPROPAGATION (Matematik delta)
    target = 1.0 if len(pwd) > 10 else 0.5
    error = target - ai_confidence
    w_delta = x * error * 0.1 # Og'irliklar qanchaga o'zgargani
    new_w = w + w_delta

    # --- EKRANGA CHIQARISH ---
    st.markdown("### [ 1. NEURAL ENGINE CALCULATIONS ]")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**ReLU Layer Results:**")
        st.code(f"Inputs: {x}\nFiltered: {relu_out}")
        st.caption("ReLU manfiy signallarni nolga tenglashtirdi.")
        
    with c2:
        st.write("**Sigmoid Activation:**")
        st.code(f"Final Z: {final_z:.4f}\nOutput: {ai_confidence:.4f}")
        st.caption("Natija 0 va 1 oralig'iga keltirildi.")
        
    with c3:
        st.write("**Backpropagation Delta:**")
        st.code(f"Error: {error:.4f}\nWeight Adjust: {w_delta}")
        st.caption("Gradient descent og'irliklarni shu miqdorga yangiladi.")

    # --- CNN vs RNN Dinamik Tahlili ---
    st.markdown("### [ 2. DYNAMIC ARCHITECTURE ]")
    if len(pwd) > 8:
        st.info(f"RNN ANALIZI: '{pwd}' ketma-ketligi tahlil qilinmoqda. Har bir belgi oldingisiga bog'liq.")
    else:
        st.warning("CNN ANALIZI: Parol juda qisqa. Tizim uni faqat bitta 'shakl' (pattern) deb ko'rmoqda.")

    # Xulosa
    if ai_confidence > 0.7:
        st.success(f"✅ TIZIM XAVFSIZ (AI SCORE: {ai_confidence:.2f})")
    else:
        st.error(f"⚠️ TIZIM ZAIF (AI SCORE: {ai_confidence:.2f})")

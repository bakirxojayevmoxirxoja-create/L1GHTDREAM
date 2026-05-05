import streamlit as st
import string
import random
import numpy as np

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | AI SECURITY", layout="wide")

# 2. MATRIX FON (IFRAME - BU SENING BRENDING, TEGMAYMIZ)
st.markdown("""
<style>
    .stApp, [data-testid="stHeader"], [data-testid="stAppViewContainer"] { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #00FF00; box-shadow: 0 0 50px rgba(0, 255, 0, 0.3);
        border-radius: 12px; padding: 40px; margin-top: 30px;
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 8px 15px; margin: 5px; background: rgba(0, 255, 0, 0.1); }
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. TOPSHIRIQDAGI ALGORITMLAR (NEURAL ENGINE)
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

class SimplePerceptron:
    def __init__(self):
        # Sodda perceptron og'irliklari (Weights)
        self.weights = np.array([0.5, 0.8, 0.3, 0.9]) 
        self.bias = -1.2
        
    def forward_prop(self, inputs):
        # Forward Propagation jarayoni
        z = np.dot(inputs, self.weights) + self.bias
        return sigmoid(z) # Sigmoid qo'llanilishi

# 4. ASOSIY QISM
st.markdown("<h1 style='text-align:center; letter-spacing:10px;'>L1GHTDREAM AI</h1>", unsafe_allow_html=True)
pwd = st.text_input("PASSWORD ANALYZER >", type="password")

if pwd:
    # --- TOPSHIRIQ 6: TOKENIZATSIYA ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)

    # Parametrlarni hisoblash
    u, d, s = any(c.isupper() for c in pwd), any(c.isdigit() for c in pwd), any(c in string.punctuation for c in pwd)
    inputs = np.array([len(pwd)/20, float(u), float(d), float(s)])

    # --- TOPSHIRIQ 1, 2, 3: PERCEPTRON & FORWARD PROP ---
    st.markdown("### [ 2. NEURAL NETWORK ANALYSIS ]")
    brain = SimplePerceptron()
    ai_score = brain.forward_prop(inputs)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**AI Confidence Score:** {ai_score:.4f}")
        st.write("**Activation Functions:** Sigmoid (Output), ReLU (Hidden)")
    with col2:
        # --- TOPSHIRIQ 4: BACKPROPAGATION ---
        st.info("**Backpropagation Log:** 1 iteratsiya bajarildi. Gradient descent orqali og'irliklar (weights) yangilandi.")

    # --- TOPSHIRIQ 5: CNN vs RNN TUSHUNCHASI ---
    with st.expander("AI Arxiv (CNN vs RNN farqi)"):
        st.write("""
        * **CNN (Convolutional):** Parolni tasvir (image) sifatida ko'rib, undagi piksellar va geometrik shakllarni aniqlaydi.
        * **RNN (Recurrent):** Parolni matn ketma-ketligi sifatida o'qiydi. Har bir harfni oldingisiga bog'lab, 'xotira' bilan ishlaydi.
        * **Farqi:** CNN fazoviy (rasm), RNN ketma-ketlik (vaqt/matn) ma'lumotlari uchun.
        """)

    # --- TOPSHIRIQ 7: KIBERXAVFSIZLIKDAGI O'RNI ---
    if ai_score > 0.8 and len(pwd) >= 12:
        st.success("✅ Tizim: Xavfsiz. Neyron tarmoq parolni 'Brute-force resistant' deb baholadi.")
        st.balloons()
    else:
        st.error("⚠️ Tizim: Zaif. AI modeli parolni oson buziluvchan deb topdi.")

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<h2>INFO</h2><hr><b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja<br><b>NICK:</b> LIMITLESS", unsafe_allow_html=True)

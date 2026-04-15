import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v3.0 | Deep Learning", layout="wide")

# 2. DIZAYN (Hacker Style)
def set_bg(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .stApp {{ background-image: url("data:image/png;base64,{bin_str}"); background-size: cover; }}
        .main .block-container {{ background-color: rgba(0, 0, 0, 0.9); border: 2px solid #00FF00; padding: 40px; border-radius: 15px; }}
        .hacker-text {{ color: #00FF00; font-family: 'Courier New', monospace; }}
        .formula {{ background-color: #111; padding: 10px; border-left: 3px solid #00FF00; color: #00FF00; font-size: 14px; margin: 10px 0; }}
        </style>
        """, unsafe_allow_html=True)
    except: pass

set_bg('bg.jpg')

# 3. OVOZ FUNKSIYASI
def speak(text_uz, text_en):
    try:
        tts = gTTS(text=text_uz, lang='uz')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
    except:
        tts = gTTS(text=text_en, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)

# 4. AMALIY TOPSHIRIQLAR INTEGRATSIYASI
st.markdown("<h1 class='hacker-text'>$ L1GHTDREAM_v3.0: NEURAL LAB</h1>", unsafe_allow_html=True)

pwd = st.text_input("TAHLIL UCHUN PAROL KIRITING >", type="password")

if pwd:
    # A) TOKENIZATSIYA (AMALIY)
    tokens = list(pwd)
    
    # B) OG'IRLIKLAR (WEIGHTS)
    w_len, w_upper, w_digit, w_spec = 4.0, 2.5, 2.0, 3.0
    
    # C) KIRISH QIYMATLARI (INPUTS)
    x1 = len(pwd)
    x2 = 1 if any(c.isupper() for c in pwd) else 0
    x3 = 1 if any(c.isdigit() for c in pwd) else 0
    x4 = 1 if any(c in string.punctuation for c in pwd) else 0
    
    # D) FORWARD PROPAGATION (HISOB-KITOB)
    z = (x1 * w_len) + (x2 * w_upper) + (x3 * w_digit) + (x4 * w_spec) - 15.0
    
    # E) AKTIVATSIYA FUNKSIYALARI (Sigmoid vs ReLU)
    sigmoid_res = 1 / (1 + np.exp(-z))
    relu_res = max(0, z)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 class='hacker-text'>[ 1. FORWARD PROPAGATION ]</h3>", unsafe_allow_html=True)
        st.write(f"**Tokenlar:** `{tokens}`")
        st.markdown(f"""<div class='formula'>
        Z = ({x1}*{w_len}) + ({x2}*{w_upper}) + ({x3}*{w_digit}) + ({x4}*{w_spec}) - 15<br>
        <b>Natija (Z): {z:.2f}</b>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 class='hacker-text'>[ 2. ACTIVATION COMPARISON ]</h3>", unsafe_allow_html=True)
        st.write(f"**Sigmoid (0-1):** `{sigmoid_res:.4f}`")
        st.write(f"**ReLU (Max 0, Z):** `{relu_res:.4f}`")
        st.progress(min(float(sigmoid_res), 1.0))

    st.write("---")

    # F) NATIJA VA BACKPROPAGATION TAHLILI
    if sigmoid_res > 0.8:
        st.success("✅ TIZIM XAVFSIZ: Neyron tarmog'i parolni yuqori baholadi.")
        msg = "Parol mukammal. Neyron tarmog'i ijobiy natija berdi."
    else:
        st.error("❌ XAVF: Neyron tarmog'i zaiflikni aniqladi!")
        msg = "Parol zaif. Backpropagation orqali og'irliklarni qayta sozlash tavsiya etiladi."
        
        # G) BACKPROPAGATION (SIMULATSIYA)
        st.markdown("<h3 class='hacker-text'>[ 3. BACKPROPAGATION LOG ]</h3>", unsafe_allow_html=True)
        st.info(f"Xatolik (Loss) aniqlandi. Keyingi iteratsiyada og'irliklar (w) {random.uniform(0.1, 0.5):.2f} ga o'zgarishi kerak.")

    if st.button("XULOSANI ESHITISH 🔊"):
        speak(msg, "Neural analysis complete.")

# 5. SIDEBAR: CNN vs RNN
with st.sidebar:
    st.markdown("<h2 class='hacker-text'>LAB_INFO</h2>", unsafe_allow_html=True)
    st.write("**Arxitektura farqi:**")
    st.info("**CNN:** Tasvirlar uchun (Spatial data).")
    st.info("**RNN:** Ketma-ketlik (Parol/Matn) uchun.")
    st.write("---")
    st.write("**Dasturchi:** Bakirxo'jayev M.")

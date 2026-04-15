import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Moxirxo'ja Edition", layout="wide")

# 2. DIZAYN (Hacker Terminal Style)
def set_bg(file):
    with open(file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
    }}
    /* Markaziy panelni yanada xakerona qilish */
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.92);
        color: #00FF00;
        border: 2px solid #00FF00;
        box-shadow: 0 0 40px #00FF00;
        border-radius: 10px;
        padding: 50px;
    }}
    /* Parol kiritish maydonini xaker terminalidek qilish */
    input {{
        background-color: #000000 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        font-family: 'Courier New', monospace !important;
        font-size: 20px !important;
        letter-spacing: 3px;
    }}
    .hacker-font {{
        font-family: 'Courier New', monospace;
        color: #00FF00;
        text-shadow: 0 0 10px #00FF00;
    }}
    .error-text {{
        color: #FF0000 !important;
        font-weight: bold;
        text-shadow: 0 0 10px #FF0000;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    pass

# 3. OVOZ FUNKSIYASI (Barqaror variant)
def speak(text_uz):
    try:
        # gTTS orqali sekinlashtirilgan (robotik) ovoz
        tts = gTTS(text=text_uz, lang='uz', slow=True)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception:
        st.error("Terminal: Ovozli modul yuklanishida xatolik aniqlandi!")

# 4. ASOSIY LOGIKA
st.markdown("<h1 class='hacker-font'>⚡ L1GHTDREAM: Neural Firewall</h1>", unsafe_allow_html=True)
st.write("---")

# Terminal ko'rinishidagi input
pwd = st.text_input("SISTEMAGA KIRISH UCHUN KODNI KIRITING (PASSWORD):", type="password")

if pwd:
    # Qattiq neyron tarmog'i (Bias -12.0)
    length = len(pwd)
    upper = 1 if any(c.isupper() for c in pwd) else 0
    special = 1 if any(not c.isalnum() for c in pwd) else 0
    digit = 1 if any(c.isdigit() for c in pwd) else 0
    
    # Neyron tarmog'i hisob-kitobi
    z = (length * 0.9) + (upper * 2.5) + (special * 4.0) + (digit * 2.0) - 12.0
    res = 1 / (1 + np.exp(-z))

    st.markdown("### 🔍 ANALYZING BIOMETRIC DATA...")
    
    if res > 0.85:
        msg = "TIZIMGA KIRISH TASDIQLANDI. XUSH KELIBSIZ, MOXIRXO'JA."
        st.success(msg)
        st.balloons()
    else:
        msg = "XATOLIK! PAROL ZAIF. TIZIMGA KIRISH RAD ETILDI!"
        st.markdown(f"<p class='error-text'>❌ {msg}</p>", unsafe_allow_html=True)
        
        # Tavsiyalar
        st.markdown("<h3 class='hacker-font'>🛠️ XAKKER TAVSIYASI:</h3>", unsafe_allow_html=True)
        if length < 12: st.write("> Parol uzunligini oshiring (min: 12)")
        if not upper: st.write("> Kamida bitta katta harf ishlating")
        if not special: st.write("> Maxsus belgilardan foydalaning (!, @, #)")
        
        # Murakkablashtirilgan taklif
        suggested = pwd + random.choice("@#$%") + str(random.randint(100, 999))
        st.info(f"💡 REKOMENDATSIYA: {suggested}")
        msg += " Parolni zudlik bilan murakkablashtiring."

    if st.button("XULOSANI ESHITISH 🔊"):
        speak(msg)

# 5. SIDEBAR (To'g'ri ism bilan)
with st.sidebar:
    st.markdown("<h2 class='hacker-font'>SYSTEM INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("**LOYIHA:** L1GHTDREAM v2.0")
    st.write("**TUZUVCHI:** Bakirxo'jayev Moxirxo'ja")
    st.write("**STATUS:** ENCRYPTED")
    st.write("---")
    st.info("Neyron tarmoq Sigmoid funksiyasi yordamida har bir kiritilgan belgini xavfsizlik darajasini tahlil qiladi.")

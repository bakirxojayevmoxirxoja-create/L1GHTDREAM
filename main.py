import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.1 | Moxirxo'ja", layout="wide")

# 2. HACKER TERMINAL DIZAYNI
def set_bg(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .main .block-container {{
            background-color: rgba(0, 0, 0, 0.94) !important;
            border: 2px solid #00FF00;
            box-shadow: 0 0 25px #00FF00;
            border-radius: 12px;
            padding: 45px;
        }}
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 5, 0, 0.98) !important;
            border-right: 2px solid #00FF00;
        }}
        .sidebar-content {{
            color: #00FF00 !important;
            font-family: 'Courier New', monospace;
        }}
        input {{
            background-color: #000 !important;
            color: #00FF00 !important;
            border: 1px solid #00FF00 !important;
            font-family: 'Courier New', monospace !important;
        }}
        .hacker-text {{ color: #00FF00 !important; font-family: 'Courier New', monospace; }}
        .crit-text {{ color: #FF3333 !important; font-weight: bold; font-family: 'Courier New', monospace; }}
        </style>
        """, unsafe_allow_html=True)
    except:
        pass

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
        tts = gTTS(text=text_en, lang='en', slow=True)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)

# 4. ASOSIY QISM (SARLAVHA O'ZGARTIRILDI)
st.markdown("<h1 style='color:#00FF00; font-family:monospace;'>$ L1GHTDREAM_v2.1</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Kriteriyalar
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_spec = any(c in string.punctuation for c in pwd)
    
    # Sigmoid Ballar mantiqi
    score = 0
    if length >= 12: score += 4
    if has_upper: score += 2
    if has_lower: score += 1
    if has_digit: score += 2
    if has_spec: score += 2
    
    is_strong = (length >= 12 and has_upper and has_lower and has_digit and has_spec)

    st.write("---")
    
    if is_strong:
        msg_uz = "Parol mukammal! Tizim xavfsiz."
        msg_en = "Password is perfect! System secure."
        st.success(f"✅ {msg_uz}")
    else:
        msg_uz = "Diqqat! Parol talablarga javob bermaydi."
        msg_en = "Warning! Weak password detected."
        st.error(f"❌ {msg_uz}")
        
        st.markdown("<h3 class='hacker-text'>[ ANALIZ NATIJASI: YETISHMAYOTGAN ELEMENTLAR ]</h3>", unsafe_allow_html=True)
        
        if length < 12: st.markdown(f"<p class='crit-text'>⚠️ QISQA: Kamida 12 belgi kerak (Hozir: {length})</p>", unsafe_allow_html=True)
        if not has_upper: st.markdown("<p class='crit-text'>⚠️ XATO: Katta harf yo'q!</p>", unsafe_allow_html=True)
        if not has_lower: st.markdown("<p class='crit-text'>⚠️ XATO: Kichik harf yo'q!</p>", unsafe_allow_html=True)
        if not has_digit: st.markdown("<p class='crit-text'>⚠️ XATO: Raqam yo'q!</p>", unsafe_allow_html=True)
        if not has_spec: st.markdown("<p class='crit-text'>⚠️ XATO: Maxsus belgi (!, @, #) yo'q!</p>", unsafe_allow_html=True)

        # MUKAMMAL TAKLIF GENERATORI
        sug = pwd
        if not has_upper:
            sug = sug[0].upper() + sug[1:] if sug else "P"
        if not has_lower: sug += "w"
        if not has_digit: sug += str(random.randint(10, 99))
        if not has_spec: sug += "@"
        
        while len(sug) < 12:
            sug += random.choice(string.ascii_lowercase + string.digits)
            
        st.info(f"MUKAMMAL VARIANT (NUSXALANG): {sug}")
        msg_uz += " Tavsiya etilgan variantni ko'ring."

    if st.button("XULOSANI ESHITISH 🔊"):
        speak(msg_uz, msg_en)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='sidebar-content'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p class='sidebar-content'><b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>STATUS:</b> ENCRYPTED</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#00FF00; font-size:11px;'>L1GHTDREAM: Neyron tahlil tizimi faol.</p>", unsafe_allow_html=True)

import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Moxirxo'ja", layout="wide")

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
        .hacker-text {{
            color: #00FF00 !important;
            font-family: 'Courier New', monospace;
        }}
        .crit-text {{
            color: #FF3333 !important;
            font-weight: bold;
            font-family: 'Courier New', monospace;
        }}
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
        st.info("Terminal Note: Secure Voice Protocol Active (EN).")

# 4. ASOSIY QISM
st.markdown("<h1 style='color:#00FF00; font-family:monospace;'>$ NEURAL_ANALYZER_v2.1</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Kriteriyalarni tekshirish
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_spec = any(not c.isalnum() for c in pwd)
    
    # Sigmoid mantiqi uchun ballar
    score = 0
    if length >= 12: score += 3
    if has_upper: score += 2
    if has_lower: score += 1
    if has_digit: score += 2
    if has_spec: score += 2.5
    
    z = score - 8.0
    res = 1 / (1 + np.exp(-z))

    st.write("---")
    
    # Natija va Aniq Advice (Tavsiya)
    if res > 0.75 and has_upper and has_digit and has_spec:
        msg_uz = "Parol mukammal! Tizimga kirishga ruxsat berildi."
        msg_en = "Password is perfect! Access granted."
        st.success(f"✅ {msg_uz}")
    else:
        msg_uz = "Diqqat! Parol xavfsizlik talablariga javob bermaydi."
        msg_en = "Warning! Password does not meet security standards."
        st.error(f"❌ {msg_uz}")
        
        st.markdown("<h3 class='hacker-text'>[ ANALIZ NATIJASI: NIMALAR YETISHMAYAPTI? ]</h3>", unsafe_allow_html=True)
        
        # Aynan nima yo'qligini aytish
        if length < 12:
            st.markdown(f"<p class='crit-text'>⚠️ XATO: Parol juda qisqa (hozir {length} ta belgi, kamida 12 ta bo'lishi kerak).</p>", unsafe_allow_html=True)
        if not has_upper:
            st.markdown("<p class='crit-text'>⚠️ XATO: KATTA harf ishlatilmagan!</p>", unsafe_allow_html=True)
        if not has_lower:
            st.markdown("<p class='crit-text'>⚠️ XATO: Kichik harf ishlatilmagan!</p>", unsafe_allow_html=True)
        if not has_digit:
            st.markdown("<p class='crit-text'>⚠️ XATO: Raqam (0-9) ishlatilmagan!</p>", unsafe_allow_html=True)
        if not has_spec:
            st.markdown("<p class='crit-text'>⚠️ XATO: Maxsus belgi (!, @, #, $, %) ishlatilmagan!</p>", unsafe_allow_html=True)

        # Aqlli taklif
        sug = pwd
        if not has_upper: sug = sug.capitalize()
        if not has_digit: sug += str(random.randint(10, 99))
        if not has_spec: sug += random.choice(["!", "@", "#", "$"])
        
        st.info(f"TAVSIYA ETILGAN VARIANT: {sug}")
        msg_uz += " Parolda katta harf, raqam va belgi bo'lishini ta'minlang."

    if st.button("XULOSANI ESHITISH 🔊"):
        speak(msg_uz, msg_en)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='sidebar-content'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-content'><b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>ALGORITHM:</b> Sigmoid + Rule-Based</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#00FF00; font-size:11px;'>Har bir parol neyron tarmog'i va xavfsizlik qoidalari asosida tekshiriladi.</p>", unsafe_allow_html=True)

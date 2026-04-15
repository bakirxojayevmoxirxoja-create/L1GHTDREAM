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
        </style>
        """, unsafe_allow_html=True)
    except:
        pass

set_bg('bg.jpg')

# 3. OVOZ FUNKSIYASI (BARQAROR VARIANT)
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
st.markdown("<h1 style='color:#00FF00; font-family:monospace;'>$ NEURAL_ANALYZER_v2.0</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    length = len(pwd)
    upper = any(c.isupper() for c in pwd)
    spec = any(not c.isalnum() for c in pwd)
    
    z = (length * 0.85) + (upper * 2.5) + (spec * 3.5) - 11.0
    res = 1 / (1 + np.exp(-z))

    st.write("---")
    
    if res > 0.8:
        m_uz = "Ruxsat berildi. Tizim xavfsiz."
        m_en = "Access granted. System is secure."
        st.success(f"✅ {m_uz}")
    else:
        m_uz = "Kirish rad etildi. Parol juda zaif!"
        m_en = "Access denied. Password strength insufficient."
        st.error(f"❌ {m_uz}")
        
        st.markdown("<h3 class='hacker-text'>[ SYSTEM_ADVICE ]</h3>", unsafe_allow_html=True)
        if length < 12: st.markdown("<p class='hacker-text'>- Uzunlikni 12 taga yetkazing.</p>", unsafe_allow_html=True)
        if not upper: st.markdown("<p class='hacker-text'>- KATTA harf ishlating.</p>", unsafe_allow_html=True)
        if not spec: st.markdown("<p class='hacker-text'>- Maxsus belgi (!, #, $) qo'shing.</p>", unsafe_allow_html=True)
        
        sug = pwd + random.choice("!@#") + str(random.randint(11, 99))
        st.info(f"STRONGER_VERSION: {sug}")
        m_uz += " Parolni kuchaytiring."

    if st.button("EXECUTE_VOICE_XULOSA 🔊"):
        speak(m_uz, m_en)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='sidebar-content'>TERMINAL_STATUS</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-content'><b>PROJECT:</b> L1GHTDREAM</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>DEVELOPER:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>STATUS:</b> ENCRYPTED</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#00FF00; font-size:12px;'>Neural analyzer ready for operation.</p>", unsafe_allow_html=True)

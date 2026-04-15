import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0", layout="wide")

# 2. DIZAYN (Yozuvlar ko'rinishi uchun)
def set_bg(file):
    with open(file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.88);
        color: #00FF00;
        border-radius: 20px;
        padding: 40px;
        border: 2px solid #00FF00;
    }}
    /* Matnni o'qish uchun maxsus uslub */
    .hacker-text {{
        color: #00FF00 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    st.warning("Rasm topilmadi.")

# 3. OVOZNI YO'G'ONLASHTIRISH (TRICK)
def speak(text):
    try:
        # slow=True ovozni sekinlashtiradi va robotik, yo'g'onroq qiladi
        tts = gTTS(text=text, lang='uz', slow=True) 
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except:
        # Agar uz ishlamasa, en orqali yo'g'on ovoz
        tts = gTTS(text="Access denied or granted by system.", lang='en', slow=True)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)

# 4. ASOSIY QISM
st.title("⚡ L1GHTDREAM: Neural Analyzer")

pwd = st.text_input("PAROL KIRITING:", type="password")

if pwd:
    # Neyron tarmog'i hisobi (Sodda ko'rinishda)
    res = (len(pwd) * 0.1) + (0.3 if any(c.isupper() for c in pwd) else 0)
    
    st.markdown("---")
    
    if res > 0.7:
        msg = "TIZIMGA KIRISHGA RUXSAT BERILDI. PAROL XAVFSIZ."
        st.success(msg)
    else:
        msg = "DIQQAT! XAVF ANIQLANDI. PAROLNI O'ZGARTIRING!"
        st.error(msg)
        
        # TAVSIYALAR (KO'RINADIGAN QILIB)
        st.markdown("<h2 class='hacker-text'>🛠️ XAKKER TAVSIYASI:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p class='hacker-text'>• Katta harf va belgi qo'shing!</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='hacker-text'>• Tavsiya: {pwd}#2026!</p>", unsafe_allow_html=True)

    if st.button("TIZIM XULOSASINI ESHITISH 🔊"):
        speak(msg)

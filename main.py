import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Neural Shield", layout="wide")

# 2. DIZAYN (Yozuvlarni o'qish uchun qora soya va bloklar)
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
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.9); /* To'qroq qora fon */
        color: #00FF00;
        border-radius: 15px;
        padding: 35px;
        border: 2px solid #00FF00;
        box-shadow: 0 0 30px #00FF00;
    }}
    .hacker-alert {{
        color: #FF0000 !important;
        font-weight: bold;
        text-shadow: 2px 2px 5px black;
        font-size: 24px;
    }}
    .hacker-safe {{
        color: #00FF00 !important;
        font-weight: bold;
        text-shadow: 2px 2px 5px black;
        font-size: 24px;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    pass

# 3. OVOZ FUNKSIYASI (Yo'g'on ovoz effekti)
def speak(text_uz):
    try:
        # slow=True ovozni sekinlashtiradi va robotik-yo'g'on qiladi
        tts = gTTS(text=text_uz, lang='uz', slow=True)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except:
        st.error("Ovozli tizimda xatolik!")

# 4. ASOSIY LOGIKA
st.title("⚡ L1GHTDREAM: Neural Analyzer")

pwd = st.text_input("TAHLIL UCHUN PAROL KIRITING:", type="password")

if pwd:
    # Qattiq neyron tarmog'i (Hisob-kitobni o'zgartirdik)
    length = len(pwd)
    upper = 1 if any(c.isupper() for c in pwd) else 0
    special = 1 if any(not c.isalnum() for c in pwd) else 0
    digit = 1 if any(c.isdigit() for c in pwd) else 0
    
    # Neyron tarmog'i og'irliklari: Uzunlik juda muhim (0.9), belgi (2.5)
    # Endi bias -10.0, ya'ni parol juda kuchli bo'lishi shart!
    z = (length * 0.8) + (upper * 2.0) + (special * 3.0) + (digit * 1.5) - 10.0
    res = 1 / (1 + np.exp(-z)) # Sigmoid

    st.markdown("---")
    
    if res > 0.8: # Faqat juda kuchli parollarga ruxsat
        msg = "Tahlil tugadi. Parol xavfsiz. Tizimga kirishga ruxsat berildi."
        st.markdown(f"<p class='hacker-safe'>✅ {msg}</p>", unsafe_allow_html=True)
        st.balloons()
    else:
        msg = "Diqqat! Neyron tarmog'i zaiflikni aniqladi. Kirish rad etildi!"
        st.markdown(f"<p class='hacker-alert'>❌ {msg}</p>", unsafe_allow_html=True)
        
        # Tavsiyalar
        st.subheader("🛠️ XAKKER TAVSIYASI:")
        if length < 10: st.write("• Parol juda qisqa (kamida 12 ta belgi qiling).")
        if not upper: st.write("• Kamida bitta KATTA harf qo'shing.")
        if not special: st.write("• Maxsus belgi (!, @, #, $) ishlatilmagan.")
        
        # Murakkablashtirish
        s_pwd = pwd + random.choice("!@#$%") + str(random.randint(100, 999))
        st.info(f"💡 Murakkab variant: {s_pwd}")
        msg += " Parolni darhol kuchaytiring!"

    if st.button("OVOZLI XULOSA 🔊"):
        speak(msg)

# Sidebar
with st.sidebar:
    st.header("L1GHTDREAM Info")
    st.write("Dasturchi: Raxmatov Badriddin")
    st.write("Neyron: Sigmoid (Threshold: 0.8)")

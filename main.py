import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import os

# Sahifa sozlamalari
st.set_page_config(page_title="L1GHTDREAM v1.0", layout="wide")

# Orqa fon o'rnatish
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
        background-color: rgba(0, 0, 0, 0.85);
        color: #00FF00;
        border-radius: 20px;
        padding: 50px;
        border: 2px solid #00FF00;
    }}
    </style>
    """, unsafe_allow_html=True)

# bg.jpg faylini tekshirish
try:
    set_bg('bg.jpg')
except:
    st.error("bg.jpg topilmadi!")

# Ovoz berish funksiyasi
def speak(text):
    try:
        tts = gTTS(text=text, lang='uz')
        tts.save("voice.mp3")
        st.audio("voice.mp3", format='audio/mp3', autoplay=True)
    except:
        st.warning("Ovozli funksiya yuklanmadi.")

# L1GHTDREAM Interfeysi
st.title("⚡ L1GHTDREAM: Neural Analyzer")
st.write("Tizim tayyor. Parol murakkabligini tahlil qilish uchun ma'lumot kiriting.")

pwd = st.text_input("Parolni kiriting:", type="password")

if pwd:
    # 6-topshiriq: Tokenizatsiya
    st.write(f"**NLP Tokenlar:** `{list(pwd)}`")

    # 1-topshiriq: Perceptron (Hisob-kitob)
    x = np.array([len(pwd), any(c.isupper() for c in pwd), any(not c.isalnum() for c in pwd)])
    w = np.array([0.7, 1.3, 2.0]) 
    z = np.dot(x, w) - 5.0

    # 2-topshiriq: Sigmoid
    res = 1 / (1 + np.exp(-z))

    st.markdown("---")
    if res > 0.7:
        natija_matni = "L1GHTDREAM tahlili: Parol xavfsiz. Tizimga kirishga ruxsat berildi."
        st.success(f"✅ {natija_matni}")
    else:
        natija_matni = "Diqqat! Neyron tarmog'i zaiflikni aniqladi. Parolni darhol kuchaytiring!"
        st.error(f"❌ {natija_matni}")

    if st.button("OVOZLI NATIJA 🔊"):
        speak(natija_matni)

# Nazariy javoblar (Topshiriq uchun)
with st.sidebar:
    st.header("Amaliy javoblar")
    st.write("**Forward:** Ma'lumotning o'tishi.")
    st.write("**Backprop:** Xatoni tuzatish.")
    st.write("**CNN vs RNN:** CNN rasm, RNN matn uchun.")

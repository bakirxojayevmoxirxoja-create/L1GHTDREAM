import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random
import string

# 1. SAHIFA SOZLAMALARI (Moxirxo'ja nashri)
st.set_page_config(page_title="L1GHTDREAM v2.0 | Moxirxo'ja", layout="wide")

# 2. DIZAYN (Hacker Terminal Style & Yozuvlar ko'rinishi)
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
        background-attachment: fixed;
    }}
    /* Asosiy panel - To'qroq shaffof fon */
    .main .block-container {{
        background-color: rgba(10, 10, 15, 0.9);
        color: #00FF00;
        border-radius: 15px;
        padding: 40px;
        border: 2px solid #00FF00;
        box-shadow: 0 0 30px #00FF00;
    }}
    /* Parol kiritish maydoni dizayni */
    input {{
        background-color: #000000 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        font-family: 'Courier New', monospace !important;
        font-size: 18px !important;
    }}
    /* Tugma dizayni */
    .stButton>button {{
        background-color: #00FF00;
        color: black;
        border-radius: 10px;
        width: 100%;
        font-weight: bold;
    }}
    /* Sidebar (Chap tomon) - Hacker Terminal */
    .css-1d391kg {{
        background-color: rgba(0, 0, 0, 0.9) !important;
        border-right: 2px solid #00FF00;
    }}
    h1, h2, h3, p {{
        font-family: 'Courier New', Courier, monospace;
    }}
    /* Tavsiyalar ro'yxatini ko'rsatish uchun maxsus uslub */
    .recommendation-list li {{
        color: #00FF00 !important;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    st.warning("bg.jpg topilmadi, lekin tizim ishlashda davom etadi.")

# 3. OVOZ FUNKSIYASI (BUFFER ORQALI - MUTLAQO XATOSIZ)
def speak(text_uz):
    try:
        # Fayl yaratmasdan, xotirada ovoz hosil qilish
        tts = gTTS(text=text_uz, lang='uz')
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        # Ovozni ijro etish
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error(f"Ovozli xatolik: {e}. Iltimos, server ruxsatlarini tekshiring.")

# 4. ASOSIY LOGIKA
st.title("⚡ L1GHTDREAM: Neural Analyzer")
st.write("---")

pwd = st.text_input("ANALIZ UCHUN PAROL KIRITING:", type="password")

if pwd:
    # 1-topshiriq: Neyron tarmog'i hisobi
    length = len(pwd)
    upper = 1 if any(c.isupper() for c in pwd) else 0
    special = 1 if any(not c.isalnum() for c in pwd) else 0
    digit = 1 if any(c.isdigit() for c in pwd) else 0
    
    # Neyron og'irliklari va Bias
    w = np.array([0.9, 1.5, 2.5]) 
    b = -7.0
    z = (length * 0.9) + (upper * 1.5) + (special * 2.5) + b
    
    # 2-topshiriq: Sigmoid
    res = 1 / (1 + np.exp(-z))

    st.markdown("---")
    
    # Natija
    if res > 0.7:
        natija_text = "L1GHTDREAM tahlili: Parol xavfsiz. Kirishga ruxsat berildi."
        st.success(f"✅ {natija_text}")
    else:
        natija_text = "Diqqat! Neyron tarmog'i zaiflikni aniqladi. Xakerlik hujumi xavfi yuqori!"
        st.error(f"❌ {natija_text}")
        
        # 3-topshiriq: Tavsiyalar (Yaxshilangan ko'rinish)
        st.subheader("🛠️ XAKKER TAVSIYASI:")
        # Tavsiyalar ko'rinishi uchun maxsus CSS klassli ro'yxat
        tavsiyalar_matni = ""
        if length < 10: tavsiyalar_matni += "<li>Parol uzunligini kamida 12 ta belgiga yetkazing.</li>"
        if not upper: tavsiyalar_matni += "<li>Kamida bitta KATTA harf qo'shing.</li>"
        if not special: tavsiyalar_matni += "<li>Maxsus belgilar qo'shing (masalan: !, @, #, $).</li>"
        
        st.markdown(f"<ul class='recommendation-list'>{tavsiyalar_matni}</ul>", unsafe_allow_html=True)
        
        # Murakkab variant taklifi
        new_pwd = pwd + random.choice("!@#$%") + str(random.randint(10, 99))
        if not any(c.isupper() for c in new_pwd):
            new_pwd = new_pwd.capitalize()
        st.info(f"💡 Tavsiya etilgan yangi parol: `{new_pwd}`")
        natija_text += " Tavsiyalarni bajaring va yangi paroldan foydalaning."

    # 2-topshiriq: Ovoz tugmasi
    if st.button("OVOZLI XULOSA 🔊"):
        speak(natija_text)

# 5. SIDEBAR JAVOBLARI (Tuzatilgan ism va Xaker Terminali)
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00; font-family:Courier New;'>System Analysis</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("**LOYIHA:** L1GHTDREAM v2.0")
    # Ismingizni qora hoshiya bilan ajratib ko'rsatish
    st.markdown("<p style='color:#00FF00; background-color:rgba(0,0,0,0.5); padding:10px; border-radius:5px;'>TUZUVCHI:<br><b>Bakirxo'jayev Moxirxo'ja</b></p>", unsafe_allow_html=True)
    st.write("**STATUS:** ENCRYPTED")
    st.write("---")
    st.info("Neyron tarmoq Sigmoid funksiyasi yordamida har bir kiritilgan belgini xavfsizlik darajasini tahlil qiladi.")

import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Deep Neural Analyzer", layout="wide")

# 2. ORQA FON VA DIZAYN (YAXSHILANGAN KO'RINISh)
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
    /* Matnlarni o'qish oson bo'lishi uchun markaziy blok */
    .main .block-container {{
        background-color: rgba(10, 10, 15, 0.9); /* To'q kulrang shaffof fon */
        color: #00FF00; /* Yashil Matrix matni */
        border-radius: 20px;
        padding: 40px;
        border: 2px solid #00FF00;
        box-shadow: 0 0 25px rgba(0, 255, 0, 0.5);
    }}
    /* Kiritish maydoni dizayni */
    .stTextInput>div>div>input {{
        background-color: #000000;
        color: #00FF00;
        border: 1px solid #00FF00;
        font-family: 'Courier New', monospace;
    }}
    /* Tugma dizayni (Yaxshilangan ko'rinish) */
    .stButton>button {{
        background-color: #008000; /* To'q yashil fonda oq fondan ko'ra yaxshi ajraladi */
        color: white;
        border-radius: 10px;
        border: 2px solid #00FF00;
        width: 100%;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #00FF00;
        color: black;
    }}
    h1, h2, h3, p, li {{
        font-family: 'Courier New', Courier, monospace;
        color: #00FF00 !important; /* Hamma matnlar yashil bo'lishini ta'minlash */
    }}
    /* Sidebar dizayni */
    .css-1d391kg {{
        background-color: rgba(0, 0, 0, 0.85);
        color: #00FF00;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    st.warning("bg.jpg topilmadi.")

# 3. OVOZ FUNKSIYASI (Yo'g'on ovoz va ZAXIRA BILAN)
def speak(text_uz, text_en="System analysis complete."):
    """O'zbekcha matnni o'qiydi, agar ishlamasa inglizcha matnni o'qiydi."""
    try:
        # Avval O'zbek tilini tekshiramiz
        tts = gTTS(text=text_uz, lang='uz', slow=True) # Sekin o'qish yo'g'on effekt beradi
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
        st.success("Ovozli tahlil: O'zbek tilida.")
    except Exception as e_uz:
        # Agar O'zbek tili ishlamasa (Language not supported: uz bo'lsa)
        st.warning(f"O'zbek tilida xatolik: {e_uz}. Ingliz tiliga o'tilmoqda.")
        try:
            # Ingliz tilini tekshiramiz (yo'g'on ovoz bilan)
            tts = gTTS(text=text_en, lang='en', slow=True) 
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format='audio/mp3', autoplay=True)
            st.success("Audio analysis: English.")
        except Exception as e_en:
            # Agar ingliz tili ham ishlamasa
            st.error(f"Ovozli tahlil mutlaqo ishlamadi: {e_en}")

# 4. PAROLNI MURAKKABLASHTIRISH FUNKSIYASI
def strengthen_password(old_pwd):
    # Parolga maxsus belgilar va sonlar qo'shish
    chars = "!@#$%^&*"
    enhanced = old_pwd + random.choice(chars) + str(random.randint(10, 99))
    if not any(c.isupper() for c in enhanced):
        enhanced = enhanced.capitalize()
    return enhanced

# 5. ASOSIY QISM
st.title("⚡ L1GHTDREAM v2.0: Deep Neural Breach Analyzer")
st.write("---")

pwd = st.text_input("ANALIZ UCHUN PAROL KIRITING:", type="password", help="Enter password to be analyzed.")

# Natija va tahlil uchun zaxira matnlar
final_status_uz = ""
final_status_en = ""

if pwd:
    # NLP Tahlili
    st.markdown("### 🔍 Deep Analysis...")
    
    # Neyron tarmog'i hisobi
    has_upper = any(c.isupper() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    length = len(pwd)
    
    # Input xususiyatlari: Uzunlik, Katta harf, Belgilar
    x = np.array([length, 1 if has_upper else 0, 1 if has_special else 0])
    
    # Neyron og'irliklari (Weights) va Bias
    # Og'irliklarni biroz o'zgartirdim, uzunlikka ko'proq ahamiyat berish uchun
    w = np.array([0.9, 1.3, 2.3]) 
    z = np.dot(x, w) - 7.0 # Bias
    
    # Aktivatsiya funksiyasi (Sigmoid)
    res = 1 / (1 + np.exp(-z))

    st.markdown("---")
    
    # 1. NATIJA VA TAVSIYALAR
    tavsiyalar = []
    if length < 10: tavsiyalar.append("Parol uzunligini kamida 12 ta belgiga yetkazing.")
    if not has_upper: tavsiyalar.append("Kamida bitta KATTA harf qo'shing.")
    if not has_special: tavsiyalar.append("Maxsus belgilar qo'shing (masalan: !, @, #, $).")
    
    if res > 0.7:
        status_msg = "Tahlil tugadi. Parol xavfsiz. Kirishga ruxsat berildi."
        st.success(f"✅ {status_msg}")
        final_status_uz = status_msg
        final_status_en = "Analysis complete. Password secure. Access granted."
    else:
        status_msg = "Diqqat! Parol juda zaif. Tizim xavf ostida!"
        st.error(f"❌ {status_msg}")
        
        # Tavsiyalarni ko'rsatish
        st.markdown("## 🛠️ XAKKER TAVSIYASI:")
        # Tavsiyalar ro'yxatini to'q rangda ko'rsatish
        for t in tavsiyalar:
            st.markdown(f"**- {t}**")
        
        # Murakkablashtirilgan variant
        new_pwd = strengthen_password(pwd)
        st.info(f"💡 Tavsiya etilgan yangi parol: `{new_pwd}`")
        final_status_uz = status_msg + " Tavsiyalarni bajaring va yangi paroldan foydalaning."
        final_status_en = "Warning! Password too weak. Breach risk detected! Check hacker recommendations and use the suggested password."

    # 2. OVOZLI CHIQISH (Faqat tugma bosilganda)
    if st.button("Tizim xulosasini eshitish 🔊 (Listen to Analysis)"):
        # O'zbekcha va Inglizcha matnlarni zaxira sifatida yuborish
        speak(final_status_uz, final_status_en)

# 6. SIDEBAR JAVOBLARI
with st.sidebar:
    st.header("L1GHTDREAM Info")
    st.write("---")
    st.write("Dasturchi: Raxmatov Badriddin")
    st.markdown("""
    **Neyron tarmoq:** Sigmoid aktivatsiya funksiyasi yordamida kiritilgan parol xavfsizligini 0 dan 1 gacha baholaydi.
    **NLP:** Matnni tokenlarga ajratish va belgilar turini tahlil qilish orqali ishlaydi.
    **Amaliy mashg'ulot javobi:** Sigmoid funksiyasi neyron chiqishini ehtimollik qiymatiga aylantiradi.
    """)

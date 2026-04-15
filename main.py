import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Deep Neural Analyzer", layout="wide")

# 2. ORQA FON
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
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.85);
        color: #00FF00;
        border-radius: 20px;
        padding: 40px;
        border: 2px solid #00FF00;
        box-shadow: 0 0 25px #00FF00;
    }}
    .stTextInput>div>div>input {{
        background-color: #0e1117;
        color: #00FF00;
        border: 1px solid #00FF00;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    st.warning("bg.jpg topilmadi.")

# 3. OVOZ FUNKSIYASI (Yo'g'on ovoz hiylasi bilan)
def speak(text):
    try:
        # O'zbekcha matnni biroz sekinroq o'qitish orqali yo'g'on effekt beramiz
        tts = gTTS(text=text, lang='uz', slow=True) 
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error(f"Ovozli xatolik: {e}")

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

pwd = st.text_input("ANALIZ UCHUN PAROL KIRITING:", type="password")

if pwd:
    # NLP Tahlili
    st.markdown("### 🔍 Deep Analysis...")
    
    # Neyron tarmog'i hisobi
    has_upper = any(c.isupper() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    length = len(pwd)
    
    x = np.array([length, 1 if has_upper else 0, 1 if has_special else 0])
    w = np.array([0.8, 1.5, 2.5])
    z = np.dot(x, w) - 6.0
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
    else:
        status_msg = "Diqqat! Parol juda zaif. Tizim xavf ostida!"
        st.error(f"❌ {status_msg}")
        
        # Tavsiyalarni ko'rsatish
        st.subheader("🛠️ XAKKER TAVSIYASI:")
        for t in tavsiyalar:
            st.write(f"• {t}")
        
        # Murakkablashtirilgan variant
        new_pwd = strengthen_password(pwd)
        st.info(f"💡 Tavsiya etilgan yangi parol: `{new_pwd}`")
        status_msg += " Tavsiyalarni bajaring va yangi paroldan foydalaning."

    # 2. OVOZLI CHIQISH
    if st.button("Tizim xulosasini eshitish 🔊"):
        speak(status_msg)

# 6. SIDEBAR JAVOBLARI
with st.sidebar:
    st.header("L1GHTDREAM Info")
    st.write("Dasturchi: Raxmatov Badriddin")
    st.markdown("""
    **Neyron tarmoq:** Sigmoid funksiyasi asosida ishlaydi.
    **NLP:** Matnni tokenlarga ajratish orqali tahlil qiladi.
    """)

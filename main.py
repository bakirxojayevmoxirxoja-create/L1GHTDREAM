import streamlit as st
import numpy as np
import base64
from gtts import gTTS
import io
import randomimport streamlit aimport streamlit as st
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
        /* Markaziy Terminal Paneli */
        .main .block-container {{
            background-color: rgba(0, 0, 0, 0.94) !important;
            border: 2px solid #00FF00;
            box-shadow: 0 0 25px #00FF00;
            border-radius: 12px;
            padding: 45px;
        }}
        /* Sidebar (Chap tomon) - Terminal Style */
        [data-testid="stSidebar"] {{
            background-color: rgba(0, 5, 0, 0.98) !important;
            border-right: 2px solid #00FF00;
        }}
        .sidebar-content {{
            color: #00FF00 !important;
            font-family: 'Courier New', monospace;
        }}
        /* Kirish maydoni (Input) */
        input {{
            background-color: #000 !important;
            color: #00FF00 !important;
            border: 1px solid #00FF00 !important;
            font-family: 'Courier New', monospace !important;
        }}
        /* Tavsiyalar uchun yashil font */
        .hacker-text {{
            color: #00FF00 !important;
            text-shadow: 1px 1px 2px black;
            font-family: 'Courier New', monospace;
        }}
        </style>
        """, unsafe_allow_html=True)
    except:
        pass

set_bg('bg.jpg')

# 3. OVOZ FUNKSIYASI (BARQAROR REJIM)
def speak(text_uz, text_en):
    try:
        # O'zbekcha sinov
        tts = gTTS(text=text_uz, lang='uz')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
    except:
        # Agar uz ishlamasa, yo'g'on inglizcha ovoz
        tts = gTTS(text=text_en, lang='en', slow=True)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
        st.info("Terminal Note: Secure Voice Protocol Active (EN).")

# 4. ASOSIY LOGIKA
st.markdown("<h1 style='color:#00FF00; font-family:monospace;'>$ NEURAL_ANALYZER_v2.0</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_spec = any(not c.isalnum() for c in pwd)
    
    # Sigmoid hisobi
    z = (length * 0.85) + (has_upper * 2.5) + (has_spec * 3.5) - 11.0
    res = 1 / (1 + np.exp(-z))

    st.write("---")
    
    if res > 0.8:
        m_uz = "Tizimga kirish tasdiqlandi. Xavfsiz."
        m_en = "Access granted. System is secure."
        st.success(f"✅ {m_uz}")
    else:
        m_uz = "Diqqat! Kirish rad etildi. Parol juda zaif!"
        m_en = "Access denied. Password strength insufficient."
        st.error(f"❌ {m_uz}")
        
        # Tavsiyalar (Tiniq ko'rinishda)
        st.markdown("<h3 class='hacker-text'>[ SYSTEM_ADVICE ]</h3>", unsafe_allow_html=True)
        if length < 12: st.markdown("<p class='hacker-text'>- Harf sonini 12 taga yetkazing.</p>", unsafe_allow_html=True)
        if not has_upper: st.markdown("<p class='hacker-text'>- KATTA harf ishlating.</p>", unsafe_allow_html=True)
        if not has_spec: st.markdown("<p class='hacker-text'>- Maxsus belgi (!, #, $) qo'shing.</p>", unsafe_allow_html=True)
        
        # Taklif
        sug = pwd + random.choice("!@#") + str(random.randint(11, 99))
        st.info(f"STRONGER_VERSION: {sug}")
        m_uz += " Parolni kuchaytiring."

    if st.button("EXECUTE_VOICE_XULOSA 🔊"):
        speak(m_uz, m_en)

# 5. SIDEBAR (To'g'ri ism va Hacker info)
with st.sidebar:
    st.markdown("<h2 class='sidebar-content'>TERMINAL_STATUS</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-content'><b>PROJECT:</b> L1GHTDREAM</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>DEVELOPER:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-content'><b>ENGINE:</b> Sigmoid Neural</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#00FF00; font-size:12px;'>Neural analyzer encrypted and ready.</p>", unsafe_allow_html=True)s st
import numpy as np
import base64
from gtts import gTTS
import io
import random

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v2.0 | Moxirxo'ja", layout="wide")

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
        background-attachment: fixed;
    }}
    /* Markaziy blok dizayni */
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.93) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 20px #00FF00;
        border-radius: 15px;
        padding: 50px;
    }}
    /* Sidebar dizayni (Chap tomon) */
    [data-testid="stSidebar"] {{
        background-color: rgba(0, 20, 0, 0.95) !important;
        border-right: 2px solid #00FF00;
    }}
    .sidebar-text {{
        color: #00FF00 !important;
        font-family: 'Courier New', monospace;
    }}
    /* Yozuvlar va tavsiyalar ko'rinishi */
    .hacker-msg {{
        color: #00FF00 !important;
        background-color: rgba(0, 50, 0, 0.5);
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-shadow: 1px 1px 2px black;
    }}
    input {{
        background-color: #000 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

try:
    set_bg('bg.jpg')
except:
    pass

# 3. OVOZ FUNKSIYASI (BARQAROR VARIANT)
def speak(text_uz, text_en):
    try:
        # Avval o'zbekchani sinab ko'ramiz
        tts = gTTS(text=text_uz, lang='uz', slow=False)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
    except:
        # Agar uz ishlamasa, inglizcha "Security System" ovozini beramiz
        tts = gTTS(text=text_en, lang='en', slow=True) # Slow yo'g'on ovoz beradi
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3', autoplay=True)
        st.warning("System Note: Voice synthesized in Security Mode (EN).")

# 4. ASOSIY QISM
st.markdown("<h1 style='color:#00FF00; font-family:monospace;'>$ L1GHTDREAM_NEURAL_SHIELD_v2.0</h1>", unsafe_allow_html=True)

pwd = st.text_input("ENTER ACCESS KEY:", type="password")

if pwd:
    # Neyron tarmog'i algoritmi
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_spec = any(not c.isalnum() for c in pwd)
    
    z = (length * 0.8) + (has_upper * 2.0) + (has_spec * 3.0) - 10.0
    res = 1 / (1 + np.exp(-z))

    if res > 0.75:
        msg_uz = "Ruxsat berildi. Tizim xavfsiz."
        msg_en = "Access granted. System secure."
        st.success(f"✅ {msg_uz}")
    else:
        msg_uz = "Diqqat! Parol zaif. Kirish rad etildi!"
        msg_en = "Warning! Weak password. Access denied!"
        st.error(f"❌ {msg_uz}")
        
        # TAVSIYALAR (Yaxshilangan ko'rinish)
        st.markdown("<div class='hacker-msg'>🛠️ TERMINAL TAVSIYASI:</div>", unsafe_allow_html=True)
        t_list = []
        if length < 12: t_list.append("Uzunlikni 12 taga yetkazing.")
        if not has_upper: t_list.append("KATTA harf qo'shing.")
        if not has_spec: t_list.append("Maxsus belgi (!, @, #) qo'shing.")
        
        for t in t_list:
            st.markdown(f"<p style='color:#00FF00; margin-left:20px;'> > {t}</p>", unsafe_allow_html=True)
            
        # Murakkab variant
        suggested = pwd + random.choice("@#$%") + str(random.randint(10, 99))
        st.info(f"💡 Taklif: {suggested}")
        msg_uz += " Parolni murakkablashtiring."

    if st.button("VOICE OUTPUT 🔊"):
        speak(msg_uz, msg_en)

# 5. SIDEBAR (Hacker Style)
with st.sidebar:
    st.markdown("<h2 class='sidebar-text'>TERMINAL INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p class='sidebar-text'><b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>ENCRYPTION:</b> AES-256 Neural</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>STATUS:</b> ACTIVE</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='font-size:12px; color:#00FF00;'>Sigmoid funksiyasi orqali har bir belgi xavfsizlik darajasi tahlil qilinmoqda.</p>", unsafe_allow_html=True)
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

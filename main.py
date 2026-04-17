import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v3.2 | Bakirxo'jayev", layout="wide")

# 2. DIZAYN (Hacker Terminal)
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
        .hacker-text {{ color: #00FF00 !important; font-family: 'Courier New', monospace; }}
        .token-box {{
            border: 1px solid #00FF00;
            padding: 10px;
            margin: 5px;
            display: inline-block;
            background: rgba(0, 255, 0, 0.1);
            color: #00FF00;
        }}
        .error-msg {{ color: #FF3333 !important; font-weight: bold; margin-bottom: 5px; }}
        .big-advice {{
            font-size: 20px !important;
            color: #00FF00;
            border: 2px solid #00FF00;
            padding: 12px;
            background: rgba(0, 50, 0, 0.6);
            margin: 8px 0;
        }}
        </style>
        """, unsafe_allow_html=True)
    except: pass

set_bg('bg.jpg')

# 3. BRUTE-FORCE VAQTINI HISOBLASH
def calculate_brute_time(pwd):
    length = len(pwd)
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    if charset == 0 or length == 0: return "0 sekund"
    
    combinations = charset ** length
    seconds = combinations / 100_000_000_000 # 100 mlrd urinish/sek
    
    if seconds < 1: return "ZUMRAD (Instant!)"
    if seconds < 3600: return f"{int(seconds/60)} daqiqa"
    if seconds < 86400: return f"{int(seconds/3600)} soat"
    return f"{int(seconds/31536000)} yil"

# 4. ASOSIY QISM
st.markdown("<h1 class='hacker-text'>$ L1GHTDREAM_v3.2</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # A) TOKENIZATSIYA (AMALIY)
    tokens = list(pwd)
    st.markdown("<h3 class='hacker-text'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in tokens])
    st.markdown(token_html, unsafe_allow_html=True)
    st.write(f"Jami belgilar soni: **{len(pwd)} ta**")

    # B) TAHLIL VA XATOLAR
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_spec = any(c in string.punctuation for c in pwd)
    length = len(pwd)
    
    st.write("---")
    
    if length >= 12 and has_upper and has_digit and has_spec:
        st.success("✅ ACCESS GRANTED: Neyron tarmog'i parolni tasdiqladi.")
    else:
        st.markdown("<h3 class='hacker-text'>[ 2. ANALYSIS ERRORS ]</h3>", unsafe_allow_html=True)
        if length < 12: st.markdown(f"<p class='error-msg'>⚠️ XATO: Uzunlik yetarli emas (Hozir: {length}, Kamida: 12)</p>", unsafe_allow_html=True)
        if not has_upper: st.markdown("<p class='error-msg'>⚠️ XATO: Katta harf (A-Z) ishlatilmagan!</p>", unsafe_allow_html=True)
        if not has_digit: st.markdown("<p class='error-msg'>⚠️ XATO: Raqam (0-9) topilmadi!</p>", unsafe_allow_html=True)
        if not has_spec: st.markdown("<p class='error-msg'>⚠️ XATO: Maxsus belgi (!, @, #) yo'q!</p>", unsafe_allow_html=True)

        # C) BRUTE-FORCE VA TAKLIFLAR
        brute_time = calculate_brute_time(pwd)
        st.error(f"Hujum simulyatsiyasi: Buzish uchun **{brute_time}** ketadi.")

        st.markdown("<h3 class='hacker-text' style='margin-top:20px;'>[ 3. SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        for _ in range(3):
            sug = "".join(random.choice(string.ascii_letters + string.digits + "!@#$") for _ in range(14))
            st.markdown(f"<div class='big-advice'> > {sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='hacker-text'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='hacker-text'><b>DEV:</b> Bakirxo'jayev M.</p>")
    st.markdown("<p class='hacker-text'><b>STATUS:</b> ENCRYPTED</p>")

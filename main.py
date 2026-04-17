import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v3.1 | Bakirxo'jayev", layout="wide")

# 2. DIZAYN VA STIL (Kattalashtirilgan yozuvlar bilan)
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
        .hacker-text {{
            color: #00FF00 !important;
            font-family: 'Courier New', monospace;
        }}
        /* TAVSIYA VA TAKLIFLARNI KATTALASHTIRISH */
        .big-advice {{
            font-size: 22px !important;
            font-weight: bold;
            color: #00FF00;
            border: 2px solid #00FF00;
            padding: 15px;
            background: rgba(0, 50, 0, 0.7);
            border-radius: 10px;
            margin: 10px 0;
        }}
        .brute-box {{
            background-color: rgba(50, 0, 0, 0.7);
            border: 2px solid #FF3333;
            color: #FF3333;
            padding: 20px;
            font-size: 20px;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
        }}
        input {{
            background-color: #000 !important;
            color: #00FF00 !important;
            border: 1px solid #00FF00 !important;
            font-size: 18px !important;
        }}
        </style>
        """, unsafe_allow_html=True)
    except: pass

set_bg('bg.jpg')

# 3. BRUTE-FORCE VAQTINI HISOBLASH (REALISTIK)
def calculate_brute_time(pwd):
    length = len(pwd)
    charset_size = 0
    if any(c.islower() for c in pwd): charset_size += 26
    if any(c.isupper() for c in pwd): charset_size += 26
    if any(c.isdigit() for c in pwd): charset_size += 10
    if any(c in string.punctuation for c in pwd): charset_size += 32
    
    if charset_size == 0: return "0 sekund"
    
    # Umumiy kombinatsiyalar soni
    combinations = charset_size ** length
    # Taxminiy tezlik: sekundiga 100 milliard urinish (kuchli server)
    seconds = combinations / 100_000_000_000
    
    if seconds < 1: return "0.01 sekund (Instant!)"
    if seconds < 60: return f"{int(seconds)} sekund"
    if seconds < 3600: return f"{int(seconds/60)} daqiqa"
    if seconds < 86400: return f"{int(seconds/3600)} soat"
    if seconds < 31536000: return f"{int(seconds/86400)} kun"
    return f"{int(seconds/31536000)} yil"

# 4. ASOSIY LOGIKA
st.markdown("<h1 class='hacker-text'>$ L1GHTDREAM_v3.1</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Neyron tahlil kriteriyalari
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_spec = any(c in string.punctuation for c in pwd)
    length = len(pwd)
    
    is_strong = length >= 12 and has_upper and has_digit and has_spec #

    st.write("---")
    
    if is_strong:
        st.success("✅ ACCESS GRANTED: Tizim xavfsiz.")
    else:
        st.error("❌ ACCESS DENIED: Parol juda zaif!")
        
        # BRUTE-FORCE (Realistik vaqt)
        brute_time = calculate_brute_time(pwd)
        st.markdown(f"""
        <div class='brute-box'>
            [ ALERT ] Hujum simulyatsiyasi:<br>
            Ushbu parolni buzish uchun taxminan <b>{brute_time}</b> vaqt ketadi.
        </div>
        """, unsafe_allow_html=True)
        
        # KATTALASHTIRILGAN TAKLIFLAR
        st.markdown("<h3 class='hacker-text' style='margin-top:25px;'>[ MUKAMMAL TAKLIFLAR ]</h3>", unsafe_allow_html=True)
        
        # 3 ta chiroyli va kuchli variant
        for _ in range(3):
            sug = "".join(random.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(14))
            st.markdown(f"<div class='big-advice'> > {sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='hacker-text'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='hacker-text'><b>DEV:</b> Bakirxo'jayev M.</p>", unsafe_allow_html=True)
    st.markdown("<p class='hacker-text'><b>VER:</b> 3.1 (Stable)</p>", unsafe_allow_html=True)

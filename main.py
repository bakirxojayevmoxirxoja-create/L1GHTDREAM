import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM v3.3 | Bakirxo'jayev", layout="wide")

# 2. DIZAYN
def set_bg(file):
    try:
        with open(file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        st.markdown(f"""
        <style>
        .stApp {{ background-image: url("data:image/png;base64,{bin_str}"); background-size: cover; background-attachment: fixed; }}
        .main .block-container {{ background-color: rgba(0, 0, 0, 0.94); border: 2px solid #00FF00; box-shadow: 0 0 25px #00FF00; padding: 45px; border-radius: 12px; }}
        .hacker-text {{ color: #00FF00 !important; font-family: 'Courier New', monospace; }}
        .token-box {{ border: 1px solid #00FF00; padding: 10px; margin: 5px; display: inline-block; background: rgba(0, 255, 0, 0.1); color: #00FF00; }}
        .brute-box {{ background-color: rgba(50, 0, 0, 0.8); border: 2px solid #FF3333; color: #FF3333; padding: 20px; font-size: 20px; border-radius: 10px; }}
        </style>
        """, unsafe_allow_html=True)
    except: pass

set_bg('bg.jpg')

# 3. VAQTNI ANIQ HISOBLASH (To'g'rilangan qism)
def calculate_brute_time(pwd):
    length = len(pwd)
    if length == 0: return "0 sekund"
    
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    
    combinations = charset ** length
    # Sekundiga 100 milliard urinish
    seconds = combinations / 100_000_000_000
    
    # ENDI "ZUMRAD" DEMAYDI, ANIQ VAQT AYTADI:
    if seconds < 0.01: return "0.0001 sekund (Juda zaif!)"
    if seconds < 1: return f"{seconds:.4f} sekund"
    if seconds < 60: return f"{int(seconds)} sekund"
    if seconds < 3600: return f"{int(seconds/60)} daqiqa"
    if seconds < 86400: return f"{int(seconds/3600)} soat"
    if seconds < 31536000: return f"{int(seconds/86400)} kun"
    return f"{int(seconds/31536000)} yil"

# 4. ASOSIY QISM
st.markdown("<h1 class='hacker-text'>$ L1GHTDREAM_v3.3</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Tokenlar
    st.markdown("<h3 class='hacker-text'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    tokens = list(pwd)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in tokens])
    st.markdown(token_html, unsafe_allow_html=True)
    st.write(f"Parol uzunligi: {len(pwd)} ta belgi.")

    # Tahlil
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_spec = any(c in string.punctuation for c in pwd)
    
    st.write("---")
    
    if len(pwd) >= 12 and has_upper and has_digit and has_spec:
        st.success("✅ TIZIM XAVFSIZ.")
    else:
        # Brute-force qutisi
        brute_time = calculate_brute_time(pwd)
        st.markdown(f"""
        <div class='brute-box'>
            [ ALERT ] HUJUM SIMULYATSIYASI:<br>
            Buzish uchun ketadigan taxminiy vaqt: <b>{brute_time}</b>
        </div>
        """, unsafe_allow_html=True)
        
        # Xatolar
        st.markdown("<h3 class='hacker-text'>[ ANALYSIS ERRORS ]</h3>", unsafe_allow_html=True)
        if len(pwd) < 12: st.error(f"⚠️ Kamida 12 ta belgi kerak (Hozir: {len(pwd)})")
        if not has_upper: st.error("⚠️ Katta harf topilmadi!")
        if not has_digit: st.error("⚠️ Raqam kiritilmagan!")
        if not has_spec: st.error("⚠️ Maxsus belgi (!, @, #) yo'q!")

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='hacker-text'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='hacker-text'><b>DEV:</b> Bakirxo'jayev M.</p>", unsafe_allow_html=True)

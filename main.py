import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. KREATIV DIZAYN
def set_design():
    st.markdown("""
    <style>
    .stApp { background-color: #000; color: #00FF00; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.95) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 30px #00FF00;
        border-radius: 15px;
        padding: 45px;
    }
    .centered-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 65px; font-weight: bold; text-shadow: 0 0 20px #00FF00;
        letter-spacing: 8px; margin-bottom: 40px;
    }
    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    .stats-box {
        background: rgba(0, 255, 0, 0.05);
        border-left: 5px solid #00FF00;
        padding: 15px; margin: 10px 0;
        font-family: 'Courier New', monospace;
    }
    .brute-box {
        background-color: rgba(50, 0, 0, 0.8);
        border: 2px solid #FF3333;
        color: #FF3333;
        padding: 20px;
        font-size: 18px;
        border-radius: 10px;
    }
    [data-testid="stSidebar"] {
        background-color: #050505 !important;
        border-right: 1px solid #00FF00;
    }
    .sidebar-text {
        color: #00FF00 !important;
        font-family: 'Courier New', monospace;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

set_design()

# 3. BRUTE-FORCE VAQTNI HISOBLASH
def get_brute_time(pwd):
    length = len(pwd)
    if length == 0: return "0 sekund"
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    
    combinations = charset ** length
    sec = combinations / 100_000_000_000 # 100 mlrd urinish/sek
    
    if sec < 0.01: return "0.0001 sekund"
    if sec < 3600: return f"{int(sec/60)} daqiqa"
    if sec < 86400: return f"{int(sec/3600)} soat"
    if sec < 31536000: return f"{int(sec/86400)} kun"
    return f"{int(sec/31536000)} yil"

# 4. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Tokenlar
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    tokens = list(pwd)
    # Tahlil - Xato shu yerda edi (f"..." qo'shildi)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in tokens])
    st.markdown(token_html, unsafe_allow_html=True)
    
    # Statistika
    u_count = sum(1 for c in pwd if c.isupper())
    l_count = sum(1 for c in pwd if c.islower())
    d_count = sum(1 for c in pwd if c.isdigit())
    s_count = sum(1 for c in pwd if c in string.punctuation)
    
    st.markdown(f"""
    <div class='stats-box'>
        > Jami belgilar: {len(pwd)} ta<br>
        > Katta harflar: {u_count} ta<br>
        > Kichik harflar: {l_count} ta<br>
        > Raqamlar: {d_count} ta<br>
        > Maxsus belgilar: {s_count} ta
    </div>
    """, unsafe_allow_html=True)

    is_ok = len(pwd) >= 12 and u_count > 0 and d_count > 0 and s_count > 0
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        brute = get_brute_time(pwd)
        st.markdown(f"<div class='brute-box'>[ ALERT ] HUJUM SIMULYATSIYASI: <b>{brute}</b></div>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color:#00FF00;'>[ ANALYSIS ERRORS ]</h3>", unsafe_allow_html=True)
        if len(pwd) < 12: st.error(f"⚠️ Kamida 12 ta belgi (Hozir: {len(pwd)})")
        if u_count == 0: st.error("⚠️ Katta harf (A-Z) ishlatilmagan")
        if d_count == 0: st.error("⚠️ Raqam (0-9) topilmadi")
        if s_count == 0: st.error("⚠️ Maxsus belgi topilmadi")

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-text'><b>DASTURCHI:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>NICKNAME:</b><br>LIMITLESS</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#008800; font-size:12px;'>Tizim tahlilga tayyor.</p>", unsafe_allow_html=True)

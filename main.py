import streamlit as st
import numpy as np
import base64
import random
import string
import time

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | Bakirxo'jayev", layout="wide")

# 2. KREATIV DIZAYN (Custom CSS)
def set_design():
    st.markdown(f"""
    <style>
    .stApp {{ background-color: #000; color: #00FF00; }}
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.95);
        border: 2px solid #00FF00;
        box-shadow: 0 0 30px #00FF00;
        border-radius: 15px;
        padding: 50px;
    }}
    .centered-title {{
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 70px; font-weight: bold; text-shadow: 0 0 25px #00FF00;
        letter-spacing: 10px; margin-bottom: 50px;
    }}
    .hacker-card {{
        border: 1px solid #00FF00; padding: 20px; border-radius: 10px;
        background: rgba(0, 255, 0, 0.05); margin: 10px 0;
        transition: 0.3s;
    }}
    .hacker-card:hover {{ background: rgba(0, 255, 0, 0.15); transform: scale(1.02); }}
    .token-box {{
        border: 2px solid #00FF00; padding: 12px; margin: 5px;
        display: inline-block; color: #00FF00; font-weight: bold;
        box-shadow: 0 0 10px #00FF00;
    }}
    </style>
    """, unsafe_allow_html=True)

set_design()

# 3. VAQTNI HISOBLASH (Realistik kombinatorika)
def get_brute_time(pwd):
    length = len(pwd)
    if length == 0: return "0 sekund"
    charset = sum([26 if any(c.islower() for c in pwd) else 0,
                  26 if any(c.isupper() for c in pwd) else 0,
                  10 if any(c.isdigit() for c in pwd) else 0,
                  32 if any(c in string.punctuation for c in pwd) else 0])
    combinations = charset ** length
    sec = combinations / 100_000_000_000
    if sec < 0.01: return "Sekunddan qisqa"
    if sec < 3600: return f"{int(sec/60)} daqiqa"
    if sec < 86400: return f"{int(sec/3600)} soat"
    return f"{int(sec/31536000)} yil"

# 4. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # KREATIV SCANNING EFFEKTI
    with st.spinner('NEURAL NETWORK IS SCANNING...'):
        time.sleep(1) # Skanerlash animatsiyasi uchun

    # 1. TOKENIZATSIYA (Vizuallash)
    st.markdown("<h3 style='color:#00FF00;'>[ SYSTEM_LOG: TOKENIZING ]</h3>", unsafe_allow_html=True)
    cols = st.columns(len(pwd) if len(pwd) < 15 else 15)
    for i, char in enumerate(list(pwd)[:15]):
        cols[i % 15].markdown(f"<div class='token-box'>{char}</div>", unsafe_allow_html=True)
    
    # 2. TAHLIL
    has_up, has_dig, has_sp = any(c.isupper() for c in pwd), any(c.isdigit() for c in pwd), any(c in string.punctuation for c in pwd)
    is_ok = len(pwd) >= 12 and has_up and has_dig and has_sp

    st.write("---")
    
    if is_ok:
        st.balloons() # G'alaba animatsiyasi
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        # BRUTE FORCE DATA
        st.warning(f"⚠️ SECURITY ALERT: Buzish vaqti - {get_brute_time(pwd)}")
        
        st.markdown("<h3 style='color:#00FF00;'>[ RECOMMENDED_VARIANTS ]</h3>", unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns(3)
        
        # KREATIV TAKLIFLAR
        for col in [col_a, col_b, col_c]:
            sug = "".join(random.choice(string.ascii_letters + string.digits + "@#$") for _ in range(14))
            col.markdown(f"""
            <div class='hacker-card'>
                <small>GEN_KEY:</small><br>
                <b>{sug}</b>
            </div>
            """, unsafe_allow_html=True)

# 5. SIDEBAR (INFO)
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.info(f"Dasturchi: Bakirxo'jayev M.")
    st.info(f"Yosh: 19") #
    st.info(f"Algoritm: Deep Neural Analysis")

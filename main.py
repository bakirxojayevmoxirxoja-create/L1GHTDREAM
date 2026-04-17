import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. DIZAYN (Hacker Style)
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
    .suggestion-card {
        border: 1px solid #00FF00; padding: 15px; border-radius: 8px;
        background: rgba(0, 255, 0, 0.12); text-align: center;
        margin: 5px; font-family: 'Courier New', monospace;
        color: #00FF00; font-size: 16px;
    }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #00FF00; }
    .sidebar-text { color: #00FF00 !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

set_design()

# 3. KUCHAYTIRILGAN VAQT HISOBLASH (Sekundlargacha aniq)
def get_precise_brute_time(pwd):
    length = len(pwd)
    if length == 0: return "0 sekund"
    
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    
    combinations = charset ** length
    # Sekundiga 100 milliard urinish (Superkompyuter tezligi)
    sec = combinations / 100_000_000_000 
    
    if sec < 1: return f"{sec:.4f} sekund (Deyarli darhol!)"
    if sec < 60: return f"{sec:.2f} sekund"
    if sec < 3600: return f"{(sec/60):.2f} daqiqa"
    if sec < 86400: return f"{(sec/3600):.2f} soat"
    if sec < 31536000: return f"{(sec/86400):.2f} kun"
    return f"{int(sec/31536000)} yil"

# 4. KUCHAYTIRILGAN TAVSIYALAR
def generate_limitless_suggestions(base_pwd):
    suggestions = []
    specs = "!@#$%^&*"
    for _ in range(3):
        # Boshiga bitta katta harf, oxiriga belgi va raqam qo'shish
        sug = random.choice(string.ascii_uppercase) + base_pwd
        sug += random.choice(specs) + random.choice(string.digits)
        # 12 tadan kam bo'lsa, to'ldirish
        while len(sug) < 13:
            sug += random.choice(string.ascii_letters + string.digits + specs)
        suggestions.append(sug)
    return suggestions

# 5. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. Tokenizatsiya
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)])
    st.markdown(token_html, unsafe_allow_html=True)
    
    # 2. Statistika
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

    # 3. Tahlil
    is_ok = len(pwd) >= 12 and u_count > 0 and d_count > 0 and s_count > 0
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        # Buzish vaqti endi 0 daqiqa demaydi!
        brute_time = get_precise_brute_time(pwd)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute_time}")
        
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        st.write("Tizim talablariga javob beruvchi kuchaytirilgan variantlar:")
        
        smart_sugs = generate_limitless_suggestions(pwd)
        cols = st.columns(3)
        for i, sug in enumerate(smart_sugs):
            cols[i].markdown(f"<div class='suggestion-card'>{sug}</div>", unsafe_allow_html=True)

# 6. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-text'><b>DASTURCHI:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>NICKNAME:</b><br>LIMITLESS</p>", unsafe_allow_html=True)

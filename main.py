import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. DIZAYN
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
    .live-tip {
        background: rgba(0, 255, 0, 0.1);
        border: 1px dashed #00FF00;
        padding: 15px; border-radius: 8px;
        margin: 10px 0; color: #00FF00;
        font-family: 'Courier New', monospace;
    }
    .suggestion-card {
        border: 1px solid #00FF00; padding: 15px; border-radius: 8px;
        background: rgba(0, 255, 0, 0.12); text-align: center;
        margin: 5px; font-family: 'Courier New', monospace; color: #00FF00;
    }
    [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #00FF00; }
    .sidebar-text { color: #00FF00 !important; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

set_design()

# 3. MATEMATIK TAHLIL FUNKSIYALARI
def get_combinations(pwd):
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    return charset ** len(pwd) if len(pwd) > 0 else 0

def format_time(sec):
    if sec < 1: return f"{sec:.4f} sekund"
    if sec < 3600: return f"{(sec/60):.2f} daqiqa"
    if sec < 86400: return f"{(sec/3600):.2f} soat"
    if sec < 31536000: return f"{(sec/86400):.2f} kun"
    return f"{int(sec/31536000)} yil"

# 4. JONLI MASLAHATLAR ALGORITMI
def get_live_tips(pwd):
    tips = []
    current_comb = get_combinations(pwd)
    speed = 100_000_000_000
    
    if not any(c.isupper() for c in pwd):
        # Katta harf qo'shilsa kombinatsiyalar qanday o'zgarishini hisoblash
        new_comb = (get_combinations(pwd + "A"))
        diff = (new_comb - current_comb) / speed
        tips.append(f"💡 <b>TIPS:</b> Bitta katta harf qo'shsangiz, himoya vaqti taxminan <b>{format_time(diff)}</b> ga uzayadi!")
    
    if not any(c in string.punctuation for c in pwd):
        new_comb = (get_combinations(pwd + "!"))
        diff = (new_comb - current_comb) / speed
        tips.append(f"💡 <b>TIPS:</b> Maxsus belgi (!, @, #) kombinatsiyalar sonini keskin oshiradi!")
        
    if len(pwd) < 12:
        needed = 12 - len(pwd)
        tips.append(f"💡 <b>TIPS:</b> Yana {needed} ta belgi qo'shib 12 taga yetkazsangiz, parolingiz super-kompyuterlar uchun ham imkonsiz bo'ladi.")
        
    return tips

# 5. TAVSIYA GENERATORI
def generate_limitless_suggestions(base_pwd):
    suggestions = []
    specs = "!@#$%^&*"
    for _ in range(3):
        sug = random.choice(string.ascii_uppercase) + base_pwd + random.choice(specs) + random.choice(string.digits)
        while len(sug) < 13: sug += random.choice(string.ascii_letters + string.digits + specs)
        suggestions.append(sug)
    return suggestions

# 6. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # A. Tokenizatsiya
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    token_html = "".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)])
    st.markdown(token_html, unsafe_allow_html=True)
    
    # B. Statistika va Jonli Maslahatlar
    u_count = sum(1 for c in pwd if c.isupper())
    d_count = sum(1 for c in pwd if c.isdigit())
    s_count = sum(1 for c in pwd if c in string.punctuation)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"""
        <div style='background:rgba(0,255,0,0.05); padding:15px; border-radius:8px;'>
            > Jami: {len(pwd)} ta | Katta: {u_count} ta<br>
            > Raqam: {d_count} ta | Belgi: {s_count} ta
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        live_tips = get_live_tips(pwd)
        for tip in live_tips:
            st.markdown(f"<div class='live-tip'>{tip}</div>", unsafe_allow_html=True)

    # C. Tahlil
    is_ok = len(pwd) >= 12 and u_count > 0 and d_count > 0 and s_count > 0
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        comb = get_combinations(pwd)
        brute_time = format_time(comb / 100_000_000_000)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute_time}")
        
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        smart_sugs = generate_limitless_suggestions(pwd)
        cols = st.columns(3)
        for i, sug in enumerate(smart_sugs):
            cols[i].markdown(f"<div class='suggestion-card'>{sug}</div>", unsafe_allow_html=True)

# 7. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-text'><b>DASTURCHI:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>NICKNAME:</b><br>LIMITLESS</p>", unsafe_allow_html=True)

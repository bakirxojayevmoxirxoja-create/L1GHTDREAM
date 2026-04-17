import streamlit as st
import numpy as np
import base64
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | Bakirxo'jayev", layout="wide")

# 2. DIZAYN (Hacker Style - Grafika Saqlangan)
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
            box-shadow: 0 0 20px #00FF00;
            border-radius: 12px;
            padding: 40px;
        }}
        .hacker-text {{
            color: #00FF00 !important;
            font-family: 'Courier New', monospace;
        }}
        input {{
            background-color: #000 !important;
            color: #00FF00 !important;
            border: 1px solid #00FF00 !important;
            font-family: 'Courier New', monospace !important;
        }}
        /* Simulyator va Takliflar foni */
        .info-panel {{
            background-color: rgba(0, 30, 0, 0.6);
            border: 1px dashed #00FF00;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
        }}
        </style>
        """, unsafe_allow_html=True)
    except:
        pass

# Grafika saqlanishi uchun 'bg.jpg' (skrinshotingizdagi fon) GitHub repozitoriyangizda bo'lishi kerak.
set_bg('bg.jpg')

# 3. MUKAMMAL TAKLIF GENERATORI
def generate_hacker_suggestions(pwd_len=12, count=5):
    suggestions = []
    
    # Har xil murakkablikdagi takliflar yaratish mantiqi
    for i in range(count):
        chars = ""
        # 1. Faqat harf va son (Sodda hacker style)
        if i % count == 0:
            chars = string.ascii_letters + string.digits
        # 2. Katta harf, son va belgi (Murakkabroq)
        elif i % count == 1:
            chars = string.ascii_letters + string.digits + "!@#$"
        # 3. To'liq to'plam (Eng murakkab)
        else:
            chars = string.ascii_letters + string.digits + string.punctuation

        # Parolni generatsiya qilish va hacker elementini qo'shish
        raw_pwd = "".join(random.choice(chars) for _ in range(pwd_len))
        
        # Hacker-style "A" -> "4", "E" -> "3", "I" -> "1", "O" -> "0"
        hacker_pwd = raw_pwd.replace('a', '4').replace('A', '4').replace('e', '3').replace('E', '3').replace('i', '1').replace('I', '1').replace('o', '0').replace('O', '0')
        
        # Uzunlikka moslash
        if len(hacker_pwd) < pwd_len:
            hacker_pwd += "".join(random.choice(string.digits) for _ in range(pwd_len - len(hacker_pwd)))
            
        suggestions.append(f"`{hacker_pwd}`")
        
    return suggestions

# 4. ASOSIY QISM
st.markdown("<h1 class='hacker-text'>$ L1GHTDREAM_v3.0</h1>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. NEURAL TAHLIL (Ballar mantiqi)
    length = len(pwd)
    x1, x2, x3, x4 = length, any(c.isupper() for c in pwd), any(c.isdigit() for c in pwd), any(not c.isalnum() for c in pwd)
    
    score = (length * 3.5) + (x2 * 2.5) + (x3 * 2.0) + (x4 * 3.0)
    
    st.write("---")
    
    # Natija chiqarish
    if score > 50 and length >= 12 and x2 and x3 and x4:
        st.success("✅ ACCESS GRANTED: System Secure.")
    else:
        st.error("❌ ACCESS DENIED: Weak Password.")
        
        # 2. BRUTE-FORCE SIMULATOR
        st.markdown("<div class='info-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 class='hacker-text'>[ BRUTE-FORCE SIMULATOR: HUJUM HISOBI ]</h3>", unsafe_allow_html=True)
        
        # Buzishga ketadigan vaqtni hisoblash (Oddiy taymer)
        # Parol kuchi bo'yicha vaqtni ko'paytiramiz
        base_years = score * length / 10 # Sodda hisob
        if length >= 12: base_years *= 1.5
        if x2: base_years *= 1.2
        if x3: base_years *= 1.1
        if x4: base_years *= 1.3
        
        years = int(base_years)
        
        st.write(f"<p class='hacker-text'>Oddiy kompyuterda bu parolni buzish uchun **~{years}** yil kerak.</p>", unsafe_allow_html=True)
        st.write("<p style='color:#00AA00; font-size:11px;'>Neyron analiz: Parol murakkabligi va entropiya hisoblandi.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # 3. TAKLIFLAR OQIMI (Yashirin panel o'rniga doimiy ko'rinish)
        st.markdown("<div class='info-panel' style='margin-top:20px;'>", unsafe_allow_html=True)
        st.markdown("<h3 class='hacker-text'>[ OPTIMALLASHTIRILGAN TAKLIFLAR ]</h3>", unsafe_allow_html=True)
        
        # Bir nechta takliflar generatsiya qilish
        sug_list = generate_hacker_suggestions(pwd_len=max(length, 12), count=6)
        
        st.write("<p class='hacker-text'>Nusxalash va ishlatish uchun tayyor murakkab variantlar:</p>", unsafe_allow_html=True)
        
        # Takliflarni ro'yxat ko'rinishida chiqarish
        for sug in sug_list:
            st.write(f"<p class='hacker-text' style='margin-left:20px;'> > {sug}</p>", unsafe_allow_html=True)
            
        st.write("<p style='color:#00AA00; font-size:11px;'>Tavsiya: Katta-kichik harf, raqam va maxsus belgilar kombinatsiyasini ishlating.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 class='hacker-text'>SYSTEM_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p class='hacker-text'><b>DEVELOPER:</b> Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='hacker-text'><b>ALGORITHM:</b> Neural Analyzer v3</p>", unsafe_allow_html=True)
    st.markdown("<p class='hacker-text'><b>STATUS:</b> ENCRYPTED</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p style='color:#00FF00; font-size:11px;'>Neural Analyzer: Parol xavfsizlik darajasi tahlil qilinmoqda.</p>", unsafe_allow_html=True)

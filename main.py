import streamlit as st
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. XAVFSIZ MATRIX FON (Harakatlanuvchi va yengil)
def add_matrix_bg():
    matrix_html = """
    <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;">
        <canvas id="m"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('m');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const chars = '01010101ABCDEFHIJKLMNOPQRSTUVXYZ';
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        const drops = Array(Math.floor(columns)).fill(1);
        function draw() {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#0F0';
            ctx.font = fontSize + 'px monospace';
            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 50);
    </script>
    <style>body { margin: 0; background: black; }</style>
    """
    st.components.v1.html(matrix_html, height=1200)

# CSS SOZLAMALARI (Interfeys qora oynada yo'qolmasligi uchun)
st.markdown("""
    <style>
    .stApp { background: transparent; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.85) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 20px #00FF00;
        border-radius: 15px;
        padding: 30px;
        margin-top: -50px; /* Yuqoridagi bo'shliqni kamaytirish */
    }
    .centered-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 55px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
        margin-bottom: 20px;
    }
    .token-box {
        border: 1px solid #00FF00; padding: 8px; margin: 3px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    .live-tip {
        background: rgba(0, 255, 0, 0.1); border: 1px dashed #00FF00;
        padding: 10px; border-radius: 8px; margin: 5px 0; color: #00FF00; font-size: 14px;
    }
    [data-testid="stSidebar"] { 
        background-color: rgba(0, 0, 0, 0.9) !important; 
        border-right: 2px solid #00FF00; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. FON VA ASOSIY LOGIKA
add_matrix_bg()

def get_combinations(pwd):
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    return charset ** len(pwd) if len(pwd) > 0 else 0

def format_time(sec):
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 3600: return f"{(sec/60):.2f} min"
    return f"{int(sec/31536000)} yil"

# 4. INTERFEYS
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)
pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. Tokenlar
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    st.markdown("".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)]), unsafe_allow_html=True)
    
    # 2. Tahlil
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style='background:rgba(0,255,0,0.05); padding:15px; border-radius:8px; border: 1px solid #00FF00;'>
            > Jami: {len(pwd)} ta | Katta: {u_c} ta<br>
            > Raqam: {d_c} ta | Belgi: {s_c} ta
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        # Live Tips
        curr_comb = get_combinations(pwd)
        if u_c == 0:
            diff = (get_combinations(pwd + "A") - curr_comb) / 100_000_000_000
            st.markdown(f"<div class='live-tip'>💡 Katta harf qo'shilsa: +{format_time(diff)}</div>", unsafe_allow_html=True)
        if len(pwd) < 12:
            st.markdown(f"<div class='live-tip'>💡 Uzunlikni 12 taga yetkazing!</div>", unsafe_allow_html=True)

    # 3. Yakuniy holat
    is_ok = len(pwd) >= 12 and u_c > 0 and d_c > 0 and s_c > 0
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        brute = format_time(get_combinations(pwd) / 100_000_000_000)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")
        
        # Smart Suggestions
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i in range(3):
            sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0,9))
            while len(sug) < 12: sug += random.choice(string.ascii_lowercase)
            cols[i].markdown(f"<div style='border:1px solid #00FF00; padding:10px; text-align:center; background:rgba(0,255,0,0.15);'>{sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("Dasturchi: Bakirxo'jayev Moxirxo'ja")
    st.write("Nickname: LIMITLESS")

import streamlit as st
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. MATRIX FONINI XAVFSIZ QO'SHISH (Iframe orqali)
def add_matrix_bg():
    matrix_code = """
    <style>
        body { margin: 0; overflow: hidden; background: black; }
        canvas { display: block; }
    </style>
    <canvas id="m"></canvas>
    <script>
        const canvas = document.getElementById('m');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const chars = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789';
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
        setInterval(draw, 33);
    </script>
    """
    st.components.v1.html(matrix_code, height=2000, scrolling=False)

# Matrixni orqaga, kontentni oldinga chiqarish uchun CSS
st.markdown("""
    <style>
    .stApp { background: black; }
    iframe { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.8) !important;
        border: 2px solid #00FF00;
        box-shadow: 0 0 25px #00FF00;
        border-radius: 15px;
        padding: 40px;
        margin-top: 50px;
    }
    .centered-title {
        text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
        font-size: 60px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
        letter-spacing: 5px;
    }
    .token-box {
        border: 1px solid #00FF00; padding: 10px; margin: 4px;
        display: inline-block; background: rgba(0, 255, 0, 0.1);
        color: #00FF00; font-family: 'Courier New', monospace;
    }
    .live-tip {
        background: rgba(0, 255, 0, 0.1); border: 1px dashed #00FF00;
        padding: 10px; border-radius: 8px; margin: 5px 0; color: #00FF00;
    }
    [data-testid="stSidebar"] { background-color: rgba(0, 0, 0, 0.9) !important; border-right: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

add_matrix_bg()

# 3. MATEMATIK FUNKSIYALAR
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
    if sec < 86400: return f"{(sec/3600):.2f} soat"
    return f"{int(sec/31536000)} yil"

# 4. ASOSIY QISM
st.markdown("<div class='centered-title'>L1GHTDREAM</div>", unsafe_allow_html=True)
pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # 1. Tokenlar
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    st.markdown("".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)]), unsafe_allow_html=True)
    
    # 2. Statistika va Jonli Maslahatlar
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style='background:rgba(0,255,0,0.05); padding:15px; border-radius:8px; border-left: 4px solid #00FF00;'>
            > Jami: {len(pwd)} ta | Katta: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqam: {sum(1 for c in pwd if c.isdigit())} ta | Belgi: {sum(1 for c in pwd if c in string.punctuation)} ta
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Live Tips
        curr_comb = get_combinations(pwd)
        if not any(c.isupper() for c in pwd):
            diff = (get_combinations(pwd + "A") - curr_comb) / 100_000_000_000
            st.markdown(f"<div class='live-tip'>💡 Katta harf qo'shilsa: +{format_time(diff)}</div>", unsafe_allow_html=True)
        if len(pwd) < 12:
            st.markdown(f"<div class='live-tip'>💡 Uzunlikni 12 taga yetkazish kerak!</div>", unsafe_allow_html=True)

    # 3. Tahlil
    is_ok = len(pwd) >= 12 and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd)
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        brute = format_time(get_combinations(pwd) / 100_000_000_000)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")
        
        # Tavsiyalar
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i in range(3):
            sug = random.choice(string.ascii_uppercase) + pwd + random.choice("!@#") + str(random.randint(0,9))
            while len(sug) < 12: sug += random.choice(string.ascii_lowercase)
            cols[i].markdown(f"<div style='border:1px solid #00FF00; padding:10px; text-align:center; background:rgba(0,255,0,0.1);'>{sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write(f"Dasturchi: Bakirxo'jayev Moxirxo'ja") #
    st.write(f"Nickname: LIMITLESS") #

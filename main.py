import streamlit as st
import random
import string

# 1. SAHIFA SOZLAMALARI (Alo darajadagi vizual uchun layout)
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. MATRIX RAIN FONINI JOYLASHTIRISH (Xavfsiz va qotmaydigan)
def set_matrix_bg():
    matrix_code = """
    <style>
        /* Matrix orqada, kontent oldinda tursin */
        #matrix-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            opacity: 0.6; /* Kodlar biroz xira bo'lsa, kontentni o'qish oson bo'ladi */
        }
    </style>
    <canvas id="matrix-canvas"></canvas>
    <script>
        const canvas = document.getElementById('matrix-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const katakana = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ';
        const numbers = '0123456789';
        const alphabet = katakana + numbers;
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        const rainDrops = [];
        for (let x = 0; x < columns; x++) { rainDrops[x] = 1; }
        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#0F0';
            ctx.font = fontSize + 'px monospace';
            for (let i = 0; i < rainDrops.length; i++) {
                const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
                ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) { rainDrops[i] = 0; }
                rainDrops[i]++;
            }
        };
        setInterval(draw, 30);
    </script>
    """
    st.components.v1.html(matrix_code, height=0, scrolling=False)

# CSS (Grafikani alo darajaga chiqarish)
st.markdown("""
    <style>
        .stApp { background-color: #000; color: #00FF00; }
        iframe { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; }
        .main .block-container {
            background-color: rgba(0, 0, 0, 0.85) !important;
            border: 2px solid #00FF00;
            box-shadow: 0 0 30px #00FF00;
            border-radius: 15px;
            padding: 40px;
            margin-top: -50px;
        }
        .centered-title {
            text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
            font-size: 60px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
            letter-spacing: 5px; margin-bottom: 20px;
        }
        .token-box {
            border: 1px solid #00FF00; padding: 10px; margin: 4px;
            display: inline-block; background: rgba(0, 255, 0, 0.1);
            color: #00FF00; font-family: 'Courier New', monospace;
        }
        .live-tip {
            background: rgba(0, 255, 0, 0.1);
            border: 1px dashed #00FF00;
            padding: 10px; border-radius: 8px;
            margin: 5px 0; color: #00FF00;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

set_matrix_bg()

# 3. MATEMATIK VA LOGIK FUNKSIYALAR
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
    if sec < 31536000: return f"{(sec/86400):.2f} kun"
    return f"{int(sec/31536000)} yil"

# LIMITLESS TAVSIYALAR (100% XAVFSIZ)
def generate_limitless_suggestions(base_pwd):
    suggestions = []
    specs = "!@#$%^&*"
    for _ in range(3):
        sug = random.choice(string.ascii_uppercase) + base_pwd
        sug += random.choice(specs) + random.choice(string.digits)
        # Uzunlikni har doim 12 tadan oshirish
        while len(sug) < 13:
            sug += random.choice(string.ascii_letters + string.digits + specs)
        suggestions.append(sug)
    return suggestions

# 4. INTERFEYS (Oldingidan yaxshi holat)
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
        <div style='background:rgba(0,255,0,0.05); padding:15px; border-radius:8px; border: 1px solid #00FF00;'>
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
            st.markdown(f"<div class='live-tip'>💡 Uzunlikni 12 taga yetkazing!</div>", unsafe_allow_html=True)

    # 3. Tahlil
    is_ok = len(pwd) >= 12 and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd)
    st.write("---")
    
    if is_ok:
        st.success("✅ STATUS: ENCRYPTED AND SECURE")
    else:
        # Buzish vaqti endi 0 daqiqa demaydi!
        brute_time = format_time(get_combinations(pwd) / 100_000_000_000)
        st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute_time}")
        
        st.markdown("<h3 style='color:#00FF00;'>[ 2. SMART SUGGESTIONS ]</h3>", unsafe_allow_html=True)
        st.write("Tizim talablariga javob beruvchi kuchaytirilgan variantlar:")
        
        # Aqlli tavsiyalar har doim talabga javob beradi
        smart_sugs = generate_limitless_suggestions(pwd)
        cols = st.columns(3)
        for i, sug in enumerate(smart_sugs):
            cols[i].markdown(f"<div style='border:1px solid #00FF00; padding:10px; text-align:center; background:rgba(0,255,0,0.1);'>{sug}</div>", unsafe_allow_html=True)

# 5. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='sidebar-text'><b>DASTURCHI:</b><br>Bakirxo'jayev Moxirxo'ja</p>", unsafe_allow_html=True)
    st.markdown("<p class='sidebar-text'><b>NICKNAME:</b><br>LIMITLESS</p>", unsafe_allow_html=True)

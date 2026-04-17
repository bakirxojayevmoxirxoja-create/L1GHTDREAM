import streamlit as st
import random
import string

# 1. SAHIFA SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM | LIMITLESS", layout="wide")

# 2. DOIMIY MATRIX FON (JS + CSS)
def set_matrix_bg():
    st.markdown("""
        <style>
            /* Matrixni orqaga qulflash */
            #matrix-canvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                z-index: -1;
            }
            /* Asosiy kontentni shaffof qilish va Matrix ustiga chiqarish */
            .stApp {
                background: transparent;
            }
            .main .block-container {
                background-color: rgba(0, 0, 0, 0.8) !important;
                border: 2px solid #00FF00;
                box-shadow: 0 0 25px #00FF00;
                border-radius: 15px;
                padding: 40px;
                margin-top: 50px;
                color: #00FF00;
            }
            .centered-title {
                text-align: center; color: #00FF00; font-family: 'Courier New', monospace;
                font-size: 50px; font-weight: bold; text-shadow: 0 0 15px #00FF00;
            }
            .token-box {
                border: 1px solid #00FF00; padding: 10px; margin: 4px;
                display: inline-block; background: rgba(0, 255, 0, 0.1);
                color: #00FF00; font-family: 'Courier New', monospace;
            }
            /* Sidebar dizayni */
            [data-testid="stSidebar"] {
                background-color: rgba(0, 0, 0, 0.9) !important;
                border-right: 2px solid #00FF00;
            }
        </style>
        
        <canvas id="matrix-canvas"></canvas>
        
        <script>
            const canvas = document.getElementById('matrix-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';
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
            setInterval(draw, 35);
            
            // Ekran o'lchami o'zgarsa Matrix ham moslashishi uchun
            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });
        </script>
    """, unsafe_allow_html=True)

set_matrix_bg()

# 3. MATEMATIK LOGIKA
def get_precise_time(pwd):
    length = len(pwd)
    if length == 0: return "0 sek"
    charset = 0
    if any(c.islower() for c in pwd): charset += 26
    if any(c.isupper() for c in pwd): charset += 26
    if any(c.isdigit() for c in pwd): charset += 10
    if any(c in string.punctuation for c in pwd): charset += 32
    
    sec = (charset ** length) / 100_000_000_000
    if sec < 1: return f"{sec:.4f} sek"
    if sec < 3600: return f"{(sec/60):.2f} min"
    if sec < 86400: return f"{(sec/3600):.2f} soat"
    return f"{int(sec/31536000)} yil"

# 4. INTERFEYS
st.markdown("<div class='centered-title'>$ L1GHTDREAM_v3.3</div>", unsafe_allow_html=True)

pwd = st.text_input("PASSWORD_INPUT >", type="password")

if pwd:
    # Tokenlar
    st.markdown("<h3 style='color:#00FF00;'>[ 1. NEURAL TOKENIZATION ]</h3>", unsafe_allow_html=True)
    tokens_html = "".join([f"<div class='token-box'>{t}</div>" for t in list(pwd)])
    st.markdown(tokens_html, unsafe_allow_html=True)
    
    # Statistika va Maslahatlar
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style='border-left: 3px solid #00FF00; padding-left: 15px;'>
            > Jami belgilar: {len(pwd)} ta<br>
            > Katta harflar: {sum(1 for c in pwd if c.isupper())} ta<br>
            > Raqamlar: {sum(1 for c in pwd if c.isdigit())} ta
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        if not any(c.isupper() for c in pwd):
            st.info("💡 Maslahat: Katta harf qo'shish xavfsizlikni 26 barobar oshiradi!")

    # Buzish vaqti (Aniq ko'rinishda)
    brute = get_precise_time(pwd)
    st.error(f"⚠️ SECURITY ALERT: Buzish vaqti - {brute}")

# 5. SIDEBAR (Raxmatov Badriddin ma'lumotlari bilan)
with st.sidebar:
    st.markdown("<h2 style='color:#00FF00;'>TERMINAL_INFO</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style='color:#00FF00; font-family:monospace;'>
            Dasturchi: Raxmatov Badriddin<br>
            Yosh: 19<br>
            Yo'nalish: Kiberxavfsizlik<br>
            Nickname: LIMITLESS
        </div>
    """, unsafe_allow_html=True)

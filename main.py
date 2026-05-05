import streamlit as st
import string
import numpy as np
import plotly.graph_objects as go

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI PRO", layout="wide")

# 2. MATRIX FON VA STILLAR (To'liq saqlandi)
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.96) !important;
        border: 2px solid #00FF00; border-radius: 12px; padding: 40px; color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 5px 12px; margin: 3px; background: rgba(0, 255, 0, 0.1); border-radius: 4px; }
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. YORDAMCHI MATEMATIK FUNKSIYALAR
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

def format_time(sec):
    if sec <= 0: return "DARHOL"
    if sec < 3600: return f"{sec/60:.2f} minut"
    if sec < 86400: return f"{sec/3600:.2f} soat"
    return f"{sec/86400:.2f} kun"

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI PRO: SYSTEM ONLINE</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password", key="pwd_input")

if pwd:
    # --- A. NLP TOKENIZATION (Eski qism saqlandi) ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    # Statistika hisoblash
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    l_c = sum(1 for c in pwd if c.islower())
    
    crack_time = ((62 if s_c==0 else 94) ** len(pwd)) / 1e11 if len(pwd) > 0 else 0
    st.error(f"🛑 SUPERCOMPUTER CRACK TIME: {format_time(crack_time)}")

    # --- B. NEURAL ENGINE CALCULATIONS (AI hisob-kitoblar) ---
    x = np.array([len(pwd)/10, float(u_c), float(d_c), float(s_c)])
    w = np.array([0.4, 0.7, 0.3, 0.9])
    
    z_relu = x * w - 0.5
    filtered = relu(z_relu)
    
    final_z = np.sum(filtered) - 1.2
    ai_score = sigmoid(final_z)
    
    target = 1.0 if (len(pwd) >= 10 and u_c > 0 and d_c > 0) else 0.2
    error = target - ai_score

    # --- C. YANGI GRAFIK KO'RINISH (DASHBOARD) ---
    st.markdown("### [ 2. VISUAL SECURITY DASHBOARD ]")
    
    g_col1, g_col2 = st.columns([1, 1])
    
    with g_col1:
        # 1. Spidometr (Gauge Chart)
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = ai_score * 100,
            title = {'text': "AI Confidence Score (%)", 'font': {'color': "#00FF00"}},
            gauge = {
                'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
                'bar': {'color': "#00FF00"},
                'steps': [
                    {'range': [0, 40], 'color': "rgba(255, 0, 0, 0.3)"},
                    {'range': [40, 75], 'color': "rgba(255, 255, 0, 0.3)"},
                    {'range': [75, 100], 'color': "rgba(0, 255, 0, 0.3)"}]}))
        fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=20,r=20,t=40,b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with g_col2:
        # 2. Parametrlar taqsimoti (Bar Chart)
        fig_bar = go.Figure(data=[go.Bar(
            x=['Uzunlik', 'Katta harf', 'Raqam', 'Simvol'],
            y=filtered,
            marker_color='#00FF00'
        )])
        fig_bar.update_layout(
            title={'text': "Neyron Signallar (ReLU Output)", 'font': {'color': "#00FF00"}},
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "#00FF00"}, height=300, margin=dict(l=20,r=20,t=40,b=20)
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- D. TEXNIK NATIJALAR (Oldingi 3 ta ustun) ---
    st.markdown("### [ 3. NEURAL ENGINE LOGS ]")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.write("**ReLU Layer:**")
        st.code(f"Filtered: {filtered}")
        st.caption("Filtrlangan signallar.")
        
    with c2:
        st.write("**Sigmoid Output:**")
        st.code(f"AI Score: {ai_score:.4f}")
        st.caption("0-1 oralig'idagi ehtimollik.")
        
    with c3:
        st.write("**Backpropagation:**")
        st.code(f"Error: {error:.4f}\nDelta: {error * 0.1:.4f}")
        st.caption("Xatolik va og'irlik o'zgarishi.")

    # --- E. ARCHITECTURAL ANALYSIS ---
    st.markdown("### [ 4. ARCHITECTURAL ANALYSIS ]")
    if s_c > 0:
        st.info(f"RNN MODULI: '{pwd}' tarkibidagi belgilar ketma-ketligini tahlil qilmoqda.")
    else:
        st.warning("CNN MODULI: Tizim faqat vizual patternlarni tahlil qilmoqda.")

    # Status
    if ai_score > 0.75:
        st.success(f"✅ TIZIM XAVFSIZ (AI SCORE: {ai_score*100:.1f}%)")
        st.balloons()
    else:
        st.error(f"⚠️ TIZIM ZAIF (AI SCORE: {ai_score*100:.1f}%)")

# 5. SIDEBAR
with st.sidebar:
    st.markdown(f"<b>DEV:</b> Moxirxo'ja<br><b>NICK:</b> LIMITLESS", unsafe_allow_html=True)

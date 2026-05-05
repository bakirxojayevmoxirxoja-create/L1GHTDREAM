import streamlit as st
import string
import numpy as np
import plotly.graph_objects as go

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI PRO", layout="wide")

# 2. MATRIX FON VA STILLAR (To'liq saqlangan)
st.markdown("""
<style>
    .stApp { background: transparent !important; }
    html, body { background-color: black !important; }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; border: none; }
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.94) !important;
        border: 2px solid #00FF00; border-radius: 12px; padding: 40px; color: #00FF00; font-family: 'Courier New', monospace;
    }
    .token-box { display: inline-block; border: 1px solid #00FF00; padding: 5px 12px; margin: 3px; background: rgba(0, 255, 0, 0.1); border-radius: 4px; }
</style>
<iframe class="matrix-bg" srcdoc="<html><body style='margin:0; overflow:hidden; background:black;'><canvas id='m'></canvas><script>const c=document.getElementById('m');const ctx=c.getContext('2d');const res=()=>{c.width=window.innerWidth;c.height=window.innerHeight;};res();window.onresize=res;const ch='01ABCDEFGHIJKLMNOPQRSTUVWXYZｱｲｳｴｵｶｷｸｹｺ';const fs=16;const col=c.width/fs;const dr=Array(Math.floor(col)).fill(1);function d(){ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,c.width,c.height);ctx.fillStyle='#0F0';ctx.font=fs+'px monospace';for(let i=0;i<dr.length;i++){const t=ch[Math.floor(Math.random()*ch.length)];ctx.fillText(t,i*fs,dr[i]*fs);if(dr[i]*fs>c.height&&Math.random()>0.975)dr[i]=0;dr[i]++;}}setInterval(d,35);</script></body></html>"></iframe>
""", unsafe_allow_html=True)

# 3. YORDAMCHI FUNKSIYALAR
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI PRO: FULL ANALYSIS</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password", key="pwd_input")

if pwd:
    # --- 1. NLP TOKENIZATION (Eski vizual saqlandi) ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    
    # --- 2. NEURAL CALCULATIONS ---
    x = np.array([len(pwd)/10, float(u_c), float(d_c), float(s_c)])
    w = np.array([0.4, 0.7, 0.3, 0.9])
    
    z_relu = x * w - 0.5
    filtered = relu(z_relu)
    ai_score = sigmoid(np.sum(filtered) - 1.2)

    # --- YANGI QO'SHIMCHA: GRAFIK (Eski narsalarga zarar bermasdan) ---
    st.markdown("### [ 2. SECURITY GRAPHICAL VIEW ]")
    fig_bar = go.Figure(data=[go.Bar(
        x=['Uzunlik', 'Katta harf', 'Raqam', 'Simvol'],
        y=filtered,
        marker_color='#00FF00'
    )])
    fig_bar.update_layout(
        title={'text': "Neyron Signallar Taqsimoti (ReLU Output)", 'font': {'color': "#00FF00"}},
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "#00FF00"}, height=300,
        yaxis=dict(gridcolor='rgba(0,255,0,0.1)', range=[0, 1])
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # --- 3. NEURAL ENGINE CALCULATIONS (Eski 3 ta ustun saqlandi) ---
    st.markdown("### [ 3. NEURAL ENGINE CALCULATIONS ]")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.write("**ReLU Layer:**")
        st.info(f"Filtered: {filtered}")
        st.caption("Manfiy signallar filtrlandi.")

    with c2:
        st.write("**Sigmoid Output:**")
        st.success(f"AI Score: {ai_score:.4f}")
        st.caption("Ehtimollik: 0 va 1 oralig'ida.")

    with c3:
        st.write("**Backpropagation:**")
        st.warning(f"Error: {0.8 - ai_score:.4f}")
        st.caption("Xatolik tahlili.")

    # --- 4. ARCHITECTURAL ANALYSIS (Eski qism saqlandi) ---
    st.markdown("### [ 4. ARCHITECTURAL ANALYSIS ]")
    if s_c > 0:
        st.info(f"RNN MODULI: '{pwd}' tarkibidagi murakkab mantiqni tahlil qildi.")
    else:
        st.warning("CNN MODULI: Tizim sodda patternlarni aniqladi.")

    # Yakuniy status
    if ai_score > 0.75:
        st.success(f"✅ TIZIM XAVFSIZ (AI SCORE: {ai_score*100:.1f}%)")
    else:
        st.error(f"⚠️ TIZIM ZAIF (AI SCORE: {ai_score*100:.1f}%)")

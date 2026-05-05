import streamlit as st
import string
import numpy as np
import plotly.graph_objects as go

# 1. TIZIM SOZLAMALARI
st.set_page_config(page_title="L1GHTDREAM AI PRO", layout="wide")

# 2. MATRIX FON VA STILLAR (Saqlab qolindi)
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

# 3. YORDAMCHI FUNKSIYALAR
def sigmoid(x): return 1 / (1 + np.exp(-x))
def relu(x): return np.maximum(0, x)

# 4. ASOSIY INTERFEYS
st.markdown("<h1 style='text-align:center;'>L1GHTDREAM AI PRO: GRAPHICAL ANALYSIS</h1>", unsafe_allow_html=True)
pwd = st.text_input("ENTER ACCESS KEY >", type="password", key="pwd_input")

if pwd:
    # --- A. NLP TOKENIZATION ---
    st.markdown("### [ 1. NLP TOKENIZATION ]")
    tokens_html = "".join([f"<div class='token-box'>{char}</div>" for char in pwd])
    st.markdown(f"<div>{tokens_html}</div>", unsafe_allow_html=True)
    
    # Parametrlarni hisoblash
    u_c = sum(1 for c in pwd if c.isupper())
    d_c = sum(1 for c in pwd if c.isdigit())
    s_c = sum(1 for c in pwd if c in string.punctuation)
    l_c = sum(1 for c in pwd if c.islower())
    
    # --- B. NEURAL CALCULATIONS ---
    x = np.array([len(pwd)/10, float(u_c), float(d_c), float(s_c)])
    w = np.array([0.4, 0.7, 0.3, 0.9])
    filtered = relu(x * w - 0.5)
    ai_score = sigmoid(np.sum(filtered) - 1.2)

    # --- C. GRAFIK KO'RINISH (YANGI QISM) ---
    st.markdown("### [ 2. VISUAL SECURITY DASHBOARD ]")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # 1. Gauge Chart (Spidometr ko'rinishidagi grafik)
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = ai_score * 100,
            title = {'text': "AI Security Score (%)", 'font': {'color': "#00FF00"}},
            gauge = {
                'axis': {'range': [0, 100], 'tickcolor': "#00FF00"},
                'bar': {'color': "#00FF00"},
                'steps': [
                    {'range': [0, 40], 'color': "rgba(255, 0, 0, 0.3)"},
                    {'range': [40, 75], 'color': "rgba(255, 255, 0, 0.3)"},
                    {'range': [75, 100], 'color': "rgba(0, 255, 0, 0.3)"}],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "#00FF00"})
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col2:
        # 2. Bar Chart (Parametrlar taqsimoti)
        fig_bar = go.Figure(data=[go.Bar(
            x=['Uzunlik', 'Katta harf', 'Raqam', 'Belgi'],
            y=filtered,
            marker_color='#00FF00'
        )])
        fig_bar.update_layout(
            title={'text': "Neyron Signallar Filtratsiyasi (ReLU)", 'font': {'color': "#00FF00"}},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "#00FF00"},
            yaxis=dict(gridcolor='rgba(0,255,0,0.1)')
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- D. TEPADAGI NATIJALARNI SAQLAB QOLISH ---
    st.markdown("### [ 3. TECHNICAL LOGS ]")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**ReLU Layer:**")
        st.code(f"Filtered: {filtered}")
    with c2:
        st.write("**Sigmoid Output:**")
        st.code(f"AI Score: {ai_score:.4f}")
    with c3:
        st.write("**Architecture:**")
        st.info("RNN Moduli faol" if len(pwd) > 8 else "CNN Moduli faol")

    if ai_score > 0.75:
        st.success("✅ TIZIM XAVFSIZ")
        st.balloons()
    else:
        st.error("⚠️ TIZIM ZAIF")

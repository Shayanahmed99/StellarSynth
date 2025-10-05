import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="🌌 Exoplanet Explorer",
    page_icon="🪐",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #0a0e27 0%, #1a1b3d 50%, #2d1b4e 100%);
        font-family: 'Press Start 2P', cursive;
    }
    
    .main-header {
        font-family: 'Press Start 2P', cursive;
        font-size: 2.5rem;
        color: #00ffff;
        text-align: center;
        text-shadow: 0 0 20px #00ffff, 0 0 40px #ff00ff;
        margin-bottom: 1rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #ff00ff; }
        to { text-shadow: 0 0 20px #00ffff, 0 0 30px #00ffff, 0 0 40px #ff00ff; }
    }
    
    .subtitle {
        font-family: 'Press Start 2P', cursive;
        font-size: 0.8rem;
        color: #ffaa00;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-family: 'Press Start 2P', cursive;
        font-size: 0.8rem;
        border: 3px solid #00ffff;
        border-radius: 10px;
        padding: 15px 30px;
        box-shadow: 0 0 20px #667eea;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px #00ffff;
    }
    
    .result-box {
        background: rgba(0, 255, 255, 0.1);
        border: 3px solid #00ffff;
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
    }
    
    .result-text {
        font-family: 'Press Start 2P', cursive;
        font-size: 1.2rem;
        color: #00ff88;
        text-shadow: 0 0 10px #00ff88;
    }
    
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    div[data-testid="stNumberInput"] label {
        color: #ffaa00 !important;
        font-size: 0.7rem !important;
    }
    
    div[data-testid="stNumberInput"] input {
        background: rgba(0, 0, 0, 0.5) !important;
        color: #00ffff !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stars" id="stars"></div>
<script>
const starsContainer = document.getElementById('stars');
for (let i = 0; i < 100; i++) {
    const star = document.createElement('div');
    star.style.position = 'absolute';
    star.style.width = Math.random() * 3 + 'px';
    star.style.height = star.style.width;
    star.style.backgroundColor = ['#ffffff', '#00ffff', '#ff00ff', '#ffaa00'][Math.floor(Math.random() * 4)];
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.borderRadius = '50%';
    star.style.animation = `twinkle ${Math.random() * 3 + 2}s infinite`;
    starsContainer.appendChild(star);
}
</script>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🪐 EXOPLANET EXPLORER 🌌</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">⭐ Discover New Worlds Beyond Our Solar System ⭐</p>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        model = joblib.load('xgb.joblib')
        le = joblib.load('disp_encode.joblib')
        return model, le
    except Exception as e:
        st.error(f"❌ Error loading models: {e}")
        return None, None

model, le = load_model()

features = ['pl_orbper', 'pl_trandurh', 'pl_trandep', 'pl_rade',
            'pl_insol', 'st_tmag', 'st_teff', 'st_rad']

feature_info = {
    'pl_orbper': ('🔄 Orbital Period', 'Days for one orbit', 12.34),
    'pl_trandurh': ('⏱️ Transit Duration', 'Hours of transit', 3.5),
    'pl_trandep': ('📉 Transit Depth', 'Brightness decrease', 0.0012),
    'pl_rade': ('🌍 Planet Radius', 'Earth radii units', 1.1),
    'pl_insol': ('☀️ Insolation Flux', 'Energy received', 250.6),
    'st_tmag': ('✨ Star Magnitude', 'Brightness value', 10.3),
    'st_teff': ('🌡️ Star Temperature', 'Kelvin', 5500.0),
    'st_rad': ('⭐ Star Radius', 'Solar radii units', 0.9)
}

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### 🚀")
    st.markdown("**PLANET DATA**")

with col3:
    st.markdown("### 🛸")
    st.markdown("**STAR DATA**")

with st.form("exoplanet_form"):
    st.markdown("### 🌟 Enter Observation Parameters")
    
    col_left, col_right = st.columns(2)
    
    input_data = {}
    
    with col_left:
        st.markdown("#### 🪐 **Planetary Properties**")
        input_data['pl_orbper'] = st.number_input(
            f"{feature_info['pl_orbper'][0]} ({feature_info['pl_orbper'][1]})",
            value=feature_info['pl_orbper'][2],
            format="%.2f"
        )
        input_data['pl_trandurh'] = st.number_input(
            f"{feature_info['pl_trandurh'][0]} ({feature_info['pl_trandurh'][1]})",
            value=feature_info['pl_trandurh'][2],
            format="%.2f"
        )
        input_data['pl_trandep'] = st.number_input(
            f"{feature_info['pl_trandep'][0]} ({feature_info['pl_trandep'][1]})",
            value=feature_info['pl_trandep'][2],
            format="%.6f"
        )
        input_data['pl_rade'] = st.number_input(
            f"{feature_info['pl_rade'][0]} ({feature_info['pl_rade'][1]})",
            value=feature_info['pl_rade'][2],
            format="%.2f"
        )
        input_data['pl_insol'] = st.number_input(
            f"{feature_info['pl_insol'][0]} ({feature_info['pl_insol'][1]})",
            value=feature_info['pl_insol'][2],
            format="%.2f"
        )
    
    with col_right:
        st.markdown("#### ⭐ **Stellar Properties**")
        input_data['st_tmag'] = st.number_input(
            f"{feature_info['st_tmag'][0]} ({feature_info['st_tmag'][1]})",
            value=feature_info['st_tmag'][2],
            format="%.2f"
        )
        input_data['st_teff'] = st.number_input(
            f"{feature_info['st_teff'][0]} ({feature_info['st_teff'][1]})",
            value=feature_info['st_teff'][2],
            format="%.1f"
        )
        input_data['st_rad'] = st.number_input(
            f"{feature_info['st_rad'][0]} ({feature_info['st_rad'][1]})",
            value=feature_info['st_rad'][2],
            format="%.2f"
        )
    
    submitted = st.form_submit_button("🔭 CLASSIFY EXOPLANET 🔭", use_container_width=True)

if submitted and model is not None:
    with st.spinner('🌌 Analyzing cosmic data...'):
        sample_df = pd.DataFrame([input_data], columns=features)
        prediction = model.predict(sample_df)
        decoded_label = le.inverse_transform(prediction)
        
        try:
            proba = model.predict_proba(sample_df)
            confidence = np.max(proba) * 100
        except:
            confidence = None
        
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.balloons()
        
        col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
        
        with col_res2:
            st.markdown("### 🎯 CLASSIFICATION RESULT")
            st.markdown(f'<p class="result-text">Planet Type: {decoded_label[0]}</p>', unsafe_allow_html=True)
            
            if confidence:
                st.markdown(f'<p style="color: #ffaa00; font-size: 0.8rem;">Confidence: {confidence:.1f}%</p>', unsafe_allow_html=True)
            
            st.markdown(f'<p style="color: #ff00ff; font-size: 0.7rem;">Encoded ID: {prediction[0]}</p>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.6rem;'>
    <p>🌠 Powered by XGBoost ML Algorithm 🌠</p>
    <p>Made with ❤️ for Space Exploration</p>
</div>
""", unsafe_allow_html=True)
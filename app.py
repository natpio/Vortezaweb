import streamlit as st
import time

# --- KONFIGURACJA ---
st.set_page_config(page_title="Vorteza Systems | Digital Detox", layout="wide", initial_sidebar_state="collapsed")

# --- DESIGN PREMIUM ---
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .hero-title { font-size: 4rem; font-weight: 200; text-align: center; margin-top: 5vh; letter-spacing: -2px; }
    .highlight { color: #c88141; font-weight: 400; }
    .stButton>button {
        width: 100%; background-color: #c88141; color: white; border: none; padding: 1.5rem;
        font-size: 1.3rem; font-weight: bold; border-radius: 8px; transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-3px); background-color: #e0965a; box-shadow: 0 10px 30px rgba(200, 129, 65, 0.4); }
    .vorteza-card { background: #0d0d0d; padding: 2rem; border-radius: 15px; border-left: 5px solid #c88141; }
</style>
""", unsafe_allow_html=True)

if 'transformed' not in st.session_state: st.session_state.transformed = False

# --- SCENA 1: CHAOS ---
if not st.session_state.transformed:
    st.markdown("<div class='hero-title'>Twoja firma <span class='highlight'>tonie w Excelach?</span></div>", unsafe_allow_html=True)
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        try: st.image("excel_chaos.png", use_container_width=True)
        except: st.warning("Uruchom najpierw skrypt make_chaos.py, aby stworzyć obrazek!")
        
        if st.button("ZASTĄP TEN CHAOS SYSTEMEM VORTEZA"):
            with st.spinner('TRWA TRANSFORMACJA TWOJEGO BIZNESU...'):
                time.sleep(2)
                st.session_state.transformed = True
                st.rerun()

# --- SCENA 2: VORTEZA OS ---
else:
    st.markdown("<div class='hero-title'>Vorteza Systems. <br><span class='highlight'>Biznes uwolniony.</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; margin-bottom: 50px;'>Jesteśmy butikową pracownią. Tworzymy systemy potężne, piękne i w ludzkiej cenie.</p>", unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["LOGISTYKA", "KANCELARIA", "MEDYCYNA"])
    
    with t1:
        c1, c2 = st.columns([2, 1])
        with c1: st.image("image_526749.jpg")
        with c2: st.markdown("<div class='vorteza-card'><h3>Vorteza Core</h3><p>Routing transportu. 5h planowania -> 5 min automatyzacji.</p></div>", unsafe_allow_html=True)
    
    with t2:
        c1, c2 = st.columns([2, 1])
        with c1: st.image("image_52609f.jpg")
        with c2: st.markdown("<div class='vorteza-card'><h3>Vorteza Lex</h3><p>Obieg spraw i billing. Pełna przejrzystość zysków.</p></div>", unsafe_allow_html=True)

    with t3:
        c1, c2 = st.columns([2, 1])
        with c1: st.image("image_5263a8.jpg")
        with c2: st.markdown("<div class='vorteza-card'><h3>Vorteza Med</h3><p>Radar obłożenia placówki. Koniec pomyłek na recepcji.</p></div>", unsafe_allow_html=True)

    if st.button("UMÓW ROZMOWĘ Z TWÓRCAMI"):
        st.balloons()
        st.info("Zadzwoń do nas: [Twój numer] lub napisz do żony!")

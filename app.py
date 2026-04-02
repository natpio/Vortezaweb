import streamlit as st
import time

# 1. KONFIGURACJA
st.set_page_config(page_title="Vorteza | Digital Detox", layout="wide", initial_sidebar_state="collapsed")

# 2. STYLE CSS (Mroczny, luksusowy klimat)
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    
    .main-title { font-size: 3.5rem; font-weight: 200; text-align: center; margin-top: 5vh; letter-spacing: -2px; }
    .highlight { color: #c88141; font-weight: 400; }
    
    .excel-box { border: 1px solid #333; opacity: 0.6; filter: grayscale(100%); transition: 0.5s; }
    .excel-box:hover { opacity: 1; filter: grayscale(0%); }
    
    .stButton>button {
        width: 100%;
        background-color: #c88141;
        color: white;
        border: none;
        padding: 1.5rem;
        font-size: 1.5rem;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(200, 129, 65, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); background-color: #e0965a; }

    .card { background: #111; padding: 2rem; border-radius: 15px; border-left: 4px solid #c88141; }
</style>
""", unsafe_allow_html=True)

# 3. LOGIKA TRANSFORMACJI (Session State)
if 'detoxed' not in st.session_state:
    st.session_state.detoxed = False

def perform_detox():
    st.session_state.detoxed = True

# --- SCENA 1: CHAOS (PRZED) ---
if not st.session_state.detoxed:
    st.markdown("<div class='main-title'>Twój biznes wciąż <span class='highlight'>tonie w Excelach?</span></div>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 1.2rem; color: #888;'>Chaos danych, błędy w formułach i marnowanie godzin na ręczne przepisywanie...</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        # Tutaj wstawiasz screena brzydkiego excela
        # st.image("excel.png", use_column_width=True, caption="Codzienność wielu firm...")
        st.markdown("<div style='height: 300px; background: #222; display: flex; align-items: center; justify-content: center; border: 2px dashed #444;'>[ TUTAJ WSTAW SCREENA TWOJEGO NAJGORSZEGO EXCELA ]</div>", unsafe_allow_html=True)
        
        st.write(" ")
        st.write(" ")
        
        if st.button("ZASTĄP TEN CHAOS INTELIGENTNYM SYSTEMEM"):
            with st.spinner('Trwa transformacja Twojego biznesu...'):
                time.sleep(1.5) # Efekt "ładowania" zmiany
                st.session_state.detoxed = True
                st.rerun()

# --- SCENA 2: VORTEZA OS (PO) ---
else:
    st.markdown("<div class='main-title'>Vorteza Systems. <span class='highlight'>Biznes uwolniony.</span></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; max-width: 800px; margin: 0 auto 3rem auto; font-size: 1.1rem; line-height: 1.6;'>
    Jesteśmy butikowym software house'em. Nie dostaniesz od nas faktury za biurowiec w centrum miasta. 
    Dostaniesz narzędzie, które wygląda jak luksusowy zegarek, a działa jak silnik odrzutowy.
    </p>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["LOGISTYKA (CORE)", "KANCELARIA (LEX)", "MEDYCYNA (MED)"])

    with tab1:
        c1, c2 = st.columns([2, 1])
        with c1:
             st.image("image_526749.jpg", use_column_width=True)
        with c2:
            st.markdown("<div class='card'><h3>Vorteza Core</h3><p>Routing transportu i planowanie zleceń. <b>Efekt:</b> 5h planowania skrócone do 5 minut.</p></div>", unsafe_allow_html=True)

    with tab2:
        c1, c2 = st.columns([2, 1])
        with c1:
             st.image("image_52609f.jpg", use_column_width=True)
        with c2:
            st.markdown("<div class='card'><h3>Vorteza Lex</h3><p>Zarządzanie sprawami i billing czasu pracy. <b>Efekt:</b> Pełna przejrzystość zysków na każdym etapie sprawy.</p></div>", unsafe_allow_html=True)

    with tab3:
        c1, c2 = st.columns([2, 1])
        with c1:
             st.image("image_5263a8.jpg", use_column_width=True)
        with c2:
            st.markdown("<div class='card'><h3>Vorteza Med</h3><p>Radar obłożenia placówki. <b>Efekt:</b> Recepcja, która nigdy się nie myli.</p></div>", unsafe_allow_html=True)

    st.write("---")
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("<p style='text-align: center;'>Zbudujemy Twój system szybciej niż agencja przygotuje wycenę.</p>", unsafe_allow_html=True)
        if st.button("DOWIEDZ SIĘ WIĘCEJ (BEZ ZOBOWIĄZAŃ)"):
            st.balloons()
            st.info("Tutaj Twój formularz kontaktowy lub numer telefonu!")

import streamlit as st
import time

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Vorteza Systems | Digital Detox",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. DESIGN PREMIUM (CSS HACKING) ---
st.markdown("""
<style>
    /* Ukrycie elementów Streamlita */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Globalny styl - Głęboka czerń */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Nagłówek Hero */
    .hero-title {
        font-size: clamp(2.5rem, 7vw, 4rem);
        font-weight: 200;
        text-align: center;
        margin-top: 5vh;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    .highlight {
        color: #c88141; /* Miedziany akcent Vorteza */
        font-weight: 400;
    }

    /* Kontener Excela (Chaos) */
    .excel-chaos-frame {
        border: 1px solid #222;
        padding: 20px;
        background: #0d0d0d;
        opacity: 0.5;
        filter: grayscale(100%) blur(1px);
        transition: 0.6s ease;
        text-align: center;
        border-radius: 15px;
    }
    .excel-chaos-frame:hover {
        opacity: 0.9;
        filter: grayscale(0%) blur(0px);
    }

    /* Przycisk Transformacji */
    .stButton>button {
        width: 100%;
        background-color: #c88141 !important;
        color: white !important;
        border: none !important;
        padding: 1.6rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 10px !important;
        box-shadow: 0 10px 30px rgba(200, 129, 65, 0.2);
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(200, 129, 65, 0.4);
        background-color: #e0965a !important;
    }

    /* Karty Portfolio po transformacji */
    .vorteza-card {
        background: #0d0d0d;
        padding: 2.5rem;
        border-radius: 20px;
        border: 1px solid #1a1a1a;
        border-left: 5px solid #c88141;
        transition: 0.3s;
    }
    
    /* Stylizacja Zakładek (Tabs) */
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 30px; }
    .stTabs [data-baseweb="tab"] { color: #555; font-size: 1.1rem; }
    .stTabs [aria-selected="true"] { color: #c88141 !important; font-weight: bold; }

</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA STANU (SESSION STATE) ---
if 'detox_done' not in st.session_state:
    st.session_state.detox_done = False

# --- SCENA 1: CHAOS (PRZED TRANSFORMACJĄ) ---
if not st.session_state.detox_done:
    st.markdown("<div class='hero-title'>Twoja firma <span class='highlight'>tonie w Excelach?</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #666; margin-bottom: 40px;'>Chaos danych i godziny zmarnowane na ręczną pracę. Czas to zmienić.</p>", unsafe_allow_html=True)
    
    _, col_mid, _ = st.columns([1, 2, 1])
    
    with col_mid:
        st.markdown("<div class='excel-chaos-frame'>", unsafe_allow_html=True)
        try:
            st.image("excel_chaos.png", use_container_width=True)
        except:
            st.info("Pamiętaj o dodaniu pliku excel_chaos.png do GitHub!")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("")
        if st.button("ZASTĄP TEN CHAOS SYSTEMEM VORTEZA"):
            with st.spinner('TRWA TRANSFORMACJA TWOJEGO BIZNESU...'):
                time.sleep(2)
                st.session_state.detox_done = True
                st.rerun()

# --- SCENA 2: VORTEZA OS (PO TRANSFORMACJI) ---
else:
    st.markdown("<div class='hero-title'>Vorteza Systems. <br><span class='highlight'>Biznes uwolniony.</span></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; max-width: 850px; margin: 30px auto 50px auto; font-size: 1.25rem; line-height: 1.6; color: #888;'>
        Jesteśmy butikową pracownią oprogramowania. Tworzymy systemy potężne jak w korporacjach, 
        ale piękne, intuicyjne i w ludzkiej cenie. <br>
        <b>Rozmawiasz bezpośrednio z twórcami. Płacisz za efekt, nie za nasze biuro.</b>
    </div>
    """, unsafe_allow_html=True)

    # INTERAKTYWNE PORTFOLIO
    t1, t2, t3 = st.tabs(["LOGISTYKA (CORE)", "KANCELARIA (LEX)", "MEDYCYNA (MED)"])

    with t1:
        c1, c2 = st.columns([1.8, 1])
        with c1:
            try: st.image("image_526749.jpg", use_container_width=True)
            except: st.error("Brak pliku image_526749.jpg")
        with c2:
            st.markdown("""<div class='vorteza-card'><h2 class='highlight'>Vorteza Core</h2><p>Złożony routing i zarządzanie flotą na żywo. <br><br><b>Efekt:</b> 5 godzin planowania tras skrócone do 5 minut automatyzacji.</p></div>""", unsafe_allow_html=True)

    with t2:
        c1, c2 = st.columns([1.8, 1])
        with c1:
            try: st.image("image_52609f.jpg", use_container_width=True)
            except: st.error("Brak pliku image_52609f.jpg")
        with c2:
            st.markdown("""<div class='vorteza-card'><h2 class='highlight'>Vorteza Lex</h2><p>Precyzyjne zarządzanie sprawami i billing czasu pracy.<br><br><b>Efekt:</b> Pełna przejrzystość zysków i koniec papierologii w kancelarii.</p></div>""", unsafe_allow_html=True)

    with t3:
        c1, c2 = st.columns([1.8, 1])
        with c1:
            try: st.image("image_5263a8.jpg", use_container_width=True)
            except: st.error("Brak pliku image_5263a8.jpg")
        with c2:
            st.markdown("""<div class='vorteza-card'><h2 class='highlight'>Vorteza Med</h2><p>Radar obłożenia i błyskawiczne zarządzanie pacjentami.<br><br><b>Efekt:</b> Recepcja, która nigdy się nie myli. Zero okienek, pełna kontrola.</p></div>""", unsafe_allow_html=True)

    # KONTAKT / STOPKA
    st.markdown("<br><br><br><hr style='border: 0.1px solid #222;'>", unsafe_allow_html=True)
    f1, f2, f3 = st.columns([1, 2, 1])
    with f2:
        st.markdown("<p style='text-align: center; color: #555;'>Twój system może być gotowy szybciej, niż agencja przygotuje ofertę.</p>", unsafe_allow_html=True)
        if st.button("DOWIEDZ SIĘ, CO MOŻEMY ZBUDOWAĆ DLA CIEBIE"):
            st.balloons()
            st.info("Tutaj wstawimy Twój numer telefonu lub link do formularza, który obsłuży żona!")

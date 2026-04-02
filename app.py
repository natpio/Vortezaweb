import streamlit as st
import time

# --- 1. KONFIGURACJA STRONY ---
st.set_page_config(
    page_title="Vorteza Systems | Digital Detox",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. STYLIZACJA CSS (KLUCZ DO EFEKTU WOW) ---
st.markdown("""
<style>
    /* Ukrycie elementów Streamlita */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Tło i główna typografia */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Styl nagłówków */
    .hero-title {
        font-size: 4rem;
        font-weight: 200;
        text-align: center;
        margin-top: 5vh;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    .highlight {
        color: #c88141; /* Miedziany kolor premium */
        font-weight: 400;
    }

    /* Wygląd "Starego Świata" (Excel) */
    .excel-container {
        border: 1px solid #333;
        padding: 20px;
        background: #1a1a1a;
        opacity: 0.5;
        filter: grayscale(100%);
        transition: 0.5s;
        text-align: center;
        border-radius: 10px;
    }
    .excel-container:hover {
        opacity: 1;
        filter: grayscale(0%);
    }

    /* Styl Przycisków */
    .stButton>button {
        width: 100%;
        background-color: #c88141;
        color: white;
        border: none;
        padding: 1.5rem;
        font-size: 1.3rem;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 8px;
        box-shadow: 0 10px 30px rgba(200, 129, 65, 0.2);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e0965a;
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(200, 129, 65, 0.4);
    }

    /* Stylowanie Kart Portfolio */
    .card {
        background: #111;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #222;
        border-left: 5px solid #c88141;
        margin-bottom: 20px;
    }
    
    /* Zakładki (Tabs) */
    .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 30px; }
    .stTabs [data-baseweb="tab"] { color: #666; font-size: 1.1rem; }
    .stTabs [aria-selected="true"] { color: #c88141 !important; }

</style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA PRZEŁĄCZANIA WIDOKU (SESSION STATE) ---
if 'is_detoxed' not in st.session_state:
    st.session_state.is_detoxed = False

# --- SCENA 1: CHAOS I EXCEL (PRZED TRANSFORMACJĄ) ---
if not st.session_state.is_detoxed:
    st.markdown("<div class='hero-title'>Twoja firma <span class='highlight'>tonie w Excelach?</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.3rem; color: #888; margin-bottom: 40px;'>Znamy ten ból. Chaos danych, błędy w formułach i marnowanie godzin na ręczną pracę.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Wizualizacja "Problemu"
        st.markdown("""
        <div class='excel-container'>
            <p style='color: #555; margin-bottom: 10px;'>[ SYMULACJA ARCHAICZNEGO SYSTEMU ]</p>
            <div style='height: 250px; background: repeating-linear-gradient(0deg, #222, #222 30px, #282828 30px, #282828 31px);'>
                <br><br><br><span style='color: #444;'>Nieczytelne tabele... błąd #REF!... utracone dane...</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # Odstęp
        
        if st.button("ZASTĄP TEN CHAOS SYSTEMEM KLASY PREMIUM"):
            with st.spinner('TRWA TRANSFORMACJA TWOJEGO BIZNESU...'):
                time.sleep(2) # Efekt budowania napięcia
                st.session_state.is_detoxed = True
                st.rerun()

# --- SCENA 2: VORTEZA OS (PO TRANSFORMACJI) ---
else:
    st.markdown("<div class='hero-title'>Vorteza Systems. <span class='highlight'>Biznes uwolniony.</span></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; max-width: 900px; margin: 0 auto 50px auto; font-size: 1.2rem; line-height: 1.6; color: #aaa;'>
        Nie jesteśmy agencją. Jesteśmy butikową pracownią oprogramowania. 
        Budujemy systemy, które wyglądają jak luksusowy dashboard, a działają jak szwajcarski zegarek. 
        <b>Bez korporacyjnego narzutu, bez zbędnych handlowców.</b>
    </div>
    """, unsafe_allow_html=True)

    # PORTFOLIO W FORMIE KLIKALNEJ
    tab1, tab2, tab3 = st.tabs(["LOGISTYKA (CORE)", "KANCELARIA (LEX)", "MEDYCYNA (MED)"])

    with tab1:
        c1, c2 = st.columns([2, 1])
        with c1:
            # Upewnij się, że pliki obrazów są w folderze!
            try:
                st.image("image_526749.jpg", use_container_width=True)
            except:
                st.warning("Dodaj plik image_526749.jpg do folderu")
        with c2:
            st.markdown("""
            <div class='card'>
                <h3 class='highlight'>Vorteza Core</h3>
                <p>Potężny system routingowy i zarządzanie flotą.</p>
                <hr style='border: 0.5px solid #333;'>
                <p style='font-size: 0.9rem;'>Zastąpił 4 arkusze Excela i 5 godzin codziennego planowania tras.</p>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        c1, c2 = st.columns([2, 1])
        with c1:
            try:
                st.image("image_52609f.jpg", use_container_width=True)
            except:
                st.warning("Dodaj plik image_52609f.jpg do folderu")
        with c2:
            st.markdown("""
            <div class='card'>
                <h3 class='highlight'>Vorteza Lex</h3>
                <p>Elegancja i precyzja w prowadzeniu kancelarii.</p>
                <hr style='border: 0.5px solid #333;'>
                <p style='font-size: 0.9rem;'>Automatyczny billing czasu pracy i rejestr spraw cywilnych.</p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        c1, c2 = st.columns([2, 1])
        with c1:
            try:
                st.image("image_5263a8.jpg", use_container_width=True)
            except:
                st.warning("Dodaj plik image_5263a8.jpg do folderu")
        with c2:
            st.markdown("""
            <div class='card'>
                <h3 class='highlight'>Vorteza Med</h3>
                <p>Radar obłożenia i zarządzanie pacjentami.</p>
                <hr style='border: 0.5px solid #333;'>
                <p style='font-size: 0.9rem;'>Szybka rejestracja, zero okienek, pełna kontrola nad wizytami.</p>
            </div>
            """, unsafe_allow_html=True)

    # STOPKA ZE SZCZEROŚCIĄ
    st.write("---")
    foot1, foot2, foot3 = st.columns([1, 2, 1])
    with foot2:
        st.markdown("<p style='text-align: center; color: #666;'>Jesteśmy dwuosobowym zespołem. Płacisz za kod i design, nie za nasze biuro.</p>", unsafe_allow_html=True)
        if st.button("DOWIEDZ SIĘ, CO MOŻEMY ZBUDOWAĆ DLA CIEBIE"):
            st.success("☎️ Kontakt: Twoja żona już czeka na wiadomość! (Dodaj tutaj link do formularza)")
            st.balloons()

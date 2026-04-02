import streamlit as st

# 1. KONFIGURACJA STRONY (Musi być na samej górze)
st.set_page_config(
    page_title="Vorteza Systems | Butikowe Oprogramowanie",
    page_icon="⚙️",
    layout="centered", # 'centered' wymusza węższy, bardziej czytelny układ przypominający stronę landing page
    initial_sidebar_state="collapsed"
)

# 2. HACKING CSS (Nadpisanie wyglądu Streamlita, dodanie mrocznego klimatu premium)
st.markdown("""
<style>
    /* Ukrycie domyślnego menu i stopki Streamlita, żeby ukryć "kuchnię" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Globalne tło i czcionka */
    .stApp {
        background-color: #0b0c10; /* Głęboki, elegancki grafit */
        color: #c5c6c7;
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
    }
    
    /* Stylowanie nagłówków */
    .hero-title {
        font-size: 3.2rem;
        line-height: 1.2;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        color: #ffffff;
        font-weight: 300;
        text-align: center;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        line-height: 1.6;
        text-align: center;
        color: #8a8d91;
        max-width: 650px;
        margin: 0 auto 4rem auto;
        font-weight: 300;
    }
    
    /* Miedziane akcenty */
    .accent {
        color: #c88141; /* Miedziany/Złoty inspirowany Vorteza Core */
        font-weight: 500;
    }
    
    /* Wygląd zakładek (Tabs) by przypominały ekskluzywne menu */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        justify-content: center;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #666;
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 1px;
        border-radius: 0;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        color: #c88141 !important;
        border-bottom: 2px solid #c88141 !important;
    }
    
    /* Ramki dla portfolio */
    .portfolio-card {
        background-color: #12151b;
        border: 1px solid #1f242d;
        border-radius: 12px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .portfolio-desc {
        color: #a0a2a5;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Przycisk CTA */
    .stButton>button {
        background-color: transparent;
        color: #c88141;
        border: 1px solid #c88141;
        border-radius: 6px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #c88141;
        color: #0b0c10;
        border: 1px solid #c88141;
    }
    
    .cta-text {
        text-align: center;
        margin-top: 5rem;
        margin-bottom: 1.5rem;
        font-size: 1.3rem;
        color: #ffffff;
        font-weight: 300;
    }
</style>
""", unsafe_allow_html=True)

# 3. SEKCJA HERO (Powitanie wgniatające szczerością)
st.markdown("""
<div class='hero-title'>
    Butikowe oprogramowanie.<br>
    <span class='accent'>Bez korporacyjnego rachunku.</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-subtitle'>
    Nie mamy szklanego biurowca ani armii handlowców. Jesteśmy we dwoje.<br>
    Budujemy dedykowane, potężne systemy, które po prostu działają i wyglądają dokładnie tak, jak powinny. 
    Płacisz za rozwiązanie problemu i świetny design, a nie za utrzymanie naszej agencji.
</div>
""", unsafe_allow_html=True)


# 4. INTERAKTYWNE PORTFOLIO (Zakładki zamiast scrollowania)
st.markdown("<p style='text-align: center; color: #555; font-size: 0.9rem; letter-spacing: 2px;'>ZOBACZ CO BUDUJEMY NA CO DZIEŃ:</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["LOGISTYKA", "KANCELARIE", "MEDYCYNA"])

with tab1:
    st.markdown("""
    <div class='portfolio-card'>
        <h3 class='accent' style='margin-bottom: 10px; font-weight: 400;'>Vorteza Core</h3>
        <p class='portfolio-desc'>Centrum dowodzenia transportem. Złożony routing i zarządzanie flotą zamknięte w interfejsie, którego nie chce się wyłączać. <i>Twój system może wyglądać podobnie.</i></p>
    </div>
    """, unsafe_allow_html=True)
    # TUTAJ PODMIENISZ NA SWÓJ OBRAZEK:
    # Upewnij się, że plik image_526749.jpg jest w tym samym folderze co skrypt app.py
    # st.image("image_526749.jpg", use_column_width=True)
    st.info("📌 W tym miejscu pojawi się zrzut z Vorteza Core. Odkomentuj linię 'st.image' w kodzie.", icon="⚙️")

with tab2:
    st.markdown("""
    <div class='portfolio-card'>
        <h3 class='accent' style='margin-bottom: 10px; font-weight: 400;'>Vorteza Lex</h3>
        <p class='portfolio-desc'>Śledzenie czasu pracy i pełen obieg spraw cywilnych. Przejrzystość, która uwalnia prawników od papierologii i zwraca się w kilka tygodni.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.image("image_52609f.jpg", use_column_width=True)
    st.info("📌 W tym miejscu pojawi się zrzut z Vorteza Lex. Odkomentuj linię 'st.image' w kodzie.", icon="⚖️")

with tab3:
    st.markdown("""
    <div class='portfolio-card'>
        <h3 class='accent' style='margin-bottom: 10px; font-weight: 400;'>Vorteza Med</h3>
        <p class='portfolio-desc'>Radar obłożenia i błyskawiczna rejestracja. Koniec z pomyłkami, okienkami i chaosem na recepcji medycznej.</p>
    </div>
    """, unsafe_allow_html=True)
    # st.image("image_5263a8.jpg", use_column_width=True)
    st.info("📌 W tym miejscu pojawi się zrzut z Vorteza Med. Odkomentuj linię 'st.image' w kodzie.", icon="⚕️")


# 5. WEZWANIE DO AKCJI (Ciche, eleganckie CTA)
st.markdown("<div class='cta-text'>Podoba Ci się to, co widzisz?</div>", unsafe_allow_html=True)

# Używamy kolumn, aby przycisk był estetycznie wyśrodkowany i nie na całą szerokość ekranu
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Porozmawiajmy o systemie dla Ciebie", use_container_width=True):
        st.success("Tutaj możemy np. wyświetlić formularz kontaktowy, numer telefonu lub link do Calendly!")

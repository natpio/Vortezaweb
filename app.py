import streamlit as st

# 1. Konfiguracja strony
st.set_page_config(
    page_title="VORTEZA SYSTEMS | Dashboard",
    page_icon="🚀",
    layout="wide"
)

# 2. "Odważny" Design - Wstrzykiwanie CSS
st.markdown("""
    <style>
    /* Główny tło i fonty */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Customowe karty */
    .sector-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    .sector-card:hover {
        transform: translateY(-5px);
        border-color: #38bdf8;
    }
    
    /* Stylizacja nagłówków */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        letter-spacing: -1px;
    }
    
    /* Przycisk CTA */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 25px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Nawigacja branżowa
with st.sidebar:
    st.image("https://via.placeholder.com/150x50?text=VORTEZA", use_container_width=True) # Tu wrzuć logo
    st.title("Panel Sterowania")
    choice = st.radio(
        "Wybierz swój świat:",
        ["Główna", "Transport & Logistyka", "Kancelaria Prawna", "Medycyna Pracy"]
    )
    st.markdown("---")
    st.info("Target: Małe firmy. Cel: Wielki wzrost.")

# 4. Logika widoków
if choice == "Główna":
    st.title("🚀 VORTEZA SYSTEMS")
    st.subheader("Nawigujemy przez biznesowy chaos.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="sector-card"><h3>🚛 Transport</h3><p>Zarządzaj flotą bez stresu. Monitoring i karty pracy w jednym miejscu.</p></div>', unsafe_allow_html=True)
        if st.button("Sprawdź Transport"):
             st.toast("Przełączam na moduł Transportu...")
             
    with col2:
        st.markdown('<div class="sector-card"><h3>⚖️ Kancelaria</h3><p>Terminy, akta i rozliczenia pod pełną kontrolą Twojego zespołu.</p></div>', unsafe_allow_html=True)
        if st.button("Sprawdź Prawo"):
            st.toast("Otwieram akta...")

    with col3:
        st.markdown('<div class="sector-card"><h3>🩺 Medycyna</h3><p>Automatyzacja badań profilaktycznych i rejestracji pacjentów.</p></div>', unsafe_allow_html=True)
        if st.button("Sprawdź Medycynę"):
            st.toast("Przygotowuję gabinet...")

elif choice == "Transport & Logistyka":
    st.title("🚛 Moduł Transportowy")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("Mapa aktywnych tras (symulacja):")
        st.map() # Streamlit ma wbudowaną obsługę map!
    with c2:
        st.metric("Aktywne pojazdy", "12", "+2 dzisiaj")
        st.metric("Dostarczone ładunki", "148", "98%")

elif choice == "Kancelaria Prawna":
    st.title("⚖️ System Zarządzania Sprawami")
    tab1, tab2 = st.tabs(["Kalendarz Rozpraw", "Baza Klientów"])
    with tab1:
        st.write("Twoje najbliższe terminy:")
        st.table({"Data": ["2026-04-10", "2026-04-12"], "Sprawa": ["Sygn. akt IV C 12/24", "Sygn. akt I AD 5/25"]})
    with tab2:
        st.text_input("Szukaj klienta po PESEL/NIP")

elif choice == "Medycyna Pracy":
    st.title("🩺 Gabinet Medycyny Pracy")
    st.progress(65, text="Obłożenie gabinetów na dziś")
    col_a, col_b = st.columns(2)
    col_a.date_input("Wybierz dzień do planowania badań")
    col_b.multiselect("Typy badań", ["Wstępne", "Okresowe", "Kierowcy", "Sanitarne"])

# 5. Stopka
st.markdown("---")
st.caption("© 2026 VORTEZA SYSTEMS | Built for scale, designed for simplicity.")

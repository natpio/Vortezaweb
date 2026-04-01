import streamlit as st

st.set_page_config(page_title="VORTEZA SYSTEMS | Nowoczesny Biznes", layout="centered")

# Stylizacja na "Modern Glassmorphism"
st.markdown("""
    <style>
    .hero-text {
        font-size: 50px;
        font-weight: 800;
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }
    .cta-button {
        text-align: center;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="hero-text">VORTEZA: Twoja firma, tylko mądrzejsza.</p>', unsafe_allow_html=True)

# Wybór branży jako główny nawigator na wizytówce
industry = st.selectbox("Wybierz swoją branżę, by zobaczyć jak zmienimy Twój biznes:", 
                        ["Transport", "Prawo", "Medycyna Pracy"])

if industry == "Transport":
    st.header("🚛 Logistyka pod pełną kontrolą")
    st.write("Dla małych firm transportowych liczy się każdy kilometr. Nasz system eliminuje puste przebiegi i automatyzuje rozliczenia kierowców.")
    # Mała interakcja marketingowa
    fleet_size = st.slider("Ile masz pojazdów?", 1, 50, 5)
    st.info(f"Przy {fleet_size} pojazdach, VORTEZA odzyskuje średnio {fleet_size * 2} godzin pracy biurowej tygodniowo.")

elif industry == "Prawo":
    st.header("⚖️ Kancelaria bez papieru")
    st.write("Skup się na prawie, my zajmiemy się terminami. Inteligentne repozytorium akt i automatyczny kalendarz rozpraw.")

# Sekcja Kontaktowa (Cel strony)
st.divider()
st.subheader("Chcesz zobaczyć pełną aplikację w akcji?")
col1, col2 = st.columns(2)
with col1:
    st.text_input("Twoje Imię")
    st.text_input("E-mail służbowy")
with col2:
    st.text_area("W czym możemy Ci pomóc?")
    if st.button("Umów bezpłatne Demo"):
        st.success("Dziękujemy! Nasz doradca odezwie się w ciągu 24h.")

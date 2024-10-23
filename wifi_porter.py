import streamlit as st
from PIL import Image

# Prilagodite osnovne postavke stranice
st.set_page_config(page_title="WiFi Porter - Brzo povezivanje na WiFi", page_icon="📶", layout="wide", initial_sidebar_state="collapsed")

# Dodavanje meta opisa (za SEO)
st.markdown("""
    <meta name="description" content="WiFi Porter - uređaj za lako povezivanje na WiFi za apartmane, hotele i stan na dan. NFC, QR kod ili klasična lozinka.">
    <meta name="keywords" content="WiFi Porter, NFC WiFi, QR kod, WiFi uređaj, prijavljivanje na WiFi">
    <meta name="author" content="WiFi Porter Team">
""", unsafe_allow_html=True)

# Učitaj slike
wifi_image = Image.open("wifi_porter.jpg")  # Slika WiFi Portera
nfc_image = Image.open("nfc_example.jpg")   # Slika NFC funkcionalnosti
qr_image = Image.open("qr_example.jpg")     # Slika QR koda

# Naslovna sekcija - SEO Heading Struktura (H1 za glavni naslov)
st.title("WiFi Porter - Brzo i jednostavno WiFi povezivanje za vaše goste")
st.markdown("""
### Povežite goste na WiFi bez muke, koristeći NFC, QR kod ili klasičnu lozinku.
**Za apartmane, hotele i izdavače stanova.**
""")

# Slika proizvoda i opis (Alt tekst za slike - SEO)
st.image(wifi_image, use_column_width=True, caption="WiFi Porter uređaj za brzo povezivanje na WiFi")
st.write("""
WiFi Porter je uređaj koji omogućava gostima da se brzo i lako povežu na vaš WiFi. 
Bilo da koriste **NFC tehnologiju**, **QR kod** ili klasični unos šifre, vaši gosti će imati besprekorno iskustvo povezivanja.
""")

# Sekcija sa slikama NFC i QR funkcionalnosti
st.subheader("Kako funkcioniše?")
col1, col2 = st.columns(2)

with col1:
    st.image(nfc_image, caption="NFC funkcionalnost - prislonite telefon da se povežete", use_column_width=True)
with col2:
    st.image(qr_image, caption="QR kod - skenirajte i povežite se", use_column_width=True)

st.write("""
### Jednostavni koraci za povezivanje:
1. Postavite WiFi Porter u apartman, sobu ili recepciju.
2. Gosti prislone telefon na NFC tag ili skeniraju QR kod.
3. Automatsko povezivanje na WiFi bez unosa lozinke.
""")

# Sekcija prednosti sa jasnom struktura za SEO
st.subheader("Prednosti za vlasnike apartmana, hostela i hotela")
st.write("""
- **Jednostavno postavljanje**: Instalirajte uređaj za nekoliko minuta.
- **Poboljšano korisničko iskustvo**: Gosti se povezuju brzo i bez komplikacija.
- **Smanjenje zahteva korisničke podrške**: Više nema pitanja o lozinkama.
- **Moderan dizajn**: WiFi Porter se lako uklapa u svaki prostor.
""")

# CTA (Call to Action) - Cena i paketi
st.subheader("Cenovnik")
st.write("""
Ponuda na osnovu količine:

- 1 uređaj: **40 EUR**
- 5 uređaja: **35 EUR** po komadu
- 10+ uređaja: **30 EUR** po komadu

Kontaktirajte nas za veće narudžbe i personalizaciju uređaja.
""")

# Kontakt forma sa CTA dugmetom
st.subheader("Zainteresovani? Kontaktirajte nas")
st.write("Popunite formu ispod ili nas kontaktirajte putem emaila **wifi.porter@example.com**")

with st.form("contact_form"):
    name = st.text_input("Vaše ime")
    email = st.text_input("Vaš email")
    message = st.text_area("Poruka")

    submitted = st.form_submit_button("Pošaljite poruku")
    if submitted:
        st.write(f"Hvala {name}, vaša poruka je poslata!")

# Footer sa ključnim informacijama za SEO
st.markdown("""
---
**WiFi Porter** | Brzo i jednostavno WiFi povezivanje za apartmane, hotele i stan na dan. | Kontakt: wifi.porter@example.com
""")
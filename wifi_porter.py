import streamlit as st
from PIL import Image

# Osnovna konfiguracija stranice
st.set_page_config(page_title="WiFi Porter", page_icon="📶", layout="wide", initial_sidebar_state="collapsed")
# Dodavanje meta opisa (za SEO)
st.markdown("""
    <meta name="description" content="WiFi Porter - uređaj za lako povezivanje na WiFi za apartmane, hotele i stan na dan. NFC, QR kod ili klasična lozinka.">
    <meta name="keywords" content="WiFi Porter, NFC WiFi, QR kod, WiFi uređaj, prijavljivanje na WiFi">
    <meta name="author" content="WiFi Porter Team">
""", unsafe_allow_html=True)

# Naslovna slika i CTA
columns_images = st.columns(3)
with columns_images[0]:
  st.image("resources/wifi_porter_0 - Copy2.png",width=400)
st.title(":blue[WiFi Porter] – Povežite vaše goste na WiFi u sekundi")
st.markdown("""
### Povežite goste na WiFi bez muke, koristeći :blue[NFC], :blue[QR kod] ili klasičnu :blue[lozinku].
""")
st.info("**Za izdavače: Stanova, Apartmana, Hostela i Hotela.**", icon=":material/tips_and_updates:")
st.write("""
WiFi Porter je uređaj koji omogućava gostima da se brzo i lako povežu na vaš WiFi. 
Bilo da koriste **NFC tehnologiju**, **QR kod** ili klasični unos šifre, vaši gosti će imati besprekorno iskustvo povezivanja.
         
""")
# Slika proizvoda i opis (Alt tekst za slike - SEO)
columns_images = st.columns(3)
with columns_images[1]:
   st.image("resources/wifi_porter_4_copy.png", use_column_width=False, width=450,caption="WiFi Porter uređaj za brzo povezivanje na WiFi")

# Prednosti sekcija
st.header("Zašto odabrati WiFi Porter?")
st.markdown("""
- Jednostavno postavljanje: Podesite uređaj za nekoliko minuta.
- Kompatibilnost: Radi sa svim pametnim telefonima i uređajima.
- Bez lozinke: NFC i QR tehnologija eliminišu unos lozinki.
- Poboljšano korisničko iskustvo: Gosti se povezuju brzo i bez komplikacija.
- Moderan dizajn: Uređaj se lako uklapa u bilo koji prostor.
""")
st.markdown(f"\n")

with st.container(border=True):
  # Kako funkcioniše sekcija
  st.header("Kako funkcioniše?")
  st.subheader("Jednostavni koraci za povezivanje:")
  col1, col2, col3 = st.columns(3)
  with col1:
      st.image("resources/wifi_porter_1.jpg", caption="NFC - Prislonite telefon", use_column_width=True)
      st.write("NFC funkcionalnost: Brzo povezivanje samo prislonite telefon.")
  with col2:
      st.image("resources/wifi_porter_2.jpg", caption="QR kod - Skenirajte i povežite se", use_column_width=True)
      st.write("QR kod: Skenirajte i automatski pristupite WiFi mreži.")
  with col3:
      st.image("resources/wifi_porter_3.jpg", caption="Unesite šifru", use_column_width=True)
      st.write("Lozinka: Klasično povezivanje pomoću lozinke.")

st.write("""
### Jednostavni koraci za podešavanje:
1. Postavite WiFi Porter u apartman, sobu ili na recepciji.
2. Otvorite aplikaciju na telefonu, upisite sifru i ime WiFi-a, i prislonite telefon na WiFi porter.
3. Skinite pdf fajl sa markiranim QR codom i sifrom, koju postavljate na zadnji deo uredjaja.
""")

st.divider()
# Cenovnik sekcija
st.header("Cenovnik")
st.write("""
Odaberite paket koji vam odgovara:
- 1 uređaj: 1640 din
- 5 uređaja: 1470 din po  komadu
- 10+ uređaja: 1390 din po komadu
""")
st.markdown(" [Kontaktirajte nas za veće narudžbe i personalizaciju uređaja.](#kontaktirajte-nas)")
st.divider()

# Testimonijali sekcija
st.header("Šta kažu naši klijenti?")
st.write("Pogledajte iskustva vlasnika apartmana i hotela.")
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
      st.info("Marko, vlasnik apartmana: Gostima je sada mnogo lakše da se povežu na WiFi.")
with col2:
    with st.container(border=True):
      st.info("Milica, menadžer hotela: Smanjili smo zahteve za podršku zahvaljujući WiFi Porteru.")
with col3:
    with st.container(border=True):
      st.info("Ivana, vlasnica hostela: Savršen uređaj za brzo povezivanje gostiju.")
st.divider()

# FAQ sekcija
st.header("Često postavljana pitanja")
faq1 = st.expander("Kako instalirati WiFi Porter?")
faq1.write("Jednostavno postavite uređaj na vidljivo mesto i povežite ga sa WiFi mrežom:")
faq1.write("""
Koraci:
1. Otvorite aplikaciju na telefonu.
2. Upisite ime i sifru WiFi-a, i prislonite telefon na WiFi porter.
3. Skinite pdf fajl sa markiranim QR codom i sifrom, koju postavljate na zadnji deo uredjaja.
""")
faq2 = st.expander("Da li radi sa svim uređajima?")
faq2.write("WiFi Porter je kompatibilan sa svim modernim pametnim telefonima i tabletima.")
faq2.write("""
           - **NFC** tehnologiju poseduje većina novijih pametnih telefona.
           - **QR code** mogu da skeniraju svi telefoni koji poseduju kameru.
           - Uz pomoć **imena i šifre WiFi-a** mogu se povezati svi uređaji.
""")

faq3 = st.expander("Mogu li personalizovati WiFi Porter?")
faq3.write("Da, možemo prilagoditi izgled uređaja sa vašim logotipom.")
st.divider()

# Kontakt forma
st.header("Kontaktirajte nas")
st.write("Popunite formu ispod za više informacija o WiFi Porteru.")
with st.form(key="contact_form"):
    name = st.text_input("Vaše ime")
    email = st.text_input("Vaš email")
    message = st.text_area("Vaša poruka")
    submit_button = st.form_submit_button(label="Pošaljite")
    if submit_button:
        st.success(f"Hvala {name}, vaša poruka je poslata!")

# Footer
st.markdown("""
---
Kontakt informacije:
- Email: wifi.porter@example.com
- Telefon: +381 64 123 4567
""")


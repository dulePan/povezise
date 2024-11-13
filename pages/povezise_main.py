import streamlit as st
from PIL import Image

# Naslovna slika i CTA
columns_main = st.columns(2) 
with columns_main[0]:
  st.title(":blue[PovežiSe uređaj] – Jednostavno povežite goste na WiFi u sekundi")
  st.markdown("""<h3 style="color:#a6a6a6;"> Omogućite gostima brz pristup WiFi mreži uz  <span style="color:#60b4ff">PovežiSe</span> – koristeći  <span style="color:#60b4ff">NFC</span>, <span style="color:#60b4ff">QR kod</span> ili klasičnu <span style="color:#60b4ff">lozinku</span>.</h3>
  """,unsafe_allow_html=True)
  st.info("**Za izdavače: Stanova, Apartmana, Hostela i Hotela.**", icon=":material/tips_and_updates:")
  st.markdown("""<h6 style="color:#a6a6a6;"><span style="color:#60b4ff">PovežiSe</span> uređaj omogućava gostima da se brzo i lako povežu na vaš WiFi. 
  Bilo da koriste  <span style="font-weight: bold;">NFC tehnologiju</span>,  <span style="font-weight: bold;">QR kod</span> ili klasični unos  <span style="font-weight: bold;">šifre</span>, vaši gosti će imati besprekorno iskustvo povezivanja.</h6>
          
  """,unsafe_allow_html=True)
  columns_actions = st.columns(2)
  with columns_actions[0]:
    if st.button(":material/shopping_bag: Poruči 'PovežiSe'",type="primary", use_container_width=True ):
      st.switch_page("pages/qr_code_generator.py")
  with columns_actions[1]:
    if st.button(":material/play_arrow: Kako se koristi?", use_container_width=True):
      st.switch_page("pages/qr_code_generator.py")
with columns_main[1]:
  st.image("resources/wifi_porter_0 - Copy2.png",use_container_width=True,)

# Slika proizvoda i opis (Alt tekst za slike - SEO)
# with columns_images[1]:
  #  st.image("resources/wifi_porter_4_copy.png", use_container_width=True, width=450,caption="PovežiSe je uređaj za brzo povezivanje na WiFi")


# Prednosti sekcija
st.markdown("""<h1 align="center" style="margin-bottom: 25px;"> Zašto da odabereš  <span style="color:#60b4ff">PovežiSe</span>?</h1>""",unsafe_allow_html=True)

columns_features = st.columns(5)
with columns_features[0]:
  with st.container(border=True,key="container_features_01"):
    st.header(":blue[:material/handyman:]")
    st.markdown("""
    <h3 align="start"> Jednostavno postavljanje</h3>
    """,unsafe_allow_html=True)
    st.markdown("""
    <p align="start"> Postavite PovežiSe uređaj u samo nekoliko minuta, bez komplikacija. Savršeno za one koji žele instant rešenje bez muke!</p>
    """,unsafe_allow_html=True)
with columns_features[1]:
  with st.container(border=True,key="container_features_02"):
    st.header(":blue[:material/devices:]")
    st.markdown("""
    <h3 align="start"> Univerzalna kompatibilnost</h3>
    """,unsafe_allow_html=True)
    st.markdown("""
    <p align="start"> Radi besprekorno sa svim pametnim telefonima i uređajima, eliminišući sve tehničke barijere. Povezivanje je brzo, jednostavno i sigurno.</p>
    """,unsafe_allow_html=True)
with columns_features[2]:
  with st.container(border=True,key="container_features_03"):
    st.header(":blue[:material/lock_open:]")
    st.markdown("""
    <h3 align="start"> Povezivanje bez lozinki</h3>
    """,unsafe_allow_html=True)
    st.markdown("""
    <p align="start"> NFC i QR tehnologije omogućavaju gostima povezivanje jednim dodirom, eliminišući potrebu za pamćenjem lozinki.</p>
    """,unsafe_allow_html=True)
with columns_features[3]:
  with st.container(border=True,key="container_features_04"):
    st.header(":blue[:material/thumb_up:]")
    st.markdown("""
    <h3 align="start"> Poboljšano korisničko iskustvo</h3>
    """,unsafe_allow_html=True)
    st.markdown("""
    <p align="start"> Gosti se lako i brzo povezuju, bez frustracija i komplikacija – za njih je sve spremno u sekundi!</p>
    """,unsafe_allow_html=True)
with columns_features[4]:
  with st.container(border=True,key="container_features_05"):
    st.header(":blue[:material/design_services:]")
    st.markdown("""
    <h3 align="start"> Elegantan dizajn</h3>
    """,unsafe_allow_html=True)
    st.markdown("""
    <p align="start"> Moderno i diskretno dizajniran, PovežiSe se lako uklapa u bilo koji prostor i dodaje notu sofisticiranosti vašem ambijentu.</p>
    """,unsafe_allow_html=True)

# Prednosti sekcija
st.markdown("""<h1 align="center" style="margin-top: 55px;"> Brzi vodič: Kako  <span style="color:#60b4ff;">PovežiSe</span> uređaj funkcioniše?</h1>""",unsafe_allow_html=True)
st.markdown("""<h4 align="center" style="margin-bottom: 25px;"> <span style="color:#60b4ff;">PovežiSe</span> omogućava brzo i jednostavno povezivanje sa WiFi mrežom uz minimalan napor. 
            Sledite ove jednostavne korake za brz pristup:</h4>""",unsafe_allow_html=True)

columns_how_works_1 = st.columns(2, vertical_alignment="center")
with columns_how_works_1[0]:
  st.image("resources/wifi_porter_1.jpg", caption="NFC - Prislonite telefon", use_container_width=False, width=500)
with columns_how_works_1[1]: 
  st.markdown("""<h1 align="start" style="white-space: nowrap;"> Povežite se putem NFC-a</h1>""",unsafe_allow_html=True)
  st.markdown("""<h4 align="start" style="color:#a6a6a6"> <span style="font-weight: bold;">Instant povezanost: </span> Uživajte u trenutnom povezivanju jednostavnim prislanjanjem telefona na uređaj. 
              Bez unosa lozinki ili dodatnih koraka!!</h4>""",unsafe_allow_html=True)
  st.subheader("Kako funkcioniše:")
  st.subheader(" :blue[:material/send_to_mobile:] Približite telefon  :blue[PovežiSe] uređaju")
  st.subheader(" :blue[:material/automation:] Telefon automatski prepoznaje mrežu")
  st.subheader(" :blue[:material/web_traffic:] Povežite se na WiFi mrežu u sekundi klikom na dugme 'Connect'")

columns_how_works_2 = st.columns(2, vertical_alignment="center")
with columns_how_works_2[0]:  
  st.markdown("""<h1 align="start" style=""> Povezivanje preko QR koda</h1>""",unsafe_allow_html=True)
  st.markdown("""<h4 align="start" style="color:#a6a6a6"> <span style="font-weight: bold;">Brz pristup: </span> Skeniranjem QR koda, gosti lako pristupaju WiFi mreži bez komplikacija – idealno za brzu povezanost!
              """,unsafe_allow_html=True)
  st.subheader("Koraci za povezivanje:")
  st.subheader(" :blue[:material/smartphone_camera:] Otvorite aplikaciju za kameru na telefonu")
  st.subheader(" :blue[:material/qr_code_scanner:] Skenirajte QR kod prikazan na uređaju")
  st.subheader(" :blue[:material/automation:] Telefon automatski preuzima podatke i povezuje vas na mrežu")
with columns_how_works_2[1]:
  st.image("resources/wifi_porter_1.jpg", caption="QR kod - Skenirajte QR kod", use_container_width=False, width=500)

columns_how_works_3 = st.columns(2, vertical_alignment="center")
with columns_how_works_3[0]:  
  st.image("resources/wifi_porter_1.jpg", caption="Povezivanje šifrom", use_container_width=False, width=500)
with columns_how_works_3[1]:
  st.markdown("""<h1 align="start" style=""> Povezivanje uz lozinku</h1>""",unsafe_allow_html=True)
  st.markdown("""<h4 align="start" style="color:#a6a6a6"> <span style="font-weight: bold;">Tradicionalni način: </span> Za korisnike koji preferiraju unos lozinke, ova opcija omogućava sigurnu i poznatu metodu povezivanja.
              """,unsafe_allow_html=True)
  st.subheader("Koraci za povezivanje:")
  st.subheader(" :blue[:material/wifi_find:] Pronađite naziv WiFi mreže na uređaju")
  st.subheader(" :blue[:material/password:] Unesite lozinku koja je prikazana na uređaju")
  st.subheader(" :blue[:material/nest_remote_comfort_sensor:] Povežite se i uživajte u stabilnoj vezi")
st.divider()
  # st.header("NFC funkcionalnost: Brzo povezivanje samo prislonite telefon.")
# with st.container(border=True): 
#   # Kako funkcioniše sekcija
#   st.header("Kako funkcioniše?")
#   st.subheader("Jednostavni koraci za povezivanje:")
#   col1, col2, col3 = st.columns(3)
#   with col1:
#       st.image("resources/wifi_porter_1.jpg", caption="NFC - Prislonite telefon", use_column_width=True)
#       st.write("NFC funkcionalnost: Brzo povezivanje samo prislonite telefon.")
#   with col2:
#       st.image("resources/wifi_porter_2.jpg", caption="QR kod - Skenirajte i povežite se", use_column_width=True)
#       st.write("QR kod: Skenirajte i automatski pristupite WiFi mreži.")
#   with col3:
#       st.image("resources/wifi_porter_3.jpg", caption="Unesite šifru", use_column_width=True)
#       st.write("Lozinka: Klasično povezivanje pomoću lozinke.")

st.write("""
### Jednostavni koraci za podešavanje:
1. Postavite PovežiSe uređaj u apartman, sobu ili na recepciji.
2. Otvorite aplikaciju na telefonu, upisite sifru i ime WiFi-a, i prislonite telefon na PovežiSe uređaj.
3. Skinite pdf fajl sa markiranim QR codom i sifrom, i postavite na zadnji deo uredjaja.
""")

st.divider()
# Cenovnik sekcija
st.header("Cenovnik")
st.write("""
Odaberite paket koji vam odgovara:
- 1 uređaj: 2500 din
- 20 uređaja: 2250 din po komadu
- 30+ uređaja: 2100 din po komadu
""")
st.markdown(" [Kontaktirajte nas za veće narudžbe i personalizaciju uređaja.](#kontaktirajte-nas)")
st.divider()

# Testimonijali sekcija
# st.header("Šta kažu naši klijenti?")
# st.write("Pogledajte iskustva vlasnika apartmana i hotela.")
# col1, col2, col3 = st.columns(3)
# with col1:
#     with st.container(border=True):
#       st.info("Marko, vlasnik apartmana: Gostima je sada mnogo lakše da se povežu na WiFi.")
# with col2:
#     with st.container(border=True):
#       st.info("Milica, menadžer hotela: Smanjili smo zahteve za podršku zahvaljujući WiFi Porteru.")
# with col3:
#     with st.container(border=True):
#       st.info("Ivana, vlasnica hostela: Savršen uređaj za brzo povezivanje gostiju.")
# st.divider()

# FAQ sekcija
st.header("Često postavljana pitanja")
faq1 = st.expander("Kako instalirati PovežiSe?")
faq1.write("Jednostavno postavite uređaj na vidljivo mesto i povežite ga sa WiFi mrežom:")
faq1.write("""
Koraci:
1. Otvorite aplikaciju na telefonu.
2. Upisite ime i sifru WiFi-a, i prislonite telefon na PovežiSe.
3. Skinite pdf fajl sa markiranim QR codom i sifrom, koju postavljate na zadnji deo uredjaja.
""")
faq2 = st.expander("Da li radi sa svim uređajima?")
faq2.write("PovežiSe je kompatibilan sa svim modernim pametnim telefonima i tabletima.")
faq2.write("""
           - **NFC** tehnologiju poseduje većina novijih pametnih telefona.
           - **QR code** mogu da skeniraju svi telefoni koji poseduju kameru.
           - Uz pomoć **imena i šifre WiFi-a** mogu se povezati svi uređaji.
""")

# faq3 = st.expander("Mogu li personalizovati WiFi Porter?")
# faq3.write("Da, možemo prilagoditi izgled uređaja sa vašim logotipom.")
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
- Email: info@povezise.rs
- Telefon: +381 64 123 4567
""")


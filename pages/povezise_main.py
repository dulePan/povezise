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
  video_file = open("resources/nfc_connect.mp4", "rb") 
  video_bytes = video_file.read()
  st.video(video_bytes,muted=True, loop = True,autoplay=True)
  # st.image("resources/wifi_porter_1.jpg", caption="NFC - Prislonite telefon", use_container_width=False, width=500)
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
  st.subheader(" :blue[:material/automation:] Telefon automatski preuzima podatke i povezuje vas na mrežu na klik")
with columns_how_works_2[1]:
  # st.image("resources/wifi_porter_1.jpg", caption="QR kod - Skenirajte QR kod", use_container_width=False, width=500)
  video_file = open("resources/qrcode_connect.mp4", "rb") 
  video_bytes = video_file.read()
  st.video(video_bytes,muted=True, loop = True,autoplay=True)

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
st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="vc_row wpb_row vc_row-fluid">
    <div class="wpb_column vc_column_container vc_col-sm-12">
        <div class="vc_column-inner">
            <div class="wpb_wrapper">
                <section id="how-it-works" class="how-it-works">
                    <div class="container">
                        <div class="section-header wow fadeInUp" style="visibility: visible; animation-name: fadeInUp; text-align: center;">
                            <h1>Jednostavni koraci za podešavanje</h1>
                            <p class="how-p">Postavite i konfigurišite <span style="color:#60b4ff">PovežiSe</span> uređaj u samo nekoliko koraka. Brzo i jednostavno, bez komplikacija.</p>
                        </div>
                        <div class="work-processes" style="display: flex; justify-content: space-between; gap: 20px;">
                            <!-- Korak 1 -->
                            <div class="work-process wow fadeIn" style="flex: 1; text-align: center;">
                                <div class="process-icon">
                                    <img decoding="async" alt="Postavljanje uređaja" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/05/desktop-106x106.png">
                                </div>
                                <h3>Postavite uređaj</h3>
                                <p>Postavite <span style="color:#60b4ff">PovežiSe</span> uređaj u apartman, sobu ili na recepciji, na lako dostupno mesto za goste.</p>
                            </div>
                            <!-- Korak 2 -->
                            <div class="work-process wow fadeIn" style="flex: 1; text-align: center;">
                                <div class="process-icon">
                                    <img decoding="async" alt="Povezivanje uređaja" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/05/toggles-106x106.png">
                                </div>
                                <h3>Konfigurišite uređaj</h3>
                                <p>Otvorite aplikaciju na telefonu, unesite WiFi naziv i lozinku, i prislonite telefon na uređaj za automatsko podešavanje.</p>
                            </div>
                            <!-- Korak 3 -->
                            <div class="work-process wow fadeIn" style="flex: 1; text-align: center;">
                                <div class="process-icon">
                                    <img decoding="async" alt="Pristup gostima" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/05/trophy-106x106.png">
                                </div>
                                <h3>Obezbedite pristup gostima</h3>
                                <p>Preuzmite PDF fajl sa generisanim QR kodom i WiFi podacima, i prikačite ga na poleđinu uređaja za jednostavan pristup gostima.</p>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </div>
</div>
""",unsafe_allow_html=True)

 
# st.divider()
# Cenovnik sekcija
# st.header("Cenovnik")
st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
# st.markdown("""
# <div style="margin-top: 30px;">
#   <div style="text-align: center;">
#     <h1>Naša Kolekcija</h1>
#     <p>Izaberite savršen <span style="color:#60b4ff">PovežiSe</span> uređaj za vašu potrebu! Nudimo fleksibilne pakete uređaja sa opcijama za različite potrebe – od manjih instalacija do većih objekata. Uređaji dolaze u dve elegantne boje: bela i crna, sa istom cenom za oba modela.</p>
#   </div>
# <div class="row collections" style="display: flex; justify-content: space-between; flex-wrap: wrap;">
#   <div class="col-sm-6 col-md-3 item wow fadeIn" data-wow-delay="SPORTS EDITION" style="visibility: visible; animation-name: fadeIn; flex: 1 1 22%; margin: 10px; text-align: center;">
#     <div class="row m0 featured-img">
#       <img decoding="async" class="product-gallery-image-single" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/06/collection-1-213x213.jpg" alt="PovežiSe NFC Edition" style="max-width: 100%; height: auto;">
#     </div>
#     <h4 class="title"><span style="color:#60b4ff">PovežiSe</span> NFC Edition</h4>
#     <h5 class="category">WiFi Connection Device</h5>
#     <h4 class="price">2500 din</h4>
#     <p><strong>Izbor boje:</strong> Bela i Crna</p>
#     <a href="#product-choose-4" class="btn">CHOOSE</a>
#   </div>

#   <div class="col-sm-6 col-md-3 item wow fadeIn" data-wow-delay="SPORTS EDITION" style="visibility: visible; animation-name: fadeIn; flex: 1 1 22%; margin: 10px; text-align: center;">
#     <div class="row m0 featured-img">
#       <img decoding="async" class="product-gallery-image-single" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/06/collection-2-213x213.jpg" alt="PovežiSe QR Edition" style="max-width: 100%; height: auto;">
#     </div>
#     <h4 class="title"><span style="color:#60b4ff">PovežiSe</span> QR Edition</h4>
#     <h5 class="category">WiFi Connection Device</h5>
#     <h4 class="price">2500 din</h4>
#     <p><strong>Izbor boje:</strong> Bela i Crna</p>
#     <a href="#product-choose-3" class="btn">CHOOSE</a>
#   </div>

#   <div class="col-sm-6 col-md-3 item wow fadeIn" data-wow-delay="1" style="visibility: visible; animation-name: fadeIn; flex: 1 1 22%; margin: 10px; text-align: center;">
#     <div class="row m0 featured-img">
#       <img decoding="async" class="product-gallery-image-single" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/06/collection-3-213x213.jpg" alt="PovežiSe Basic Edition" style="max-width: 100%; height: auto;">
#     </div>
#     <h4 class="title"><span style="color:#60b4ff">PovežiSe</span> Basic Edition</h4>
#     <h5 class="category">WiFi Connection Device</h5>
#     <h4 class="price">2500 din</h4>
#     <p><strong>Izbor boje:</strong> Bela i Crna</p>
#     <a href="#product-choose-2" class="btn">CHOOSE</a>
#   </div>

#   <div class="col-sm-6 col-md-3 item wow fadeIn" data-wow-delay="0.5" style="visibility: visible; animation-name: fadeIn; flex: 1 1 22%; margin: 10px; text-align: center;">
#     <div class="row m0 featured-img">
#       <img decoding="async" class="product-gallery-image-single" src="https://ninetheme.com/themes/proland/wp-content/uploads/2016/06/collection-2-213x213.jpg" alt="PovežiSe Premium Edition" style="max-width: 100%; height: auto;">
#     </div>
#     <h4 class="title"><span style="color:#60b4ff">PovežiSe</span> Premium Edition</h4>
#     <h5 class="category">WiFi Connection Device</h5>
#     <h4 class="price">2500 din</h4>
#     <p><strong>Izbor boje:</strong> Bela i Crna</p>
#     <a href="#product-choose-1" class="btn">CHOOSE</a>
#   </div>
# </div>

# </div>
# """, unsafe_allow_html=True)
st.markdown("""
<div style="margin-top: 30px;">
  <div style="text-align: center;">
    <h1>Naša Kolekcija</h1>
    <p>Izaberite savršen <span style="color:#60b4ff">PovežiSe</span> uređaj za vašu potrebu! Nudimo fleksibilne pakete uređaja sa opcijama za različite potrebe – od manjih instalacija do većih objekata. Uređaji dolaze u dve elegantne boje: bela i crna, sa istom cenom za oba modela.</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
columns_products = st.columns(2,gap ="medium")
with columns_products[0]:
  with st.container(border=True,key="container_products_02"):
    st.image("resources/wifi_porter_0 - Copy2.png",use_container_width=True)
    st.markdown(f"""<h2 align="center"> <span style="color:#60b4ff">PovežiSe</span><br>Black Edition</h2>""",unsafe_allow_html=True)
    st.markdown("""<h3 align="center">2500 RSD</h3>""",unsafe_allow_html=True)
    st.markdown("""
    <p align="center">Boja: Crna</p>
    """,unsafe_allow_html=True)
with columns_products[1]:
  with st.container(border=True,key="container_products_03"):
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")

    st.image("resources/wifi_porter_white.png",use_container_width=True)  
 
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown(f"\n \n")
    st.markdown("""<h2 align="center"> <span style="color:#60b4ff">PovežiSe</span><br>White Edition</h2>""",unsafe_allow_html=True)
    st.markdown("""<h3 align="center">2500 RSD</h3>""",unsafe_allow_html=True)
    st.markdown("""
    <p align="center">Boja: Bela</p>
    """,unsafe_allow_html=True)


# st.markdown(" [Kontaktirajte nas za veće narudžbe i personalizaciju uređaja.](#kontaktirajte-nas)")
# st.divider()

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
st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
st.markdown("""<div style="text-align: center;margin-bottom: 30px"><h1>Galerija</h1></div>""",unsafe_allow_html=True)
columns_gallery = st.columns(4)
with columns_gallery[0]:
  st.image("resources/gal_img01.jpg",use_container_width=True,)
  st.image("resources/gal_img05.jpg",use_container_width=True,)
with columns_gallery[1]:
  st.image("resources/gal_img07.jpg",use_container_width=True,)
  st.image("resources/gal_img06.jpg",use_container_width=True,)
with columns_gallery[2]:
  st.image("resources/gal_img03.jpg",use_container_width=True,)
  st.image("resources/gal_img02.jpg",use_container_width=True,)
with columns_gallery[3]:
  st.image("resources/gal_img04.jpg",use_container_width=True,)
  st.image("resources/gal_img08.jpg",use_container_width=True,) 

st.markdown("""<div style="text-align: center;margin-bottom: 30px"><h1>Često postavljana pitanja:</h1></div>""",unsafe_allow_html=True)

# Using two columns for FAQ layout
col1, col2 = st.columns(2)

with col1:
    faq1 = st.expander("Kako instalirati :blue[PovežiSe]?")
    faq1.write("Instalacija :blue[PovežiSe] uređaja je brza i jednostavna. Pratite sledeće korake:")
    faq1.write("""
    Koraci:
    1. Postavite uređaj na vidljivo i lako dostupno mesto.
    2. Otvorite aplikaciju na svom telefonu i unesite ime i šifru WiFi mreže.
    3. Prislonite telefon na uređaj :blue[PovežiSe] da biste ga povezali sa mrežom.
    4. Preuzmite PDF fajl sa QR kodom i šifrom, i postavite ga na zadnji deo uređaja, kako bi gosti mogli lako da se povežu putem QR koda.
    """)
    faq2 = st.expander("Da li uređaj radi sa svim uređajima?")
    faq2.write(":blue[PovežiSe] je kompatibilan sa svim modernim pametnim telefonima i tabletima, uz sledeće tehnologije:")
    faq2.write("""
    - **NFC** tehnologija je podržana od strane većine novijih pametnih telefona.
    - **QR kod** može da skenira svaki telefon sa kamerom.
    - **WiFi ime i šifra** omogućavaju povezivanje svih uređaja, čak i onih koji nemaju NFC ili QR podršku.
    """)
    faq4 = st.expander("Koliko uređaja mogu povezati na mrežu?")
    faq4.write(":blue[PovežiSe] omogućava povezivanje više uređaja na istu WiFi mrežu. Nema ograničenja u broju uređaja koji mogu koristiti istu mrežu, ali za optimalne performanse, preporučujemo povezivanje do 30 uređaja po mreži.")

with col2:
    faq3 = st.expander("Koje boje su dostupne?")
    faq3.write(":blue[PovežiSe] uređaj je dostupan u dve boje: bela i crna, kako bi se uklopio u svaki prostor.")
    faq5 = st.expander("Da li je :blue[PovežiSe] uređaj bezbedan?")
    faq5.write("Da, :blue[PovežiSe] koristi sigurnosne protokole koji osiguravaju da vaša WiFi mreža bude zaštićena prilikom povezivanja uređaja. Podaci su šifrovani i sigurni.")
    faq6 = st.expander("Šta ako ne mogu da povežem uređaj?")
    faq6.write("Ako imate problem sa povezivanjem, proverite sledeće:")
    faq6.write("""
    1. Uverite se da je WiFi signal dovoljno jak na mestu gde se nalazi uređaj :blue[PovežiSe].
    2. Proverite da li ste ispravno uneli ime i šifru WiFi mreže.
    3. Ako koristite NFC ili QR kod, proverite da li je vaš telefon kompatibilan sa tim tehnologijama.
    4. Ako i dalje imate problema, obratite nam se putem korisničke podrške.
    """)

st.divider()
# Kontakt forma
st.header("Kontaktirajte nas")
st.markdown("Potražite nas na [instagramu](https://www.instagram.com/povezise_official/) za više informacija o :blue[PovežiSe].")

# with st.form(key="contact_form"):
#     name = st.text_input("Vaše ime")
#     email = st.text_input("Vaš email")
#     message = st.text_area("Vaša poruka")
#     submit_button = st.form_submit_button(label="Pošaljite")
#     if submit_button:
#         st.success(f"Hvala {name}, vaša poruka je poslata!")

# Footer
st.image("resources/logo_povezise.png",width=100)

st.markdown("""
---
© 2024 PovežiSe a WebApp Landing Page by Dule_Pan.

""")
#Kontakt informacije:
# - Email: info@povezise.rs
# - Telefon: +381 64 123 4567

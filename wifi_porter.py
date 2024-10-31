import streamlit as st
from PIL import Image

# Osnovna konfiguracija stranice
st.set_page_config(page_title="WiFi Porter", page_icon="📶", layout="wide", initial_sidebar_state="auto")
# Dodavanje meta opisa (za SEO)
st.markdown("""
    <meta name="description" content="WiFi Porter - uređaj za lako povezivanje na WiFi za apartmane, hotele i stan na dan. NFC, QR kod ili klasična lozinka.">
    <meta name="keywords" content="WiFi Porter, NFC WiFi, QR kod, WiFi uređaj, prijavljivanje na WiFi">
    <meta name="author" content="WiFi Porter Team">
""", unsafe_allow_html=True)

# Sidebar opcije
# page = st.sidebar.radio("Izaberite stranicu:", ["Početna", "QR Code Generator"])
pages = {
    "Your account": [
        st.Page("pages/qr_code_generator.py", title="Kreiraj QR-code") 
    ]
}
pg = st.navigation([st.Page("pages/wifi_porter_main.py",title="Početna"),st.Page("pages/qr_code_generator.py",title="Kreiraj QR-code")],position="sidebar",expanded=True)
pg.run()

import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import tempfile
from streamlit_pdf_viewer import pdf_viewer
import fitz  # PyMuPDF

pdfmetrics.registerFont(TTFont('Roboto-Bold', './resources/Roboto-Bold.ttf'))

# Funkcija za generisanje WiFi QR koda
def generate_wifi_qr(ssid, password, encryption):
    qr_data = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    qr_img = qrcode.make(qr_data)
    return qr_img

# Postavljanje stranice i naslova
# st.set_page_config(page_title="WiFi QR Code Generator", page_icon="📶", layout="wide")

# Naslov
st.title("Generišite QR kod za prijavljivanje na WiFi mrežu")

# Unos podataka o WiFi mreži
ssid = st.text_input("Unesite naziv WiFi mreže (SSID):")
password = st.text_input("Unesite WiFi lozinku:", type="password")
encryption = st.selectbox("Odaberite vrstu enkripcije:", ["WPA2", "WEP", "None"])

# Dugme za generisanje QR koda
if st.button("Generiši QR kod"):
    if ssid and (encryption == "None" or password):
        # Generisanje QR koda
        qr_image = generate_wifi_qr(ssid, password, encryption)
        
        # Omogućavanje preuzimanja QR koda
        qr_buffer = BytesIO()
        qr_image.save(qr_buffer, format="PNG")
        qr_buffer.seek(0)

        # Prikaz QR koda
        st.image(qr_buffer, caption="Skrenirajte QR kod da biste se povezali na WiFi", use_column_width=False)

        # PDF Generation
        pdf_buffer = BytesIO()  # Buffer for the PDF
        # Define dimensions for the rectangle in mm
        rect_width_mm = 77.5  # Rectangle width in mm
        rect_height_mm = 39  # Rectangle height in mm
        # Convert mm to points (1 mm = 2.83465 points)
        rect_width_pts = rect_width_mm * mm
        rect_height_pts = rect_height_mm * mm
        c_show = canvas.Canvas(pdf_buffer, pagesize=(rect_width_pts, rect_height_pts))
        width, height = A4

        # Draw a rectangle outline (adjust coordinates as needed)
        rect_x, rect_y = 20 * mm, height - 80 * mm
        rect_width, rect_height = 72 * mm, 36 * mm

        # Set line width for border
        border_line_width = 2  # Set your desired line width here
        c_show.setLineWidth(border_line_width)  # Set the line width

        # Set dash pattern for dashed border
        c_show.setDash(3, 2)  # 3 mm dashes and 2 mm gaps
        c_show.setStrokeColorRGB(0, 0, 0)  # Set border color to black
        # c.setFillColorRGB(1, 1, 1)  # Ensure rectangle is filled with white        
        c_show.rect(1,7.5, rect_width, rect_height, stroke=1, fill=0)

        # Save QR code to a temporary file and add to PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            qr_image.save(tmp_file, format="PNG")
            tmp_file_path = tmp_file.name
        c_show.drawImage(tmp_file_path, 4.5 * mm, 9.5 * mm, width=23 * mm, height=23 * mm)


        # Insert QR Code on the left side
        qr_x, qr_y = rect_x + 5 * mm, rect_y + 5 * mm
        # c.drawImage(qr_buffer, qr_x, qr_y, width=25 * mm, height=25 * mm)

        # Add WiFi credentials text on the right side
        text_x =  35 * mm
        text_y =  21 * mm
        c_show.setFont("Roboto-Bold",7.5)
        c_show.drawString(text_x, text_y, f"WiFi: {ssid}")
        c_show.drawString(text_x, 18 * mm, f"Pass: {password}")

        # Save the PDF
        c_show.save()
        pdf_buffer.seek(0)  # Move to the start of the buffer
        
        pdf_viewer(pdf_buffer.getvalue(), width=600)
        # Convert PDF buffer to image
        # with fitz.open(stream=pdf_buffer, filetype='pdf') as doc:
        #     for page in doc:
        #         # Get original page dimensions
        #         original_width = page.rect.width
        #         original_height = page.rect.height
        #         pix = page.get_pixmap(matrix=fitz.Matrix(200/72, 200/72))  # Render page to image
        #         img_buffer = BytesIO(pix.tobytes("png"))  # Convert to PNG format
        #                 # st.image(qr_buffer, caption="Skrenirajte QR kod da biste se povezali na WiFi", use_column_width=False)

        #         st.image(img_buffer, caption="Converted PDF to Image", use_column_width=False)
        #         break  # Only show the first page

        #############################################################################################################
        ########################################## Ovde je za skidanje PDF ##########################################
        # PDF Generation
        pdf_print_buffer = BytesIO()  # Buffer for the PDF
        c_print = canvas.Canvas(pdf_print_buffer, pagesize=A4)
        # Set line width for border
        c_print.setLineWidth(border_line_width)  # Set the line width
        # Set dash pattern for dashed border
        c_print.setDash(3, 2)  # 3 mm dashes and 2 mm gaps
        c_print.setStrokeColorRGB(0, 0, 0)  # Set border color to black
        # c.setFillColorRGB(1, 1, 1)  # Ensure rectangle is filled with white        
        c_print.rect(1,7.5, rect_width, rect_height, stroke=1, fill=0)
        # Save QR code to a temporary file and add to PDF
        c_print.drawImage(tmp_file_path, 4.5 * mm, 9.5 * mm, width=23 * mm, height=23 * mm)
        # Add WiFi credentials text on the right side
        c_print.setFont("Roboto-Bold",7.5)
        c_print.drawString(text_x, text_y, f"WiFi: {ssid}")
        c_print.drawString(text_x, 18 * mm, f"Pass: {password}")
        # Save the PDF
        c_print.save()
        pdf_print_buffer.seek(0)  # Move to the start of the buffer

        # st.download_button(
        #     label="Preuzmite QR kod",
        #     data=buffer.getvalue(),
        #     file_name="wifi_qr_code.png",
        #     mime="image/png"
        # )
        st.download_button(
            label="Preuzmite QR PDF",
            data=pdf_print_buffer,
            file_name="wifi_pdf.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Molimo unesite validne podatke o mreži.")

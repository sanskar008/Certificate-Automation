import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, black
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

# ========== CONFIG ==========
excel_file = "data_file.xlsx"
template_pdf = "template.pdf"  # optional: if you already have a background certificate
output_folder = "certificates/"  # folder where PDFs will be saved

# ========== STEP 1: Load Excel ==========
data = pd.read_excel(excel_file, engine="openpyxl")

# ========== STEP 2: Generate Certificates ==========
for index, row in data.iterrows():
    name = row["Name"]
    course = row["Course"]
    date = row["Date"]
    cert_id = row["Certificate ID"]

    # Create a temporary PDF with text
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    width, height = A4

    # Match updated template positions
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, height - 280, name)  # Name

    c.setFillColor(HexColor("#2E4057"))
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(width / 2, height - 380, course)  # Course

    c.setFillColor(black)
    c.setFont("Helvetica", 14)
    c.drawString(100, 120, f"Date: {date}")
    c.drawRightString(width - 100, 120, f"ID: {cert_id}")

    c.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Read your existing template
    existing_pdf = PdfReader(open(template_pdf, "rb"))
    output = PdfWriter()
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    # Save output
    output_filename = f"{output_folder}/{name.replace(' ', '_')}_certificate.pdf"
    with open(output_filename, "wb") as out_f:
        output.write(out_f)

    print(f"Generated certificate for {name}")

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, gold
from reportlab.platypus import Image


c = canvas.Canvas("template.pdf", pagesize=A4)
width, height = A4

# Add logo at the top center
logo_path = "logo.png"
logo_width = 100
logo_height = 100
logo_x = (width - logo_width) / 2
logo_y = height - 100
try:
    c.drawImage(
        logo_path, logo_x, logo_y, width=logo_width, height=logo_height, mask="auto"
    )
except Exception as e:
    print(f"Warning: Could not add logo: {e}")

# Draw decorative border
c.setStrokeColor(HexColor("#2E4057"))
c.setLineWidth(3)
c.rect(30, 30, width - 60, height - 60)
c.setLineWidth(1)
c.rect(40, 40, width - 80, height - 80)

# Add decorative corner elements
corner_size = 20
c.setFillColor(HexColor("#2E4057"))
for x, y in [(50, height - 70), (width - 70, height - 70), (50, 50), (width - 70, 50)]:
    c.circle(x, y, corner_size, fill=1)

# Title with elegant styling
c.setFillColor(HexColor("#2E4057"))
c.setFont("Helvetica-Bold", 36)
c.drawCentredString(width / 2, height - 130, "CERTIFICATE")
c.setFont("Helvetica", 20)
c.drawCentredString(width / 2, height - 160, "OF COMPLETION")

# Decorative line under title
c.setStrokeColor(HexColor("#D4A574"))
c.setLineWidth(2)
c.line(width / 2 - 100, height - 180, width / 2 + 100, height - 180)

# Subtitle with better spacing
c.setFillColor(black)
c.setFont("Helvetica", 18)
c.drawCentredString(width / 2, height - 220, "This is to certify that")

# Name placeholder with underline
c.setFont("Helvetica-Bold", 28)
c.drawCentredString(width / 2, height - 280, "")
# Add underline for name
c.setStrokeColor(black)
c.setLineWidth(1)
c.line(width / 2 - 150, height - 290, width / 2 + 150, height - 290)

# Course description
c.setFont("Helvetica", 18)
c.drawCentredString(width / 2, height - 340, "has successfully completed the course on")

# Course placeholder with underline
c.setFillColor(HexColor("#2E4057"))
c.setFont("Helvetica-Bold", 22)
c.drawCentredString(width / 2, height - 380, "")
# Add underline for course
c.setStrokeColor(black)
c.setLineWidth(1)
c.line(width / 2 - 120, height - 390, width / 2 + 120, height - 390)

# Achievement message
c.setFillColor(black)
c.setFont("Helvetica-Oblique", 16)
c.drawCentredString(
    width / 2, height - 430, "in recognition of dedication and achievement"
)

# Date section with improved styling
c.setFont("Helvetica", 14)
c.drawString(100, 120, "Date: ")

# Add signature line
c.setStrokeColor(black)
c.setLineWidth(1)
c.line(width - 200, 100, width - 80, 100)
c.setFont("Helvetica", 12)
c.drawCentredString(width - 140, 85, "Authorized Signature")

c.save()
print("Created template.pdf")

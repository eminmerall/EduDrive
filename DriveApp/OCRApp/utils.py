import pdfplumber
from docx import Document
import pytesseract
from PIL import Image

def process_pdf(uploaded_file):
    text = ''
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_docx(uploaded_file):
    doc = Document(uploaded_file)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

def process_image(uploaded_file):
    image = Image.open(uploaded_file)
    text = pytesseract.image_to_string(image)
    return text
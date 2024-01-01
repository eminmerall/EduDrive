from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import OCRDocument
import pytesseract
from PIL import Image
import pdfplumber
from docx import Document
from .forms import OCRDocumentForm
from django.contrib import messages

def process_pdf(file_name):
    text = ''
    with pdfplumber.open(file_name) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_docx(file_name):
    doc = Document(file_name)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

def process_image(file_name):
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)
    return text

def ocr_document(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name, file_extension = uploaded_file.name, uploaded_file.name.split('.')[-1]

        if file_extension.lower() == 'pdf':
            text = process_pdf(uploaded_file)
        elif file_extension.lower() == 'docx':
            text = process_docx(uploaded_file)
        else:
            text = process_image(uploaded_file)

        ocr_document = OCRDocument.objects.create(
            title=request.POST.get('title', ''),
            description=request.POST.get('description', ''),
            ocr_text=text
        )

        return redirect('ocr_result', pk=ocr_document.pk)

    return render(request, 'ocr-upload.html')

def ocr_result(request, pk):
    ocr_document = get_object_or_404(OCRDocument, pk=pk)

    if request.method == 'POST':
        form = OCRDocumentForm(request.POST, instance=ocr_document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved successfully!')
            return redirect('ocr_document')  # Önceki sayfaya yönlendir
        else:
            messages.error(request, 'Error occurred. Please check the form.')
    else:
        form = OCRDocumentForm(instance=ocr_document)

    return render(request, 'ocr-result.html', {'form': form, 'ocr_document': ocr_document})
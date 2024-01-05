from django import forms
from .models import OCRDocument
from django.forms import widgets

class OCRDocumentForm(forms.ModelForm):
    class Meta:
        model = OCRDocument
        fields = ['description', 'file']

    def __init__(self, *args, **kwargs):
        super(OCRDocumentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control','rows':'3'})
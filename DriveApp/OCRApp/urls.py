from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.ocr_document, name='ocr_document'),
    path('result/<int:pk>/', views.ocr_result, name='ocr_result'),
]
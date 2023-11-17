from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("files", views.files),
    path("files/<slug:slug>",views.files_details)
]

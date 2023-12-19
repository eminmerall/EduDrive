from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("files", views.files, name="files_page"),
    path("files/<slug:slug>",views.file_details, name="file_details")
]

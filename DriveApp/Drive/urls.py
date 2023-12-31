from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),
    path("files", views.files, name="files_page"),
    path("files/<slug:slug>",views.file_details, name="file_details"),
    path('file-upload', views.file_upload, name='file_upload'),
    path('file-dowload/<slug:file_slug>/', views.download_file, name='download_file'),
    path('user-files', views.user_files, name='user_files'),
    path('edit-file/<slug:file_slug>/', views.edit_file, name='edit_file'),
    path('add-school', views.add_school, name='add_school'),
    path('add-department', views.add_department, name='add_department'),
    path('add-lesson', views.add_lesson, name='add_lesson'),
    path('add-outhor', views.add_outhor, name='add_outhor')
]

from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="home_page"),
    path("files", views.files, name="files_page"),
    path("files/<slug:slug>",views.file_details, name="file_details"),
    path('file-upload', views.file_upload, name='file_upload'),
    path('file-dowload/<slug:file_slug>/', views.download_file, name='download_file'),
    path('user-files', views.user_files, name='user_files'),
    path('edit-file/<slug:file_slug>/', views.edit_file, name='edit_file'),
    path('scholls', views.scholl_list, name='scholl_list'),
    path('add-school', views.add_school, name='add_school'),
    path('departments/', views.department_list, name='department_list'),
    path('add-department', views.add_department, name='add_department'),
    path('add-lesson', views.add_lesson, name='add_lesson'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('add-outhor', views.add_outhor, name='add_outhor'),
    path('outhors/', views.outhor_list, name='outhor_list'),
    path('profile-list/', views.profile_list, name='profile_list'),
    path('404/', TemplateView.as_view(template_name='Drive/404-Message.html'), name='404'),
]

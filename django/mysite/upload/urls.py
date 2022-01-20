from django.urls import path
from . import views

urlpatterns = [
    # Upload file using Model Form
    path('', views.upload_file, name='upload_file'),

    # View file list
    path('files/', views.file_list, name='files_list'),
]
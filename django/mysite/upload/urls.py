from unicodedata import name
from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [
    # Upload file using Model Form
    path('', views.upload_file, name='upload_file'),

    # View file list
    path('files/', views.files_list, name='files_list'),
]
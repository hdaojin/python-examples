from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadFileModel
from .forms import UploadFileForm
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'upload/index.html')

# Upload file using Model Form
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():  # 执行validate, clean_file
            form.save()
            return redirect(reverse('upload:files_list'))
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form, 'heading': 'Upload file with Model Form'})

def files_list(request):
    log_files = UploadFileModel.objects.all().order_by('-log_date', '-uploaded_date')
    return render(request, 'upload/file_list.html', {'log_files': log_files})

from audioop import reverse
from django.shortcuts import render, redirect
from django.template.defaultfilters import filesizeformat
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
        if form.is_valid():
            form.save()
            return redirect(reverse('files_list'))
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form, 'heading': 'Upload file with Model Form'})

def file_list(request):
    files = UploadFileModel.objects.all().order_by('-uploaded_at')
    return render(request, 'upload/file_list.html', {'files': files})

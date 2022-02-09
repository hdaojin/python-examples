from tabnanny import verbose
from unicodedata import name
from django import forms
from .models import UploadFileModel


# ModelForm
# https://docs.djangoproject.com/zh-hans/4.0/topics/forms/modelforms/


author_names = ['黄金强', '周文', '邓波']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = "__all__"
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '你的姓名...'}),
            'author_role': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'log_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'class_type': forms.Select(attrs={'class': 'form-control'}),
            'module_list': forms.Select(attrs={'class': 'form-control'}),
            'log_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_author_name(self):
        author_name = self.cleaned_data['author_name']
        if author_name not in author_names:
            raise forms.ValidationError("你的姓名不在列表中。")
        return author_name
    
        
    def clean_log_file(self):
        log_file = self.cleaned_data['log_file']
        ext = log_file.name.split('.')[-1].lower()
        if ext not in ["doc", "docx", "pdf"]:
            raise forms.ValidationError("只能上传doc, docx, pdf格式的文件。")
        return log_file
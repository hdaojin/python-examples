from django import forms
from .models import UploadFileModel

# ModelForm
# https://docs.djangoproject.com/zh-hans/4.0/topics/forms/modelforms/



class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ["title", "author", "role", "date", "file"]

        def clean_file(self):
            file = self.cleaned_data['file']
            ext = file.name.split('.')[-1].lower()
            if ext not in ["doc", "docx", "pdf"]:
                raise forms.ValidationError("Only doc, docx, pdf files are allowed.")
            return file

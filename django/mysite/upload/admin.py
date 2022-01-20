from django.contrib import admin
from .models import UploadFileModel

# Register your models here.
@admin.register(UploadFileModel)
class UploadFileModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'role', 'date', 'file', 'uploaded_at')
    list_filter = ('title', 'author', 'role', 'date', 'uploaded_at')
    search_fields = ('title', 'author', 'role', 'date', 'file')

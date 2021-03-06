# Generated by Django 3.2.11 on 2022-01-20 03:37

import datetime
from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_uploadfile_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('date', models.DateField(default=datetime.date.today)),
                ('file', models.FileField(null=True, upload_to=upload.models.user_dierctory_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]

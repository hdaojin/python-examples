from logging import PlaceHolder
from operator import attrgetter
from django.db import models
import os
from datetime import date

#import uuid

# Create your models here.
TITLE_CHOICES = [
    ("class", "第46届世界技能大赛网络系统管理项目精英班训练日志"),
    ("training", "第46届世界技能大赛网络系统管理项目中国集训队集训日志"),
]

ROLE_CHOICES = [
    (
        "Coach",
        "教练",
    ),
    (
        "Competitor",
        "选手",
    ),
    (
        "Student",
        "学生",
    ),
]

# Define user directory path
def user_dierctory_path(instance, filename):
    # ext = filename.split('.')[-1]
    # filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


# return os.path.join('files', str(instance.upload_date), filename)


class UploadFileModel(models.Model):
    title = models.CharField(max_length=100, choices=TITLE_CHOICES, default="class")
    author = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="Student", verbose_name="角色")
    date = models.DateField(default=date.today)
    file = models.FileField(upload_to=user_dierctory_path, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title



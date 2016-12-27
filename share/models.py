from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
import os
from django import forms

# Create your models here.

# model for files uploads

class File(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d', help_text="Choose the file to upload.")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    password_set = models.BooleanField(default=False, help_text="Do you want to set any password to the uploaded file")
    password = models.CharField(max_length=20, null=True, blank=True, help_text="Password of the file")
    day_1weeklater = date.today() + timedelta(days = 7)
    expiry_date = models.DateField(default=day_1weeklater, help_text="Choose the expiry date of the file. NOTE: By default, the file would expire after 7 days of uploading")
    public = models.BooleanField(default=False, help_text="Do you want the file to appear in the public repo")

    def __str__(self):
        if self.uploaded_by is None:
            return self.filename() + " uploaded by Guest Account"
        else:
            return self.filename() + " uploaded by " + self.uploaded_by.first_name

    def filename(self):
        return os.path.basename(self.file.name)

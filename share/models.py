# various imported libraries
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
import os
from django import forms

# model for files uploads
class File(models.Model):
    # uploaded file
    file = models.FileField(upload_to='%Y/%m/%d', help_text="Choose the file to upload.")
    # User who uploaded the file
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # is a password set on the file
    password_set = models.BooleanField(default=False, help_text="Do you want to set any password to the uploaded file")
    # password on the file
    password = models.CharField(max_length=150, null=True, blank=True, help_text="Password of the file")
    # calculating the default expiry date
    day_1weeklater = date.today() + timedelta(days = 7)
    # expiry date of the file
    expiry_date = models.DateField(default=day_1weeklater, help_text="Choose the expiry date of the file. NOTE: By default, the file would expire after 7 days of uploading")
    # make the file available in th public repo
    public = models.BooleanField(default=False, help_text="Do you want the file to appear in the public repo")

    def __str__(self):
        return self.filename() + " uploaded by " + self.uploaded_by.first_name

    def filename(self):
        return os.path.basename(self.file.name)

    def delete(self):
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)

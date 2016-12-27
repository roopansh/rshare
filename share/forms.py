from django import forms
from django.contrib.auth.models import User
from share.models import File
from datetime import date, timedelta

class FileForm(forms.Form):
    file = forms.FileField(label="File to upload")
    password_set = forms.BooleanField(label="Set password ?", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    expiry_date = forms.DateField(label="Expiry date", widget=forms.SelectDateWidget, initial=date.today()+ timedelta(days=7))
    public = forms.BooleanField(label="Make Public", required=False)
    class Meta:
        model = File
        fields = ['file', 'password_set', 'password', 'expiry_date', 'public']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


# various imported libraries
from django import forms
from django.contrib.auth.models import User
from share.models import File
from datetime import date, timedelta

# Form for uploading the files
class FileForm(forms.Form):
    #File
    file = forms.FileField(label="File to upload")
    # whether the password is set or not
    password_set = forms.BooleanField(label="Set password ?", required=False)
    # setting the password
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    # setting the expiry date
    expiry_date = forms.DateField(label="Expiry date", widget=forms.SelectDateWidget, initial=date.today()+ timedelta(days=7))
    # making public
    public = forms.BooleanField(label="Make Public", required=False)
    
    class Meta:
        model = File
        fields = ['file', 'password_set', 'password', 'expiry_date', 'public']


# Form for user registration
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
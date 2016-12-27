from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import File
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, FileForm

def home(request):
    return render(request, 'share/home.html')

def index(request):
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        newfile = File()
        # get the file
        newfile.file = request.FILES['file']
        # uploaded by
        if request.user.is_authenticated :
            newfile.uploaded_by = request.user
        else:
            newfile.uploaded_by = None
        # set the password
        password_set = request.POST.get('password_set', False)
        if password_set:
            newfile.password_set = True
            newfile.password = request.POST['password']
        else:
            newfile.password_set = False
            newfile.password = ""
        # make the file public
        public = request.POST.get('public', False)
        if public:
            newfile.public = True
        else:
            newfile.public = False
        # set the expiry date
        expiry_date_year = int(request.POST['expiry_date_year'])
        expiry_date_month = int(request.POST['expiry_date_month'])
        expiry_date_day = int(request.POST['expiry_date_day'])
        newfile.expiry_date = date(expiry_date_year, expiry_date_month, expiry_date_day)
        newfile.save()
        pk = newfile.pk
        link = str(request.get_host())+"/share/download/"+str(pk)
        context = {'file_download':link, 'form':form}
        return render(request, 'share/index.html', context)
    context = {'form':form, "error_message":"not valid"}
    return render(request, 'share/index.html', context)


def public(request):
    publicFiles = File.objects.filter(public="True", expiry_date__gte=date.today() - timedelta(days=2))
    return render(request, 'share/publiclist.html', {'publicFiles': publicFiles, 'today':date.today()- timedelta(days=1)})


def downloadfile(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    if file.expiry_date < date.today():
        return render(request, 'share/download.html', {'expired':True, 'file_details':str(file)})
    elif file.password_set:
        return render(request, 'share/download.html', {'file_id':file_id, 'password_set':True, 'file_details':str(file)})
    else:
        file = File.objects.get(pk=file_id)
        return render(request, 'share/download.html', {'success': True, 'file': file, 'file_details':str(file)})

def password_validate(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    password = file.password
    if request.POST['password']==password:
        file = File.objects.get(pk=file_id)
        return render(request, 'share/download.html', {'success': True, 'file':file, 'file_details':str(file)})
    else:
        return render(request, 'share/download.html', {'error_message': "Wrong Password",'file_id': file_id, 'password_set':True, 'file_details':str(file)})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'share/home.html')
    context = {
        "form": form,
    }
    return render(request, 'share/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'share/home.html')
            else:
                return render(request, 'share/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'share/login.html', {'error_message': 'Invalid login'})
    return render(request, 'share/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'share/home.html')

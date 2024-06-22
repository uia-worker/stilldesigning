from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Prompt, UploadedFile
from .forms import UploadFileForm
from .forms import FileListForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.template import RequestContext

# from app.forms import SimpleForm, PostForm
# from app.models import Post

import pdfplumber
from django.core.files import File
from .models import User
from .models import Prompt
from .forms import CreateUserFrom


def registerPage(request):
    form = CreateUserFrom()


    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/register.html" % theme, context)

def write(request, id):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Prompt.objects.get(pk=id)
    #typingPrint(data)
    return render(request, "%s/write.html" % theme, {"prompt": data})

def home_redirect_view(request):
    return redirect("/promptform")

def promptdetail(request, id):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Prompt.objects.get(pk=id)
    return render(request, "%s/promptdetail.html" % theme, {"prompt": data})

def userdetail(request, id):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = User.objects.get(pk=id)
    return render(request, "%s/userdetail.html" % theme, {"user": data})

def prompt(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = Prompt.objects.all()
    return render(request, "%s/prompt.html" % theme, {'prompts':data})

def promptform(request):
    navn = request.POST.get('navn')
    tittel = request.POST.get('tittel')
    tekst = request.POST.get('tekst')

    if tittel and tekst and navn:
        prompt = Prompt(tittel=tittel, tekst=tekst, navn=navn)
        prompt.save()
        return HttpResponseRedirect('/prompt')
    return render(request, 'bootstrap/promptform.html')

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    telephone = request.POST.get('telephone')
    name = request.POST.get('name')


    if username and password and email and name and telephone:
        user = User(username=username, password=password, email=email, name=name)
        user.save()
        return HttpResponseRedirect('/user')
    return render(request, 'bootstrap/form.html')

def user(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    data = User.objects.all()
    return render(request, "%s/user.html" % theme, {'users':data})

def promptdelete(request, id):
    Prompt.objects.get(pk=id).delete()
    return HttpResponseRedirect('/prompt')

def userdelete(request, id):
    User.objects.get(pk=id).delete()
    return HttpResponseRedirect('/user')

def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/upload_file.html" % theme, {'form': form, 'files': files})


def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response


def read_file(request):
    file_path = settings.BASE_DIR / "media/uploads/uml-2.5.1-formal-17-12-05.pdf"
    #file_path = settings.BASE_DIR / "media/uploads/simple.pdf"

    with pdfplumber.open(file_path) as pdf:
        first_page = pdf.pages[0]
        context = {'first_page': first_page.extract_text_simple()}
        print(context)
    
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    return render(request, "%s/pdf2txt.html" % theme, context)

def filelist(request):
    theme = getattr(settings, "VITASS_THEME", "bootstrap")
    files = UploadedFile.objects.all()
    return render(request, "%s/filelist.html" % theme, {'files': files})


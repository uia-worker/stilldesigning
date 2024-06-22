from django import forms
from .models import UploadedFile
from .models import FileList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# from martor.fields import MartorFormField
# from app.models import Post

class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    # description = MartorFormField()
    # wiki = MartorFormField()


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ["file"]

class SimpleTestForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())

class FileListForm(forms.ModelForm):
    class Meta:
        model = FileList
        fields = ['fileslistbox']
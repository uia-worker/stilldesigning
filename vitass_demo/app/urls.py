"""
from django.urls import path

from app.views import (
    home_redirect_view,
    simple_form_view,
    post_form_view,
    test_markdownify,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("simple-form/", simple_form_view, name="simple_form"),
    path("post-form/", post_form_view, name="post_form"),
    path("test-markdownify/", test_markdownify, name="test_markdownify"),
]
"""
from django.urls import path
from . import views

from app.views import (
    home_redirect_view,
    upload_file_view,
    promptdelete,
)

urlpatterns = [
    path("", home_redirect_view, name="home_redirect"),
    path("upload/", upload_file_view, name='upload_file'),
    path("download/<int:file_id>/", views.download_file, name='download_file'),
    path("pdf2txt/", views.read_file, name='read_file'),
    path("form/", views.register, name="register"),
    path("prompt/", views.prompt, name="prompt"),
    path("promptform/", views.promptform, name="promptform"),
    path("prompts/<int:id>/", views.promptdetail, name="promptdetail"),
    path("promptdelete/<int:id>/", views.promptdelete, name="promptdelete"),
    path("user/", views.user, name="user"),
    path("users/<int:id>/", views.userdetail, name="userdetail"),
    path("userdelete/<int:id>/", views.userdelete, name="userdelete"),
    path("write/<int:id>", views.write, name="write"),
    path("register/", views.registerPage, name="registerPage"),
    path("filelist/", views.filelist, name="filelist"),
    path("pdf/<int:id>/", views.textFindNounsAndVerbs, name="textfindnouns"),

    path("text/", views.text, name="text"),
    path("text/<int:id>/", views.textdetail, name="textdetail"),
    path("textform/", views.addtext, name="addtext"),
    path("textdelete/<int:id>/", views.textdelete, name="textdelete"),

    path("pdf/", views.pdf, name="pdf"),
    path("pdfdelete/<int:id>/", views.pdfdelete, name="pdfdelete"),

]

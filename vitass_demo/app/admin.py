from .models import Movie
from django.contrib import admin
from .models import User
from .models import Prompt

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Prompt)
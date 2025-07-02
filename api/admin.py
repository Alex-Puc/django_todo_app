from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Newsfeed, Todo

# Register your models here.
@admin.register(Newsfeed)
class Newsfeed(TranslatableAdmin):
    pass

admin.site.register(Todo)
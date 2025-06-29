from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Newsfeed

# Register your models here.
@admin.register(Newsfeed)
class Newsfeed(TranslatableAdmin):
    pass
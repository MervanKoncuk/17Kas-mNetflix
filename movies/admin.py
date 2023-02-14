from django.contrib import admin
from .models import *
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('isim', 'kategori')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Kategori)
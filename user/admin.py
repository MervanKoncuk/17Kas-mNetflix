from django.contrib import admin
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('isim', 'olusturan', 'olusturulmaTarihi', 'id', 'slug')
    list_filter = ('olusturan',)
    readonly_fields = ('id', 'slug')
# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Hesap)
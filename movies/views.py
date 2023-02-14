from django.shortcuts import render
from .models import *
from user.models import *
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, slug, profilId):
    profil = Profile.objects.get(id = profilId, slug = slug)
    profiller = Profile.objects.filter(olusturan = request.user)
    filmler = Movie.objects.all()
    populer = Movie.objects.filter(kategori__isim = "Popüler")
    gundemde = Movie.objects.filter(kategori__isim = "Gündemde")
    context = {
        'filmler':filmler,
        'populer':populer,
        'gundemde':gundemde,
        'profil':profil,
        'profiller':profiller
    }
    return render(request, 'browse-index.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        # değişken ismi ile tırnak içerisinde olan ismin aynı olması zorunlu değil
        kullaniciAdi = request.POST['kullanici']
        email = request.POST['email']
        tel = request.POST['tel']
        resim = request.FILES['resim'] # FILES: formdan gelen dosyayı alır
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre1 == sifre2:
            if User.objects.filter(username = kullaniciAdi).exists():
                messages.error(request, 'Kullanıcı adı kullanılıyor')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'Email Kullanımda')
                return redirect('register')
            elif len(sifre1) < 6:
                messages.error(request, 'Şifre en az 6 karakter olması gerekiyor')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = kullaniciAdi,
                    email = email,
                    password = sifre1
                )
                Hesap.objects.create(
                    user = user,
                    resim = resim,
                    tel = tel
                )
                user.save()
                messages.success(request, 'Kayıt başarılı')
                return redirect('index')
        else:
            messages.error(request, 'Şifreler uyuşmuyor')
            return redirect('register')
    return render(request, 'register.html')

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Başarılı')
            return redirect('profiles')
        else:
            messages.error(request, 'kullanici adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'login.html')


def profiles(request):
    profiller = Profile.objects.filter(olusturan = request.user)
    context = {
        'profiller':profiller
    }
    return render(request, 'browse.html', context)

def create(request):
    form = ProfileForm()
    profiller = Profile.objects.filter(olusturan = request.user)
    print(Profile.objects.filter(olusturan = request.user).count())
    if request.method == 'POST':
        if 'olustur' in request.POST:
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                if Profile.objects.filter(olusturan = request.user).count() < 4:
                    profil = form.save(commit=False)
                    profil.olusturan = request.user
                    profil.save()
                    messages.success(request, 'Profil Oluşturuldu')
                    return redirect('profiles')
                else:
                    messages.error(request, 'En fazla 4 profil oluşturabilirsiniz')
                    return redirect('profiles')
        if 'sil' in request.POST:
            profileId = request.POST['profileId']
            profil = Profile.objects.get(id = profileId)
            profil.delete()
            messages.success(request, 'Profil Silindi')
            return redirect('create')
    context = {
        'form':form,
        'profiller':profiller
    }
    return render(request, 'create.html', context)


def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')

def hesap(request):
    profil = request.user.hesap
    
    context = {
        'profil': profil
    }
    return render(request, 'hesap.html', context)


def reset(request):
    print(request.user.password)
    if request.method == 'POST':
        eski = request.POST['eski']
        yeni1 = request.POST['yeni1']
        yeni2 = request.POST['yeni2']

        user = authenticate(request, username = request.user, password = eski)

        if user is not None:
            if yeni1 == yeni2:
                kullanici = request.user
                # şifreyi değiştirmek için
                kullanici.set_password(yeni1)
                kullanici.save()
                messages.success(request, 'Şifreniz Güncellendi')
                return redirect('login')
            else:
                messages.error(request, 'Şifreler uyuşmuyor')
                return redirect('reset')
        else:
            messages.error(request, 'Mevcut şifreniz hatalı')
            return redirect('reset')
    return render(request, 'resetPassword.html')


def update(request):
    user = request.user
    hesabim = request.user.hesap
    # formu html'den kendimiz oluşturursak
    # if request.method == 'POST':
    #     kullanici = request.POST['kullanici']
    #     email = request.POST['email']
    #     tel = request.POST['tel']
    #     resim = request.FILES['resim']

    #     user.username = kullanici
    #     user.email = email
    #     user.save()
    #     hesabim.tel = tel
    #     hesabim.resim = resim
    #     hesabim.save()
    #     messages.success(request, 'Bilgileriniz güncellendi')
    #     return redirect('hesap')

    # formu forms.py'dan kullandımığımzda
    form = UserForm(instance = user)
    hesapForm = HesapForm(instance = hesabim)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        hesapForm = HesapForm(request.POST, request.FILES, instance = hesabim)
        if form.is_valid() and hesapForm.is_valid():
            form.save()
            hesapForm.save()
            messages.success(request, 'Bilgiler güncellendi')
            return redirect('hesap')
    context = {
        'user':user,
        'hesabim':hesabim,
        'form':form,
        'hesapForm':hesapForm
    }
    return render(request, 'update.html', context)


def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Kullanici silindi')
    return redirect('index')
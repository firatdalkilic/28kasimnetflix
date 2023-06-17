from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def UserRegister(request):
    # form =UserForm()
    # if request.method == 'POST':
    #     form =UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("index")
    # context={
    #     "form": form,
    # }
    # return render(request,"register.html",context)
    if request.method == 'POST':
        isim=request.POST["isim"]
        soyisim=request.POST["soyisim"]
        email=request.POST["email"]
        resim=request.POST["resim"]
        tel=request.POST["tel"]
        dogum=request.POST["dogum"]
        sifre1=request.POST["sifre1"]
        sifre2=request.POST["sifre2"]
        
        if sifre1 == sifre2:
            if User.objects.filter(email = email).exists():
                messages.error(request,"Kullanılan mail")
                return redirect("register")
            elif len(sifre1)<6:
                messages.error(request,"Şifre en az 6 karakter olmalı")
                return redirect("register")
            else:
                user=User.objects.create_user(username=email, email=email,password=sifre1)
                Kullanici.objects.create(
                    user=user,
                    isim=isim,
                    soyisim=soyisim, 
                    email=email,
                    resim=resim,
                    tel=tel,
                    dogum=dogum
                )
                user.save()
                messages.success(request,"Kullanıcı oluşturuldu")
                return redirect("login")
    return render(request,"register.html")
    
    
def Login(request):
    if request.method == "POST" :
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Giriş Yapıldı")
            return redirect("profil")
        else:
            messages.error(request,"Kullanıcı bulunamadı")
            return redirect("login")
    return render(request,"login.html")
def profiles(request):
    profiller=Profiles.objects.filter(owner=request.user)
    context={
        "profiller": profiller
    }
    return render(request,"browse.html",context)
def createProfile(request):
    form=ProfileForm()
    if request.method=="POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.owner=request.user
            profile.save()
            return redirect("profil")
    context={
            "form": form,
        }
    return render(request,"create.html",context)

def userLogout(request):
    logout(request)
    messages.success(request,"çıkış yapıldı")
    return redirect("index")

def hesap(request):
    user=request.user.username
    context = {
        "user":user
        }
    return render(request,"hesap.html",context)
def userDelete(request):
    user=request.user
    user.delete()
    messages.success(request,"Hesabınız silindi")
    return redirect("index")
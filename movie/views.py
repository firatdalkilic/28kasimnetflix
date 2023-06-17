from django.shortcuts import render
from .models import *
from user.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def movies(request,id):
    filmler=Movie.objects.all()
    profile=Profiles.objects.get(id = id)
    profiller=Profiles.objects.filter(owner=request.user)
    context={
        "filmler":filmler,
        "profile":profile,
        "profiller":profiller
        
    }
    return render(request,"browse-index.html",context)
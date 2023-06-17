
from django.urls import path,include
from .views import *


urlpatterns = [
   
    path('register/',UserRegister,name="register" ),
    path('login/',Login,name="login" ),
    path('profiles/',profiles,name="profil" ),
    path('create/',createProfile, name="create" ),
    path('logout/',userLogout, name="logout" ),
    path('hesap/',hesap, name="hesap" ),
    path('delete/',userDelete, name="delete" ),
    
    
]
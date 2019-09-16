"""Caieirasfy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from artista.views import ArtistaList, ArtistaDetail
from caieirasfy.views import MusicaViewsSets, MusicaDetail, MusicaList

router = routers.DefaultRouter()
router.register(r'musica', MusicaViewsSets)

urlpatterns = [
    path('artista/',ArtistaList.as_view()),
    path('artista/<int:id>',ArtistaDetail.as_view()),
    path('musica/',MusicaList.as_view()),
    path('musica/<int:id>',MusicaDetail.as_view()),
    path('admin/',admin.site.urls),
    path('api/', include(router.urls)),
    path('auth-api/',obtain_auth_token)

]
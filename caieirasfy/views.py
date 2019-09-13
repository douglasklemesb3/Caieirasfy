from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from caieirasfy.models import Musica
from caieirasfy.serializers import MusicaSerializer

class MusicalViewsSets(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    serializer_class = ['^nome','genero_musical']
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer





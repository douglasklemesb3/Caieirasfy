from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from caieirasfy.models import Musica
from caieirasfy.serializers import MusicaSerializer

class MusicaViewsSets(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome','^artista','^genero_musical']
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class MusicaList(views.APIView):
    def get(self, request):
        musica = Musica.object.all()
        serializer = MusicaSerializer(musica,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = MusicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response

from artista.models import Artista
from artista.serializers import ArtistaLightSerializer, ArtistaSerializer


class ArtistaList(views.APIView):
    def get(self,request):
        artista =  Artista.objects.all()
        serializer = ArtistaLightSerializer(artista, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ArtistaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ArtistaDetail(views.APIView):
    def get_object(self, id):
        try:
            return Artista.objects.get(id=id)
        except:
            raise Http404
    def get(self, request, id):
        artista = self.get_object(id)
        serializer = ArtistaSerializer(artista)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self,request,id):
        artista = self.get_object(id)
        serializer = ArtistaSerializer(artista, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


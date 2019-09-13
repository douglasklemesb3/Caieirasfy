
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from caieirasfy.models import Musica
from caieirasfy.serializers import MusicaSerializer, MusicaLightSerializer


class MusicaViewsSets(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome','^genero']
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class MusicaList(views.APIView):
    def get(self, request):
        musica = Musica.objects.all()
        serializer = MusicaLightSerializer(musica,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = MusicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicaDetail(views.APIView):

    def get_objects(self, id):
        try:
            return Musica.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        musica = self.get_objects(id)
        serializer = MusicaSerializer(musica)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        musica = self.get_objects(id)
        serializer = MusicaSerializer(musica, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
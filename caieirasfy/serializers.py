from rest_framework import serializers

from artista.models import Artista
from artista.serializers import ArtistaLightSerializer
from caieirasfy.models import Musica



class MusicaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=50)
    tempo = serializers.IntegerField()
    artista = ArtistaLightSerializer(required=False)
    genero = serializers.CharField(max_length=255)

    def create(self, validated_data):
        artista_id = validated_data.pop('artista')
        artista = Artista.objects.get(id=artista_id['id'])
        musica = Musica.objects.create(artista=artista, **validated_data)

        return musica

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.tempo = validated_data.get('tempo')
        id_artista = validated_data.pop('artista')
        print(id_artista.get('id'))
        instance.artista = Artista.objects.get(id=id_artista['id'])
        instance.genero = validated_data.get('genero')
        instance.save()
        return instance

class MusicaLightSerializer(serializers.Serializer):
    nome = serializers.CharField()
    tempo = serializers.IntegerField()
    genero = serializers.CharField()
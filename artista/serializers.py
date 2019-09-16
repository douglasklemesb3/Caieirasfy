from rest_framework import serializers

from artista.models import Artista
from caieirasfy.models import Musica


class MusicaDTO(serializers.Serializer):
    nome = serializers.CharField()
    genero = serializers.CharField()


class ArtistaDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class ArtistaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    musica = MusicaDTO(many=True, read_only=True)
    estilo_musical = serializers.CharField()

    def create(self, validated_data):
        #musica_data = validated_data.pop('minhas musicas')
            #musica = Musica.objects.get(id=musica_data['id'])
        artista = Artista.objects.create(**validated_data)
        return artista

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.estilo = validated_data.get('estilo')
        musica_data = validated_data.pop('musica_favorita')
        musica = Musica.objects.get(id=musica_data['id'])
        instance.musica_favorita = musica
        instance.save()
        return instance

class ArtistaLightSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        nome = serializers.CharField(read_only=True)
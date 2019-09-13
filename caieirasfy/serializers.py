from rest_framework import serializers

from caieirasfy.models import Musica


class MusicaSerializer(serializers.Serializer):
    nome = serializers.CharField(
        max_length=50,
    )
    tempo = serializers.IntegerField()

    Artista =serializers.CharField(
        max_length=50,

    )

    genero_musical = serializers.CharField(
        max_length=255,
    )

    def create(self, validated_data):
        musica =  Musica.objects.create(**validated_data)
        return musica

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.tempo =validated_data.get('tempo')
        instance.artista = validated_data.get('artista')
        instance.genero_musical = validated_data.get('genero_musical')

class MusicaLinghtSerializer(serializers.Serializer):
    nome = serializers.CharField()
    genero_musical =serializers.CharField()
from rest_framework import serializers

from caieirasfy.models import Musica


class MusicaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=50)
    tempo = serializers.IntegerField()
    Artista =serializers.CharField(max_length=50)
    genero_musical = serializers.CharField(max_length=255)

    def create(self, validated_data):
        musica =  Musica.objects.create(**validated_data)
        return musica

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.tempo =validated_data.get('tempo')
        instance.artista = validated_data.get('artista')
        instance.genero_musical = validated_data.get('genero_musical')
        instance.save()
        return instance

class MusicaLinghtSerializer(serializers.Serializer):
    nome = serializers.CharField()
    tempo =serializers.IntegerField()
    genero_musical =serializers.CharField()
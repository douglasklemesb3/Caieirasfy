from rest_framework import serializers

from caieirasfy.models import Musica


class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields =('__all__')

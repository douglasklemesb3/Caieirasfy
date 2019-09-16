from django.db import models

# Create your models here.
from artista.models import Artista


class Musica(models.Model):
    nome = models.CharField(max_length=50)
    tempo = models.IntegerField()
    artista = models.ForeignKey(Artista, related_name='musica', on_delete=models.CASCADE)
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.nome + ' ' + self.Artista
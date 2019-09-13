from django.db import models

# Create your models here.

class Musica(models.Model):
    nome = models.CharField(max_length=50)
    tempo = models.IntegerField()
    # artista = models.ForeignKey(max_length=50)
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.nome + ' ' + self.Artista
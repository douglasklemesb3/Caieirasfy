from django.db import models

# Create your models here.

class Musica(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome da musica '
    )
    tempo =  models.IntegerField()
    Artista = models.CharField(
        max_length=50,
        verbose_name='Artista',
    )
    genero_musical = models.CharField(
        max_length=255,
        verbose_name='Genero musical',
        unique=True
    )
    link = models.CharField(
        max_length=255,
        verbose_name='link da musica',
    )

    def __str__(self):
        return self.nome + ' ' + self.Artista
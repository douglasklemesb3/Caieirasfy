from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(
        max_length=255,
    )

    idade = models.IntegerField()

    estilo_musical = models.CharField(
        max_length=255,
    )
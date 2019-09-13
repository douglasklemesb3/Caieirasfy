# Generated by Django 2.2.5 on 2019-09-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caieirasfy', '0004_musica_tempo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='Artista',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='genero_musical',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='link',
        ),
        migrations.AddField(
            model_name='musica',
            name='genero',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musica',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]

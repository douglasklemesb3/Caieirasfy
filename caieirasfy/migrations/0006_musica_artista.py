# Generated by Django 2.2.5 on 2019-09-16 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artista', '0001_initial'),
        ('caieirasfy', '0005_auto_20190913_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='artista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='musica', to='artista.Artista'),
            preserve_default=False,
        ),
    ]

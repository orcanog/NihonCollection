# Generated by Django 4.1.7 on 2023-10-05 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeInfos',
            fields=[
                ('titre', models.CharField(max_length=100)),
                ('image', models.URLField(default=None)),
                ('id_anime', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Favori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100)),
                ('id_anime_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Collection.animeinfos')),
            ],
        ),
    ]

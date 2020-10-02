# Generated by Django 3.1.2 on 2020-10-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='movie',
        ),
        migrations.AddField(
            model_name='character',
            name='movie',
            field=models.ManyToManyField(related_name='movies', to='movies.Movie'),
        ),
        migrations.RemoveField(
            model_name='detailmovie',
            name='planet',
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='planet',
            field=models.ManyToManyField(related_name='planets', to='movies.Planet'),
        ),
        migrations.RemoveField(
            model_name='detailmovie',
            name='producer',
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='producer',
            field=models.ManyToManyField(related_name='producers', to='movies.Producer'),
        ),
    ]
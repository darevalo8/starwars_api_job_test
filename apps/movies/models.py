from django.db import models


# Create your models here.

class Planet(models.Model):
    planet_name = models.CharField(max_length=50)

    def __str__(self):
        return self.planet_name


class Producer(models.Model):
    producer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.producer_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name


class MovieDetail(models.Model):
    text = models.TextField(max_length=200)
    planet = models.ManyToManyField(Planet, related_name="planets")
    director = models.CharField(max_length=50)
    producer = models.ManyToManyField(Producer, related_name="producers")
    release_date = models.DateField()
    movie = models.OneToOneField(Movie, related_name='detail', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie)


class Character(models.Model):
    character_name = models.CharField(max_length=50)
    movie = models.ManyToManyField(Movie, related_name="movies")

    def __str__(self):
        return self.character_name

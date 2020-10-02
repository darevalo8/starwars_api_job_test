from graphene_django import DjangoObjectType

from apps.movies.models import (Planet, Producer, Movie, MovieDetail, Character)


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = ("id", "planet_name")


class ProducerType(DjangoObjectType):
    class Meta:
        model = Producer
        fields = ("id", "producer_name")


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "movie_name")


class MovieDetailType(DjangoObjectType):
    class Meta:
        model = MovieDetail
        fields = ("id", "text", "planet", "director", "producer", "release_date", "movie")


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = ("id", "character_name", "movie")

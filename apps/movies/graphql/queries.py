import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from apps.movies.graphql.types import (PlanetType, ProducerType, MovieType,
                                       MovieDetailType, CharacterType)

from apps.movies.models import (Planet, Producer, Movie,
                                MovieDetail, Character)


class Query(graphene.ObjectType):
    all_characters = graphene.List(CharacterType)
    character_by_name = graphene.Field(CharacterType, name=graphene.String())
    all_planets = graphene.List(PlanetType)
    movie_detail = graphene.Field(MovieDetailType, id=graphene.Int())
    all_movies = graphene.List(MovieType)

    @staticmethod
    def resolve_all_characters(root, info):
        return Character.objects.prefetch_related("movie__movies").all()

    @staticmethod
    def resolve_all_planets(root, info):
        return Planet.objects.all()

    @staticmethod
    def resolve_all_movies(root, info):
        return Movie.objects.all()

    @staticmethod
    def resolve_movie_detail(root, info, id):
        id_movie = id

        if id_movie is not None:
            return MovieDetail.objects.get(movie_id=id_movie)

        return None

    @staticmethod
    def resolve_character_by_name(root, info, name):

        try:
            return Character.objects.prefetch_related("movie__movies").get(character_name__startswith=name)
        except Character.DoesNotExist:
            return None

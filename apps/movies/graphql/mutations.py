import graphene

from apps.movies.models import Planet, Movie, Character, MovieDetail, Producer
from apps.movies.graphql.types import PlanetType, MovieType, CharacterType, MovieDetailType


class CreatePlanetMutation(graphene.Mutation):
    class Arguments:
        planet_name = graphene.String()

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate(cls, root, info, planet_name, *args, **kwargs):
        planet = Planet.objects.create(planet_name=planet_name)

        return CreatePlanetMutation(planet=planet)


class CreateMovieMutation(graphene.Mutation):
    class Arguments:
        movie_name = graphene.String()

    movie = graphene.Field(MovieType)

    @classmethod
    def mutate(cls, root, info, movie_name, *args, **kwargs):
        movie = Movie.objects.create(movie_name=movie_name)

        return CreateMovieMutation(movie=movie)


class CreateCharacterMutation(graphene.Mutation):
    class Arguments:
        character_name = graphene.String()
        movies = graphene.List(graphene.Int)

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, character_name, movies, *args, **kwargs):
        movie = Movie.objects.filter(pk__in=movies)
        character = Character.objects.create(character_name=character_name)
        character.movie.set(movie)
        character.save()
        return CreateCharacterMutation(character=character)


class CreateCharacterMutation(graphene.Mutation):
    class Arguments:
        character_name = graphene.String()
        movies = graphene.List(graphene.Int)

    character = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, character_name, movies, *args, **kwargs):
        movie = Movie.objects.filter(pk__in=movies)
        character = Character.objects.create(character_name=character_name)
        character.movie.set(movie)
        character.save()
        return CreateCharacterMutation(character=character)


class CreateMovieDetailMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String()
        planets = graphene.List(graphene.Int)
        producers = graphene.List(graphene.Int)
        release_date = graphene.Date()
        director = graphene.String()
        movie = graphene.Int()

    movie_detail = graphene.Field(MovieDetailType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        movie = Movie.objects.get(pk=kwargs['movie'])
        planets = Planet.objects.filter(pk__in=kwargs['planets'])
        producers = Producer.objects.filter(pk__in=kwargs['producers'])
        movie_detail = MovieDetail.objects.create(
            text=kwargs['text'],
            release_date=kwargs['release_date'],
            director=kwargs['director'],
            movie=movie

        )
        movie_detail.producer.set(producers)
        movie_detail.planet.set(planets)
        movie_detail.save()
        return CreateMovieDetailMutation(movie_detail=movie_detail)

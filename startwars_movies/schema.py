from apps.movies.graphql.queries import Query
from apps.movies.graphql.mutations import (CreatePlanetMutation, CreateMovieMutation,
                                           CreateCharacterMutation, CreateMovieDetailMutation)

import graphene


class RootQuery(Query, graphene.ObjectType):
    pass


class RootMutation(graphene.ObjectType):
    create_planet = CreatePlanetMutation.Field()
    create_movie = CreateMovieMutation.Field()
    create_character = CreateCharacterMutation.Field()
    create_detail = CreateMovieDetailMutation.Field()


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)

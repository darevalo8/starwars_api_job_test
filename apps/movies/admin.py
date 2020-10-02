from django.contrib import admin
from apps.movies.models import (Planet, Producer, Movie, MovieDetail, Character)

# Register your models here.
admin.site.register(Planet)
admin.site.register(Producer)
admin.site.register(Movie)
admin.site.register(MovieDetail)
admin.site.register(Character)
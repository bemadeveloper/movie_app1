from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from afisha.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.db.models import Avg


@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=404)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def movie_reviews(request):
    movies = Movie.objects.prefetch_related('reviews')  # Используем обновленное имя связи обратного доступа
    serializer = MovieSerializer(movies, many=True)

    average_rating = Review.objects.aggregate(Avg('stars'))['stars__avg']

    data = {
        'movies': serializer.data,
        'average_rating': average_rating
    }

    return Response(data)

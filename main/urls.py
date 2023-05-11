from django.contrib import admin
from django.urls import path
from afisha.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_list),
    path('api/v1/directors/<int:id>/', director_detail),
    path('api/v1/movies/', movie_list),
    path('api/v1/movies/<int:id>/', movie_detail),
    path('api/v1/movies/reviews/', movie_reviews),
    path('api/v1/reviews/', review_list),
    path('api/v1/reviews/<int:id>/', review_detail),
]
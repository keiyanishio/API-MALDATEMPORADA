from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/animes/<int:anime_id>/', views.api_anime),
    path('api/animes/', views.api_anime_list)
]
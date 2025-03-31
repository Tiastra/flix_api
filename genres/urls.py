from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenresListCreateView.as_view(), name='genres-list'),
    path('genres/<int:pk>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
]

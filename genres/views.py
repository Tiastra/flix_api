import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class GenresListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Trocada por GenresListCreateView. Esse modelo de baixo é muito descritivo e pode ser simplificado
# @csrf_exempt
# def genres_view(request):
#     if  request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name},
#             status=201,
#         )


# Trocada por GenreRetrieveUpdateDestroyView. Esse modelo de baixo é muito descritivo e pode ser simplificado
# @csrf_exempt
# def genre_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     if  request.method == 'GET':
#         return JsonResponse({'id': genre.id, 'name': genre.name}, safe=False)

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name': genre.name}
#         )

#     elif request.method == 'DELETE':
#         genre_deleted = genre.name
#         genre.delete()
#         return JsonResponse(
#             {'message': f'Gênero {genre_deleted} excluído com sucesso!'},
#             status=204,
#         )

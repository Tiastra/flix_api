from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1950.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo deve ser menor que 200 caracteres.')
        return value

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return rate
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()

        # Foi substituido por um método mais simples
        # reviews = obj.reviews.all()
        # rate = 0
        # if reviews:
        #     for review in reviews:
        #         rate += review.stars
        #     return rate/len(reviews)
        # return None

# Serializer escrito à mão sem usar o ModelSerializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset=Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset=Actor.objects.all(),
#         many=True
#     )
#     resume = serializers.CharField()

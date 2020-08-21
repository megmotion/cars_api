from rest_framework import serializers
from .models import Car, Rating


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'average', 'rating_count')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'car', 'rate')

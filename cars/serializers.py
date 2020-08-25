from rest_framework import serializers
from rest_framework.response import Response
from .models import Car, Rating
import requests
import json


class CarSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'url', 'make', 'model', 'average', 'rating_count')

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    def create(self, validated_data):
        make = validated_data['make']
        model = validated_data['model']
        data = requests.get(
            f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json')
        cars = json.loads(data.text)
        added_car=Car.objects.filter(make=make, model=model)
        if not added_car:
            for item in cars['Results']:
                if model.lower() == item['Model_Name'].lower():
                    return Car.objects.create(**validated_data)
            else:
                raise serializers.ValidationError("There is no such car :D")
        else:
            raise serializers.ValidationError("This car already exists in database")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'car', 'rate')

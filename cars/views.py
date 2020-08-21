from django.shortcuts import render
from django.db.models import Count
from rest_framework import mixins, viewsets, views
from .models import Car, Rating
from .serializers import CarSerializer, RatingSerializer


class CarView(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer


class RatingView(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class PopularView(viewsets.ReadOnlyModelViewSet):
	popularity =  Car.objects.all().annotate(count=Count('rating')).order_by('-count').values_list('count', flat=True).distinct()
	queryset = Car.objects.all().annotate(count=Count('rating')).order_by('-count').filter(count__in=popularity[:3])
	serializer_class = CarSerializer

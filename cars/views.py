from django.shortcuts import render
from django.db.models import Count
from rest_framework import mixins, viewsets, views
from .models import Car, Rating
from .serializers import CarSerializer, RatingSerializer


class CarView(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer

	def get_serializer_context(self, *args, **kwargs):
		return {"request": self.request}

class RatingView(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class PopularView(viewsets.ReadOnlyModelViewSet):
	queryset = Car.objects.all().annotate(count=Count('rating')).order_by('-count')[:10]
	serializer_class = CarSerializer

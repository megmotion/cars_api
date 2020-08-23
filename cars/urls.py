from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('cars', views.CarView, 'cars')
router.register('popular', views.PopularView, 'popular')
router.register('rating', views.RatingView, 'rating')


urlpatterns = [
    path('', include((router.urls, 'cars')))
]

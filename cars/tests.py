from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from .models import Car
from . import views

class CarAPITestCase(APITestCase):
	def setUp(self):
		car=Car.objects.create(make='honda', model='Pilot')

	def test_car(self):
		car_count=Car.objects.count()
		self.assertEqual(car_count,1)

	def test_get_carlist(self):
		data={}
		url=api_reverse('cars:cars-list')
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_post_car(self):
		data={'make':'honda', 'model':'civic'}
		url=api_reverse('cars:cars-list')
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_post_invalid_car(self):
		data={'make':'honda', 'model':'xxxxxxx'}
		url=api_reverse('cars:cars-list')
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_get_car(self):
		car=Car.objects.first()
		data={}
		url=car.get_api_url()
		response = self.client.get(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_popular(self):
		data={}
		response = self.client.get('http://localhost:8000/popular/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
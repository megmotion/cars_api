from django.db import models
from django.db.models import Avg, Count


class Car(models.Model):
	make = models.CharField(max_length=50)
	model = models.CharField(max_length=50)

	@property
	def average(self):
		return Rating.objects.filter(car__id=self.id).aggregate(Avg('rate'))

	@property
	def rating_count(self):
		return Rating.objects.filter(car__id=self.id).count()

	def __str__(self):
		return self.make+'_'+self.model

class Rating(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    RATE_CHOICES = (
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
    )
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

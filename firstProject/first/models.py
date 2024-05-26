from django.db import models
from django.utils import timezone

# Create your models here.

class CarVariety(models.Model):
    CAR_TYPE = [
        ('HB','HATCHBACK'),
        ('SE','SEDAN'),
        ('X','XUV'),
        ('S','SUV'),
        ('PER','PERFORMANCE')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=100, choices=CAR_TYPE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
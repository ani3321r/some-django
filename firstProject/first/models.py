from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

class CarReview(models.Model):
    car = models.ForeignKey(CarVariety, on_delete=models.CASCADE, related_name='reviews')        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} reviewed {self.car.name} with a rating of {self.rating}'
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)    
    car_varities = models.ManyToManyField(CarVariety, related_name='stores')

    def __str__(self):
        return self.name
    
class CarCertificate(models.Model):
    car = models.OneToOneField(CarVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    validate_until = models.DateTimeField()

    def __str__(self):
        return f'{self.car.name} certificated with number {self.certificate_number}'
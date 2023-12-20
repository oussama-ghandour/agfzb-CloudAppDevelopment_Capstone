from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create a Car Make model 
class CarMake(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES = [
        ('SEDAN','sedan'),
        ('SUV', 'suv'),
        ('WAGON','wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    def __str__(self):
        return f"{self.car_make.name} - {self.name}"
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
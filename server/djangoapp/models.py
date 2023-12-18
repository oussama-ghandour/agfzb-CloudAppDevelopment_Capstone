from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create a Car Make model 
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


# Create a Car Model model 
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.CharField(max_length=80)
    CAR_TYPES = [
        ('SEDAN','sedan'),
        ('SUV', 'suv'),
        ('WAGON','wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    def __str__(self):
        return f"{self.car_make.name} - {self.name}"



# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

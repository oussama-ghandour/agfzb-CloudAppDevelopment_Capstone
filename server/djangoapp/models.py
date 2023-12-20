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



# Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name



# <HINT> Create a plain Python class `DealerReview` to hold review data

from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create a Car Make model 
class CarMake(models.Model):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return "Name: " + self.name

class CarModel(models.Model):
    
    # Porsche Models:
    PORSCHE_CAYENNE = "porsche_cayenne"
    PORSCHE_Panamera = "porsche_panamera"
    PORSCHE_Carrera = "porsche_carrera"

    # Chevrolet Models:
    CHEVROLET_TRAVERSE = "chevrolet_traverse"
    CHEVROLET_BLAZER = "chevrolet_blazer"

    # Mercedes Models:
    MERCEDES_CLS = "mercedes_cls"
    MERCEDES_MAYBACH = "mercedes_maybach"
    MERCEDES_CLASSE_G = "mercedes_classe_g"

    CAR_CHOICES = [
        ('PORSCHE_CAYENNE','Porsche Cayenne'),
        ('PORSCHE_PANAMERA', 'Porsche Panamera'),
        ('PORSCHE_CARRERA','Porsche Carrera'),
        ('CHEVROLET_TRAVERSE','Chevrolet Traverse'),
        ('CHEVROLET_BLAZER','Chevrolet Blazer'),
        ('MERCEDES_CLS','Mercedes Cls'),
        ('MERCEDES_MAYBACH','Mercedes Maybach'),
        ('MERCEDES_CLASSE_G','Mercedes Classe G'),
    ]
    # id = models.BigAutoField(primary_key=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)  
    car_type = models.CharField(
        null=False,
        max_length=20,
        choices=CAR_CHOICES,
        default=MERCEDES_CLASSE_G, 
    )
    year = models.DateField(default=now)


    def __str__(self):
        return "Name: " + self.name
    # type = models.CharField(max_length=10, choices=CAR_TYPES)
    # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    




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



# Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.id = id
        
    
    def __str__(self):
        return "Dealer Review: " + self.review


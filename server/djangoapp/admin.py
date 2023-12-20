from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name', 'dealer_id', 'type', 'year')

    # Override the save_model method to fetch dealer_id from Cloudant
    def save_model(self, request, obj, form, change):
        # Fetch dealer_id based on car_make and name 
        dealer_id = get_dealer_id_from_cloudant(obj.car_make.name, obj.name)
        obj.dealer_id = dealer_id
        obj.save()

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)



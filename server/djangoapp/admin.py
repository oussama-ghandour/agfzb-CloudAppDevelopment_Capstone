from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
   

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealer_id', 'car_type', 'year')
    list_filter = ['year']
    search_fields = ['name', 'car_type']


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)



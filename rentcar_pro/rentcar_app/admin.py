from django.contrib import admin
from .models import Car, Customer, CarRents

# Register your models here.
# admin.site.register(Car)
admin.site.register(Customer)


class CarRentsInline(admin.TabularInline):
    model = CarRents
    extra = 3

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year', 'price_for_day', 'car_class', 'is_rent', 'car_photo')
    inlines = (
        CarRentsInline,
    )
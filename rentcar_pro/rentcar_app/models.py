from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


CAR_CLASS = (
    (1,"A"),
    (2,"B"),
    (3,"C"),
    (4,"D"),
)

class Car(models.Model):
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_for_day = models.FloatField()
    car_class = models.IntegerField(choices=CAR_CLASS)
    is_rent = models.BooleanField(default=False)
    car_photo = models.FileField(null=True)
    rents = models.ManyToManyField("Customer", through="CarRents")

    def __str__(self):
        return "{} {}".format(self.mark, self.model)

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    city =models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_nr = models.CharField(max_length=50)
    flat_nr = models.CharField(max_length=50, null=True, blank = True)
    # rents = models.ManyToManyField(Car, through="CarRents")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)



class CarRents(models.Model):
    car = models.ForeignKey(Car)
    customer = models.ForeignKey(Customer)
    days = models.IntegerField()
    price_sum = models.FloatField()
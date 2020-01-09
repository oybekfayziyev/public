from django.db import models

# Create your models here.

class Vehicle(models.Model):
    vin = models.CharField(max_length=20,default='')
    year = models.IntegerField();
    make = models.CharField(max_length=10);
    model = models.CharField(max_length=20);
    typev = models.CharField(max_length=50);
    color = models.CharField(max_length=20);
    dimensions = models.TextField();
    weight = models.FloatField(max_length=40);

    def __str__(self):
        return self.vin;

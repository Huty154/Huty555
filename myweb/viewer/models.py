from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    order = models.IntegerField()
    title = models.CharField(max_length=500)
# models.py
from django.db import models

class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f'Rezervace od {self.start_date} do {self.end_date}'



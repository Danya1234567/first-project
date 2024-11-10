from django.db import models

# Create your models here.


class Technique(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/technique', blank=True, null=True)
    type=[('Cars', 'Cars'),('Motorcycles', 'Motorcycles'),('Flat', 'Flat'),('House', 'House')]
    type=models.CharField(max_length=200, choices=type)
    producer = models.CharField(max_length=200)
    cost = models.IntegerField()
    avaible=[('Not Avaible', 'Not Avaible'),('Avaible', 'Avaible')]
    avaible=models.CharField(max_length=15, choices=avaible)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
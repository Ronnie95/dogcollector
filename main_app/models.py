from django.db import models

# Create your models here.

class Dog(models.Model):

    breed = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    life_expectancy = models.CharField(max_length=250)

    def __str__(self):
        return self.breed

    class Meta:
        ordering = ['breed']

class Mix(models.Model):

    breed1 =models.CharField(max_length=250)
    breed2 =models.CharField(max_length=250)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="mix")

    def __str__(self):
            return self.breed1

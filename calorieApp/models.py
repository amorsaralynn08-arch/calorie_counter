from django.db import models

# Create your models here.
from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.food_name
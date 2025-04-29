from django.db import models

# Create your models here.

from django.db import models

class CalorieEntry(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.meal} - {self.calories} cal on {self.date}"

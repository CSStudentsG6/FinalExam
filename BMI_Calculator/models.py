from django.db import models

#uses info from the database for past interactions and results
class BMIRecord(models.Model):
    
    date = models.DateTimeField(auto_now_add=True) #gets the date and time from the __init__.py provided by the django install
    
    bmi = models.FloatField()# gets the previously entered bmi calculation for the past results
    
    def __str__(self):
        return f"{self.date}: {self.bmi}"
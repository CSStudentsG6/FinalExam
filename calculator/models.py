from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone






class ExerciseCalculation(models.Model):
    WEIGHT_UNITS = [
        ('kg', 'Kilograms'),
        ('lbs', 'Pounds'),
    ]
    
    mets = models.FloatField(validators=[MinValueValidator(0.1)])
    weight_value = models.FloatField(validators=[MinValueValidator(1)])
    weight_unit = models.CharField(max_length=3, choices=WEIGHT_UNITS, default='kg')
    target_calories = models.FloatField(validators=[MinValueValidator(1)])
    
  
    calories_per_min = models.FloatField(editable=False)
    required_minutes = models.FloatField(editable=False)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # most users using lbs.. convert lbs to kg for formula convenience!!
        if self.weight_unit == 'lbs':
            weight_kg = self.weight_value * 0.453592
        else:
            weight_kg = self.weight_value  # Already in kg
            
        # calories per minute
        self.calories_per_min = (self.mets * 3.5 * weight_kg) / 200
        
        # and the exercise duration (how long to exercise to burn the calorie integer)
        self.required_minutes = self.target_calories / self.calories_per_min
        
        super().save(*args, **kwargs)

    def get_duration_display(self):
        """Returns formatted duration string"""
        minutes = self.required_minutes
        hours = int(minutes // 60)
        remaining_minutes = int(round(minutes % 60))
        
        if hours > 0:
            return f"{hours} hour{'s' if hours > 1 else ''} {remaining_minutes} minute{'s' if remaining_minutes != 1 else ''}"
        return f"{remaining_minutes} minute{'s' if remaining_minutes != 1 else ''}"

    def __str__(self):
        return f"{self.target_calories} kcal @ {self.mets} METS"
from django.shortcuts import render
from .models import BMIRecord
from datetime import datetime

#function that calculates bmi based on whether you want to use imperial or metric units
def calculate_bmi(request):
    
    bmi = None #sets variable to nothing 
    
    history = BMIRecord.objects.all().order_by('-date')[:5]  # Fetch last 5 results

    if request.method == "POST":
        try:
            unit = request.POST.get("unit")
            weight = float(request.POST.get("weight"))
            height = float(request.POST.get("height"))
            #does the conversion if imperial units are requested 
            if unit == "imperial":
                weight *= 0.453592  # Convert lbs to kg
                height *= 0.0254    # Convert inches to meters
            
            if height > 0: #if height is a positive value, the calculation will be completed
                bmi = round(weight / (height ** 2), 2)
                BMIRecord.objects.create(date=datetime.now(), bmi=bmi)  # Save result with date and time entered
        #exception handling
        except (ValueError, TypeError):
            bmi = "Invalid input"
    
    return render(request, 'BMI_Calculator/bmi_calculator.html', {'bmi': bmi, 'history': history})

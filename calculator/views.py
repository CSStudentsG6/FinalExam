from django.shortcuts import render, redirect
from .models import ExerciseCalculation



def exercise_calculator(request):
    if request.method == 'POST':
        
        mets = float(request.POST.get('mets'))
        weight_value = float(request.POST.get('weight_value'))
        weight_unit = request.POST.get('weight_unit')
        target_calories = float(request.POST.get('target_calories'))
        
       
        calculation = ExerciseCalculation(
            mets=mets,
            weight_value=weight_value,
            weight_unit=weight_unit,
            target_calories=target_calories
        )
        calculation.save()
        
        return render(request, 'result.html', {
            'calculation': calculation,
            'converted_weight': calculation.weight_value * 0.453592 if weight_unit == 'lbs' else calculation.weight_value
        })
    
    return render(request, 'input.html')
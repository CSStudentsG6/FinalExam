from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.exercise_calculator, name='calculator'),
    # Add more URL patterns as needed
]
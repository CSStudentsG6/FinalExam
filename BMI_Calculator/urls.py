from django.urls import path
from . import views
from .views import calculate_bmi

urlpatterns = [
    path('bmi/', calculate_bmi, name='calculate_bmi'),
]
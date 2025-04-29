from django.urls import path, include
from .views import base, result


urlpatterns = [
    path('', base, name='base'),
    path('result/', result, name='result'),

    
    
]

#http://127.0.0.1:8000/
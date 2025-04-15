# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='restaurant_home'),
    path('start_over/', views.start_over, name='start_over'),
    path('choose_budget/', views.choose_budget, name='choose_budget'),
    path('choose_category/', views.choose_category, name='choose_category'),
    path('show_restaurants/', views.show_restaurants, name='show_restaurants'),
    path('eliminate_or_new_round/', views.eliminate_or_new_round, name='eliminate_or_new_round'),
    path('final_choice/', views.final_choice, name='final_choice'),
]



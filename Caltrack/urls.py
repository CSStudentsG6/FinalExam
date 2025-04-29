from django.urls import path
from . import views

app_name = 'caltrack'  # <- THIS LINE is important! It defines the namespace.

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_entry, name='add_entry'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('progress/', views.progress_report, name='progress_report'),
    path('calendar/', views.calendar_view, name='calendar_view'),
]

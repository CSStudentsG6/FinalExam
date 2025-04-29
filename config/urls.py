from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('myapp.urls')),  # This includes URLs for myapp
    path('restaurant/', include('myapp.restaurant.urls')),  # This includes URLs for the restaurant app
    path('calculator/', include('calculator.urls')),  # Connects your calculator app's URLs
    path('bmi/', include('BMI_Calculator.urls')),  # Includes URLs for BMI_Calculator app
    path('Caltrack/', include('Caltrack.urls')),  # Calorie Tracker app URLs
    path('blog/', include('blog.urls')),  # ✅ Added line to include blog URLs
]






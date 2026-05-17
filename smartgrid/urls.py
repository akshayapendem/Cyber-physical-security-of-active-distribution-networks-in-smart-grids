from django.contrib import admin
from django.urls import path, include
from adn_operations import views as adn_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', adn_views.register, name='register'),
    path('adn/', include('adn_operations.urls')),
    path('device/', include('device_security.urls')),
    path('standards/', include('communication_standards.urls')),
    path('drivers/', include('application_drivers.urls')),
    path('industry/', include('industry_solutions.urls')),
    path('research/', include('research_outcomes.urls')),
    path('', include('adn_operations.urls')),  # Default route
]

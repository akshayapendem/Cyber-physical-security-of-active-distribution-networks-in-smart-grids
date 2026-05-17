from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='adn_operations_index'),
    path('upload/', views.upload_dataset, name='upload_dataset'),
]

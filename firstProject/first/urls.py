from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_cars, name='all_cars'),
]
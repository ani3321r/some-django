from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_cars, name='all_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
]
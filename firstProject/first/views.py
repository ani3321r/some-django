from django.shortcuts import render
from .models import CarVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_cars(request):
    cars = CarVariety.objects.all()
    return render(request, 'first/all_first.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(CarVariety, pk=car_id)
    return render(request, 'first/car_detail.html', {'car':car})

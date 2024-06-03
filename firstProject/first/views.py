from django.shortcuts import render
from .models import CarVariety, Store
from django.shortcuts import get_object_or_404
from .forms import CarVarietyForm

# Create your views here.
def all_cars(request):
    cars = CarVariety.objects.all()
    return render(request, 'first/all_first.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(CarVariety, pk=car_id)
    return render(request, 'first/car_detail.html', {'car':car})

def car_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = CarVarietyForm(request.POST)
        if form.is_valid():
            car_variety = form.cleaned_data['car_variety']
            Store.objects.filter(car_varities = car_variety)
    else:
        form = CarVarietyForm()
    return render(request, 'first/car_stores.html',{'stores': stores, 'form': form})    
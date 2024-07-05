from django.shortcuts import render
from .models import Xapp
from .forms import XForms
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def X_list(request):
    Xss = Xapp.objects.all().order_by('-created_at')
    return render(request, 'X_list.html', {'Xss': Xss})

def X_create(request):
    if request.method == 'POST':
        form = XForms(request.POST, request.FILES)
        if form.is_valid():
            X = form.save(commit=False)
            X.user = request.user
            X.save()
            return redirect('X_list')
    else:
        form = XForms()
    return render(request, 'X_form.html', {'form': form}) 

def X_edit(request, X_id):
    X = get_object_or_404(Xapp, pk=X_id, user = request.user)
    if request.method == 'POST':
        form = XForms(request.POST, request.FILES, instance=X)
        if form.is_valid():
            X = form.save(commit=False)
            X.user = request.user
            X.save()
            return redirect('X_list')
    else:
        form = XForms(instance=X)
    return render(request, 'X_form.html', {'form': form})    

def X_delete(request, X_id):
    X = get_object_or_404(Xapp, pk=X_id, user = request.user)
    if request.method == 'POST':
        X.delete()
        return redirect('X_list')
    return render(request, 'X_confirm_delete.html', {'X': X}) 
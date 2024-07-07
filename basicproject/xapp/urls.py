from django.urls import path
from . import views

urlpatterns = [
    path("", views.X_list, name='X_list'),
    path("create/", views.X_create, name='X_create'),
    path("<int:X_id>/edit/", views.X_edit, name='X_edit'),
    path("<int:X_id>/delete/", views.X_delete, name='X_delete'),
]
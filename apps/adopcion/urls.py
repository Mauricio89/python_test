from django.urls import path

#from apps.mascota.views import index
from . import views

urlpatterns = [
    path('', views.index_adopcion, name='adopcion'), #index = nombre mas largo
]
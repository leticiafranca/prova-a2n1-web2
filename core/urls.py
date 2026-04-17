from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo_evento/', views.novo_evento, name='novo'),
]
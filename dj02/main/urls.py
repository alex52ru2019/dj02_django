from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('animals/', views.animals, name='animals'),
    path('personal/', views.personal, name='personal')
]

from django.contrib import  admin
from django.urls import path
from  . import views

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('randomfacts/' , views.randomfacts, name ='randomfacts'),
    path('students/', views.students, name ='students'),
    path('bored/', views.bored, name = 'bored'),
    
]

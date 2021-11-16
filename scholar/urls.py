from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    
    path('', include('scientificjournal.urls')),
    path('about/', views.about),
    path('contact/', views.contact), 
    path('latestPapers/', views.latestPapers),
    path('', include('account.urls')),
    path('', views.registration),
]

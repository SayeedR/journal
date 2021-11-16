from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('journal_Policies/', views.journalPolicies),
    path('reviewers/', views.reviewers),
    path('editors/', views.editors),
    path('privacyPolicy/', views.editors),
     
     
]
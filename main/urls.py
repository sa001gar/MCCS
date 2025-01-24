from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('faculty/', views.faculty, name='faculty'),
    path('team/', views.team, name='team'),
    path('alumni/', views.alumni, name='alumni'),
    path('gallery/', views.gallery, name='gallery'),
    path('feedback/', views.feedback, name='feedback'),

]
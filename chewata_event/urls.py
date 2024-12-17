from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='chewata-home'),
    path('about/', views.about, name='chewata-about'),
    path('schedule/', views.schedule, name='chewata-schedule'),
    path('contact/', views.contact, name='chewata-contact')
]

from django.contrib import admin
from django.urls import path, include

from AboutUsApp import views

urlpatterns = [
    path('About/', views.AboutUsAppMethod, name='About')
]

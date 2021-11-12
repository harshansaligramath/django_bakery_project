from django.contrib import admin
from django.urls import path, include

from ContactUsApp import views

urlpatterns = [
    path('Contact/', views.ContactUsAppMethod, name='Contact'),

]

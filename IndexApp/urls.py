from django.contrib import admin
from django.urls import path, include

from IndexApp import views

urlpatterns = [
    path('', views.IndexAppMethod, name='Index'),
    path('About/', include('AboutUsApp.urls'), name='About'),
    path('Contact/', include('ContactUsApp.urls'), name='Contact'),

]

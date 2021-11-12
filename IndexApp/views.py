from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from IndexApp.models import Destination

def IndexAppMethod(request):

    dest1=Destination.objects.all()
    return render(request, 'index.html',{"dest1":dest1})




from django.shortcuts import render

# Create your views here.
def AboutUsAppMethod(request):
    return render(request,'about.html')

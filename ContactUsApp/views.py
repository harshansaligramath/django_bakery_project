from django.shortcuts import render


# Create your views here.
def ContactUsAppMethod(request):
    return render(request, 'Contact.html')

from django.shortcuts import render


def base(request):
    return render(request, 'home.html')
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})


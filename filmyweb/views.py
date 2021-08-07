from django.shortcuts import render
from django.http import HttpResponse

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    return render(request, 'filmy.html')


from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def testtest(request):
    return HttpResponse("<h3><i><b>ТЕСТОВАЯ строка</b></i></h3>")


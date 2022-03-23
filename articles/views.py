from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    html_string = """ <h1>Halo</h1> """
    return HttpResponse(html_string)

def showId(request, id):
    print(id)
    return HttpResponseRedirect(reverse('index'))
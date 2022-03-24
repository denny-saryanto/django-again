from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article

# Create your views here.
def index(request):
    html_string = """ <h1>Halo</h1> """
    return HttpResponse(html_string)

def showId(request, id):
    article_id = Article.objects.get(id=id)
    return HttpResponse(""" <center> <h1> {} </h1> <p> {} </p> </center>""".format(article_id.title, article_id.content))
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article
from djangomid import views as viewsDjangomid

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(viewsDjangomid.index))

def showId(request, id=None):
    try:
        article_id = Article.objects.get(id=id)
        context = {
            'article' : article_id,
        }
        return render(request, "articles/index.html", context=context)
    except Exception:
        return HttpResponseRedirect(reverse(viewsDjangomid.index))

def searchArticle(request):
    query = request.GET
    query_data = query.get('query')

    try:
        query_data = int(query_data)
    except:
        query_data = None

    article, context = None, None
    if query_data is not None:
        try:
            article = Article.objects.get(id=query_data)
            context = {
                'result' : {
                    'id' : article.id,
                    'title' : article.title,
                    'content' : article.content,
                } 
            }
        except Exception as e:
            context = {
                'result' : {
                    'id' : "Not Found",
                    'title' : "Not Found",
                    'content' : "Not Found",
                } 
            }
    return render(request, 'articles/search.html', context=context)
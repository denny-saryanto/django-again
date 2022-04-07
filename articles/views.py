from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm
from djangomid import views as viewsDjangomid
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(viewsDjangomid.index))

def showId(request, slug=None):
    try:
        article_slug = Article.objects.get(slug=slug)
        context = {
            'article' : article_slug,
        }
        return render(request, "articles/index.html", context=context)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    except Article.MultipleObjectsReturned:
        article_slug = Article.objects.filter(slug=slug).order_by('id').first()
    except Exception:
        return HttpResponseRedirect(reverse(viewsDjangomid.index))

def searchArticle(request):
    query_data = request.GET.get('query')
    article = Article.objects.search(query=query_data)
    context = {
        'result' : article,
    }
    return render(request, 'articles/search.html', context=context)

@login_required
def inputArticle(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form
    }
    # Form Manual Handle

    # if request.method == "POST":
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article_object = Article.objects.create(title=title, content=content)
    #     context['object'] = article_object
    #     context['created'] = True

    # Django Form Handle 
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm(request.POST or None)
        # Tanpa Django Form
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/create.html', context=context)
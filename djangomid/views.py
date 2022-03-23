from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

def index(request):
    article_obj = Article.objects.get(id=1)
    article_all = Article.objects.all()

    context = {
        "arr_app" : article_all,
        "id" : article_obj.id,
        "title" : article_obj.title,
        "content" : article_obj.content,
    }

    html = render_to_string("djangomid/index.html", context=context)

    return HttpResponse(html)
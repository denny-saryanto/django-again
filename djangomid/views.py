from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

def index(request):
    article_obj = Article.objects.get(id=1)
    arr = [1, 4, 5, 12, 61, 2]
    arr_app = ""

    # for x in enumerate(arr):
    #     # arr_app += """<li> index {} data {} </li>""".format(x, arr[x])
    #     arr_app += """ <li> index {} data {} </li>""".format(x[0], x[1])

    context = {
        "arr_app" : arr,
        "id" : article_obj.id,
        "title" : article_obj.title,
        "content" : article_obj.content,
    }

    html = render_to_string("djangomid/index.html", context=context)

    return HttpResponse(html)
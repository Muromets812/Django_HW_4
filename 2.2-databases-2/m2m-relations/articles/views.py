from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article = Article.objects.all().order_by(ordering)
    context = {'object_list': article,
               }

    return render(request, template, context)

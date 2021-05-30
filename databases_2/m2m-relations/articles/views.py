from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Topic, Scopes


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    a = Article.objects.all().order_by(ordering).prefetch_related('scopes')
    context = {'object_list': a}

    # a = Article.objects.first().scopes.first().is_main
    # print(a)
    # s = Scope.objects.first()
    # iii = Scope_Article.objects.get(article=a, scope=s)
    #
    # print(iii)


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)

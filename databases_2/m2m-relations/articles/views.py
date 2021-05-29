from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, Scope_Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    a = Article.objects.all().order_by(ordering).prefetch_related('scopes')
    context = {'object_list': a}

    for aa in a:
        print(aa.scopes.all())

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)

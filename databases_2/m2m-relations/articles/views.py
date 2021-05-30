from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Topic, Scopes


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    a = Article.objects.all().order_by(ordering).prefetch_related('scopes')
    context = {'object_list': a}

    return render(request, template, context)

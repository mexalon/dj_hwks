from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    sorts = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}

    phones = Phone.objects.all().order_by(sorts.get(sort, 'name'))
    context = {'items': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'item': phone}
    return render(request, template, context)


def home_view(request):
    return redirect(reverse('catalog'))

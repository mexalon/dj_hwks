from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Phone

SORT_TYPE = ['name']
CURRENT_P = [1]


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort', SORT_TYPE[0])
    SORT_TYPE[0] = sort  # чтобы сохранялся вид сортировки при пагинации

    sorts = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}

    phones = Phone.objects.all().order_by(sorts.get(sort, 'name'))

    current_page = request.GET.get('page', CURRENT_P[0])
    CURRENT_P[0] = current_page  # чтобы сохранялась страница при сортировке
    items_per_page = 5

    pagi = Paginator(phones, items_per_page)
    the_page = pagi.page(current_page)

    if the_page.has_next():
        next_page_num = the_page.next_page_number()
    else:
        next_page_num = int(current_page)

    if the_page.has_previous():
        prev_page_num = the_page.previous_page_number()
    else:
        prev_page_num = int(current_page)

    next_params = urlencode({'page': next_page_num})
    prev_params = urlencode({'page': prev_page_num})

    next_page_url = reverse('catalog') + "?" + next_params
    prev_page_url = reverse('catalog') + "?" + prev_params

    context = {'items': the_page,
               'current_page': current_page,
               'prev_page_url': prev_page_url,
               'next_page_url': next_page_url,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()

    context = {'item': phone}

    return render(request, template, context)


def home_view(request):
    return redirect(reverse('catalog'))

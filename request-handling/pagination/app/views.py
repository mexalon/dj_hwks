from urllib.parse import urlencode

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

import csv

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='1251') as csvf:
        reader = csv.DictReader(csvf)
        DATA = [{'Name': raw['Name'], 'Street': raw['Street'], 'District': raw['District']} for raw in reader]

    default_page_num = 1
    current_page = request.GET.get('page', default_page_num)
    items_per_page = 10
    my_first_pagi = Paginator(DATA, items_per_page)
    the_page = my_first_pagi.page(current_page)

    next_page_num = the_page.next_page_number()
    prev_page_num = max([default_page_num, next_page_num - 2])

    next_params = urlencode({'page': next_page_num})
    prev_params = urlencode({'page': prev_page_num})

    next_page_url = reverse('bus_stations') + "?" + next_params  # как то не уверен насчёт +"?", как иначе его добавить?
    prev_page_url = reverse('bus_stations') + "?" + prev_params

    return render(request, 'index.html', context={
        'bus_stations': the_page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


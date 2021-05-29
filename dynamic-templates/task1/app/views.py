from django.conf import settings
from django.shortcuts import render
import csv


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def color_it(val: str):
    color = rgb2hex(255, 255, 255)
    try:
        f = float(val)
        if f < 0:
            color = rgb2hex(0, 128, 0)
        if f > 1:
            red = 255 - (min([round(f), 6])) * 20
            color = rgb2hex(red, 0, 0)
    except Exception:
        pass

    return color


def inflation_view(request):
    template_name = 'my_content.html'
    with open(settings.INFL_CSV, encoding='utf8') as csvf:
        reader = csv.reader(csvf, delimiter=';')
        data = [row for row in reader]

    body_ = []  # добавление полей цвета и раскраска
    for row in data:
        dataline = [{'value': item, 'color': None} for item in row]
        body_ += [dataline]

    for row in body_[1:]:
        row[-1]['color'] = rgb2hex(169, 169, 169)
        for item in row[1:-1]:
            item['color'] = color_it(item['value'])

    c = {'data': body_}

    return render(request, template_name, context=c)

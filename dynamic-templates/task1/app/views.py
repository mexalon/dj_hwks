from django.conf import settings
from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    print(settings.INFL_CSV)
    with open(settings.INFL_CSV, encoding='utf8') as csvf:
        reader = csv.DictReader(csvf, delimiter=';')
        DATA = [row for row in reader]
        header_ = list(DATA[0].keys())
        body_ = [[int(list(row.values())[0])] + [float(item) for item in list(row.values())[1:]] for row in DATA]


    # чтение csv-файла и заполнение контекста
    context = {}

    return render(request, template_name,
                  context)

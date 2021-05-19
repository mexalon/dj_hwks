from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
from django.urls import reverse

LAND_CHOICE = {'original': 'landing.html', 'test': 'landing_alternate.html'}
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_page = request.GET.get('from-landing', None)
    if from_page:
        counter_show[from_page] += 1
        counter_click['all'] += 1

    #чтобы было проще тестить
    pages = {
        'Перейти на original': 'landing/?ab-test-arg=original',
        'Перейти на test': 'landing/?ab-test-arg=test',
        'Посмотреть статистику': reverse('stats')
    }
    context = {
        'pages': pages
    }
    return render(request, 'index.html', context)

def landing(request):
    the_choice = request.GET.get('ab-test-arg')
    the_landing = LAND_CHOICE.get(the_choice, 'original')
    return render(request, the_landing)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': round(counter_show['test']/counter_click['all'], 2),
        'original_conversion': round(counter_show['original']/counter_click['all'], 2),
    })

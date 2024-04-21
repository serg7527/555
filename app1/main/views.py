from django.http import HttpResponse
from django.shortcuts import render
#from django.template import context
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()
    context: dict = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Самый нужный текст на этом сайте'
    }

    return render(request, 'main/about.html', context)



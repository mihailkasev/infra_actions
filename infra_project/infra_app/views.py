from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Ура, наконец!')


def second_pages(request):
    return HttpResponse('А это вторая страница. Да.')

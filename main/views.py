from django.shortcuts import render, Http404
from django.http import HttpResponse
import datetime
data = datetime.datetime.now()
from main.models import Films,Review

def index_views(request):
    return render(request, 'index.html')


def data_now(request):
    return HttpResponse(data)

def main(requests):
    return HttpResponse('Hello World')


def films(request):
    queryset = Films.objects.all()
    context = {
        'films_list': queryset
    }
    return render(request, 'films.html', context=context)

def films_detail(request,id):
    detail = Films.objects.get(id=id)

    context = {
        'films_detail': detail,
        'review':Review.objects.filter(film_id=id)
    }
    return render(request, 'film_detail.html', context=context)



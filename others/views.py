from django.http import Http404
from django.shortcuts import render
from .models import Others


def all(request):
    auction = Others.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'others/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Others.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'others/single.html'
        return render(request, template, context)
    except:
        raise Http404

from django.http import Http404
from django.shortcuts import render
from .models import Eoi


def all(request):
    eoi = Eoi.objects.order_by('-published_date')
    context = {'eoi': eoi}
    template = 'eoi/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Eoi.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'eoi/single.html'
        return render(request, template, context)

    except:
        raise Http404

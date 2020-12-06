from django.http import Http404
from django.shortcuts import render
from .models import Quotation


def all(request):
    auction = Quotation.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'quotation/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Quotation.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'quotation/single.html'
        return render(request, template, context)

    except:
        raise Http404

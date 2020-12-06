from django.http import Http404
from django.shortcuts import render
from .models import Auction


def all(request):
    auction = Auction.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'auction/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Auction.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'auction/single.html'
        return render(request, template, context)

    except:
        raise Http404

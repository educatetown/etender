from django.http import Http404
from django.shortcuts import render
from .models import StandingList


def all(request):
    auction = StandingList.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'standinglist/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = StandingList.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'standinglist/single.html'
        return render(request, template, context)

    except:
        raise Http404

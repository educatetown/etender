from django.http import Http404
from django.shortcuts import render
from .models import Proposal


def all(request):
    auction = Proposal.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'proposal/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Proposal.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'proposal/single.html'
        return render(request, template, context)

    except:
        raise Http404

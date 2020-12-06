from django.http import Http404
from django.shortcuts import render
from .models import Intents2Awards


def all(request):
    auction = Intents2Awards.objects.order_by('-published_date')
    context = {'auction': auction}
    template = 'intent2awards/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        auction = Intents2Awards.objects.get(slug=slug)

        context = {'tender': auction}
        template = 'intent2awards/single.html'
        return render(request, template, context)

    except:
        raise Http404

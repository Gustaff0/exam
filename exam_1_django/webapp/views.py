from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Hotel
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def hotel_list(request):
    lists = Hotel.objects.all()
    return render(request, 'lists.html', context={'lists': lists})


def hotel_view(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
    except Modern.DoesNotExist:
        raise Http404
    return render(request, 'hotel_view.html', context={'hotel': hotel})
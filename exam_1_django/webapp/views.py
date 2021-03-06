from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Hotel
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def hotel_list(request):
    lists = Hotel.objects.all()
    return render(request, 'lists.html', context={'lists': lists})


def hotel_create_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'create.html')
    elif request.method == "POST":
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        text = request.POST.get("text")

        hotel = Hotel.objects.create(
            name=name,
            mail=mail,
            text=text
        )

    return redirect('home')
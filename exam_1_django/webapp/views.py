from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Hotel
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.core.exceptions import ObjectDoesNotExist
from webapp.forms import RegForm

# Create your views here.

def hotel_list(request):
    if request.GET.get('search'):
        lists = Hotel.objects.filter(name=request.GET.get('search')).order_by('-time_start')
        return render(request, 'lists.html', context={'lists': lists})
    else:
        lists = Hotel.objects.filter(status='active').order_by('-time_start')
        return render(request, 'lists.html', context={'lists': lists})


def hotel_create_view(request, *args, **kwargs):
    if request.method == "GET":
        form = RegForm()
        return render(request, 'create.html', context = {'form': form})
    elif request.method == "POST":
        form = RegForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            mail = request.POST.get("mail")
            text = request.POST.get("text")

            Hotel.objects.create(
                name=name,
                mail=mail,
                text=text
            )
            return redirect('home')
        else:
            return render(request, 'create.html', context={'form': form})


def hotel_edit_view(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'GET':
        form = RegForm(initial={
            'name': hotel.name,
            'mail': hotel.mail,
            'text': hotel.text
        })
        return render(request, 'edit.html', context={'form': form, 'hotel': hotel})
    elif request.method == 'POST':
        form = RegForm(data=request.POST)
        if form.is_valid():
            hotel.name = form.cleaned_data['name']
            hotel.mail = form.cleaned_data['mail']
            hotel.text = form.cleaned_data['text']
            hotel.save()
            return redirect('home')
        else:
            return render(request, 'edit.html', context={'form': form, 'hotel': hotel})


def hotel_delete_view(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'hotel': hotel})
    elif request.method == 'POST':
        hotel.delete()
        return redirect('home')

def reg_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,
                  'result_search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
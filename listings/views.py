from django.shortcuts import render, redirect
from listings import models, forms, filters

# Create your views here.
def index(request):
    return render(request, 'listings/index.html')

def listings(request):
    list = models.Listings.objects.order_by('-list_date')
    myFilter = filters.ListingFilter(request.GET, queryset = list)
    list = myFilter.qs
    context = {
        'listings': list,
        'myFilter': myFilter
    }
    return render(request, 'listings/list.html', context)

def new(request):
    if request.method != 'POST':
        form = forms.FormList()
    else:
        form = forms.FormList(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/mylisting/')

    context = {
        'form': form
    }
    return render(request, 'listings/new.html', context)

def detail(request, pk):
    detail = models.Listings.objects.get(pk=pk)
    context = {
        'detail': detail
    }
    return render(request, 'listings/detail.html', context)

def mylist(request):
    list = request.user.listings_set.order_by('-list_date')
    context = {
        'list': list
    }
    return render(request, 'listings/mylist.html', context)

def editList(request, pk):
    listing = models.Listings.objects.get(pk=pk)
    if request.method != 'POST':
        form = forms.FormList(instance=listing)
    else:
        form = forms.FormList(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/mylisting/')
    context = {
        'listing': listing,
        'form': form
    }
    return render(request, 'listings/edit_list.html', context)


def deleteList(request, pk):
    listing = models.Listings.objects.get(pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('/mylisting/')
    context = {
        'listing': listing
    }
    return render(request, 'listings/confirm.html', context)
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import priceChoices, bedroomChoices, stateChoices

def index(request):
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render (request, 'listings/listing.html', context)

def search(request):
    querysetList = Listing.objects.order_by('-listDate')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querysetList = querysetList.filter(description__icontains=keywords)

    # City 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querysetList = querysetList.filter(city__iexact=city)

    # State 
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querysetList = querysetList.filter(state__iexact=state)
    
    # Bedrooms 
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querysetList = querysetList.filter(bedrooms__iexact=bedrooms)

    # Price 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querysetList = querysetList.filter(price__lte=price)

    context = {
        'stateChoices': stateChoices,
        'priceChoices': priceChoices,
        'bedroomChoices': bedroomChoices,
        'listings': querysetList,
        'values': request.GET
    }

    return render (request, 'listings/search.html', context)
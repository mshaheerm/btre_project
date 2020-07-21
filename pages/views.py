from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import priceChoices, bedroomChoices, stateChoices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)[:3]
    context = {
        'listings': listings,
        'stateChoices': stateChoices,
        'priceChoices': priceChoices,
        'bedroomChoices': bedroomChoices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hireDate')

    # Get MVP realtor/realtors
    mvpRealtors = Realtor.objects.all().filter(isMVP=True)

    context = {
        'realtors': realtors,
        'mvpRealtors': mvpRealtors
    }
    return render(request, 'pages/about.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        print('Hello')
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


    contact = Contact(listing=listing, listingID=listing_id, name=name, email=email, phone=phone, message=message, userID=user_id)

    contact.save()

    messages.success(request, 'Thank you for submitting your request. We will get back to you soon !')

    return redirect('/listings/' + listing_id)



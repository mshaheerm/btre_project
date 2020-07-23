from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

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

    #   Check if user has made inquiry already.
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(listingID=listing_id, userID=user_id)
        if has_contacted:
            messages.error(request, 'You have already made an inquiry for this listing!')
            return redirect('/listings/' + listing_id)

    contact = Contact(listing=listing, listingID=listing_id, name=name, email=email, phone=phone, message=message, userID=user_id)

    contact.save()

    # send email
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for "' + listing + '". Sign into admin panel for more info',
        'msmuser4@gmail.com',
        [realtor_email, 'mshaheermunir@gmail.com'],
        fail_silently=False
    )

    messages.success(request, 'Thank you for submitting your request. We will get back to you soon !')

    return redirect('/listings/' + listing_id)



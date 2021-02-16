from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail 
from .models import Contacts 



def contacts(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
       
        if request.user.is_authenticated:
            user_id = request.user_id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made in inquiry for this listing')
                return redirect('/listings/'+listing_id)
 

        contacts = Contacts(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contacts.save()


        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + '. Sign into the admin panel for more info',
            'mukhamed.dzhanbekov@mail.ru'
        )

        messages.success(request, 'your request has been submitted, a realtor get back to you soon')
        return redirect('/listings/'+listing_id)





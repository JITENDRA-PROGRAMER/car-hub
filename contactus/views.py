import django
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contactus
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contactus.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'you have already made an inquiry about this car. Please wait we get back to you.')
                return redirect('/cars/'+car_id)

        contactus = Contactus(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                              last_name=last_name, customer_need=customer_need, city=city, state=state, phone=phone,
                              email=email, message=message)

        admin_info = User.objects.filter(is_superuser=True)
        admin_emails = []
        for i in admin_info:
            admin_emails.append(i.email)
        send_mail(
                'New Car Inquiry',
                'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
                'jsah4501@gmail.com',
                admin_emails,
                fail_silently=False,
            )
 
        ## Email Sandind
        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email
 
        # send_mail(
        #     'New Car Inquiry',
        #     'You have a new inquiry for the car' +car_title+ '. Please login to your admin pannel for more info.',
        #     'jsah4501@gmail.com', 
        #     [admin_email],
        #     fail_silently=False, 
        # )

        contactus.save()
        messages.success(
            request, 'Your request has been submited, we will get back to you shortly')
        return redirect('/cars/'+car_id)


from django.contrib import messages
from django.shortcuts import render,redirect

from pages.models import Team
# from .models import *
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.

# Home page function


def Home(request):
    teams = Team.objects.all()
    feature_car = Car.objects.order_by('-created_date').filter(is_feature=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'feature_car': feature_car,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def About(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def Servecs(request):
    return render(request, 'pages/servec.html')


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message for carzone website regrading ' + subject
        message_body = 'Name:-' + name  + ', Email:-' + email + ', Phone-:' + phone +  ', Message:' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'jsah4501@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submited, we will get back to you shortly')
        return redirect('contact')
    return render(request, 'pages/contact.html')

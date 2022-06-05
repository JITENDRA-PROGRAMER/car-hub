from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contactus.models import Contactus
from django.contrib.auth.decorators import login_required
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now loged in ')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invilade login cerdintials ')
            return redirect('login')
    else:  
        return render(request, 'accounts/login.html')


def Register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname'] 
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Register sucessfully ')
                    return redirect('login')


        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else: 
        return render(request, 'accounts/register.html')

@login_required(login_url='login')
def Dashbord(request):
    user_inquiry = Contactus.objects.order_by('-create_date').filter(user_id=request.user.id)
    data ={
        'inquiries':user_inquiry,
    }
    return render(request, 'accounts/dashboard.html',data)


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'you are sucessfuly log out')
        return redirect('home')

    return redirect('home')
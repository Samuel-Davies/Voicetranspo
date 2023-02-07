from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'account/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            print('logged in')
            return redirect('account:dashboard')
        else: 
            messages.info(request, 'invalid credentials')
            print('back to page')
            return redirect('account:login')
    else:
        return render(request, 'account/Login.html')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken')
                return redirect('account:signup')

            elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('account:signup')
            else:
                 user = User.objects.create_user(username=username, password = password1, email=email, 
                 first_name = first_name, last_name = last_name)

                 user.save()
                 print('user created')
                 return redirect('account:login')
            
        else:
               
                messages.info(request,'Password not matching')
                return redirect('account:signup')
            
    else:
        return render(request, 'account/SignUp.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('account:index')


def about_us(request):
    return render(request, 'account/About-Us.html')


def how_it_works(request):
    return render(request, 'account/How-It-Works.html')

def dashboard(request):
    return render(request, 'account/dashboard.html') 
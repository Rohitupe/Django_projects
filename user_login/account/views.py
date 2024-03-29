from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username is Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email is Taken')
                return redirect('register')
            else:
                data = User.objects.create_user(first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password1)
                data.save()
                return redirect('login')
        else:
            messages.warning(request,'password is not maching')
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'invalid data')
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
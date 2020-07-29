from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from . forms import RegisterForm
from django.contrib import messages
from .models import User,Customer

# Create your views here.

def register(request):
    form = RegisterForm(request.POST, request.FILES)
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password=request.POST['password']
        confirm_password = request.POST['confirm_pasword']

        if User.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('username taken')</script>")
            #messages.info(request,'username-taken')
        elif User.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('email taken')</script>")
            #messages.info(request, 'email-taken')
        elif User.objects.filter(mobile=mobile).exists():
            return HttpResponse("<script>alert('mobile num taken')</script>")
            #messages.info(request, 'mobile-taken')
        elif confirm_password != password:
            return HttpResponse("<script>alert('password doesnot matched')</script>")

        else:
            user=User.objects.create_user(username=username,password=password,email=email,mobile=mobile)
            user.save();
            messages.info(request, 'user-created')

            if form.is_valid():
                form.save()
                redirect('/login')
            else:
                form = RegisterForm()


        return redirect('/login')
    return render(request,'register_form.html',{'form':form,})



def login(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = auth.authenticate(username=phone_number, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponse('wrong username / password')
            messages.info(request, 'invalid credentials')
    else:
        return render(request,'login_form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request,name):
    customer = Customer.objects.filter(username=name)

    return render(request,"profile.html",{'customer':customer})

def home(request):
    return render(request,"home.html")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from nandatemple.models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def homepage(request):
    return render(request, 'nandatemple/homepage.html')

def registration(request):
    if request.method == 'POST':
        frist_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        address = request.POST.get('address')
        gender = request.POST.get('inlineRadioOptions_gender')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        total_person = request.POST.get('total_persons')
        email = request.POST.get('email')
        modeldata = Registration(frist_name=frist_name, last_name=last_name,mother_name=mother_name,father_name=father_name,
                                 address=address,gender=gender,state=state,city=city,pincode=pincode,total_person=total_person,email=email)
        modeldata.save()
        messages.success(request, "Thank you for the registration!")
        return redirect('registration')
    return render(request, 'nandatemple/registration.html')

def index(request):
    return render(request, 'registration/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('useremail')
        password = request.POST.get('password')
        rpassword = request.POST.get('rpassword')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('signin')
    return render(request, 'registration/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            firstname = user.first_name
            return render(request, 'nandatemple/homepage.html', {'firstname':firstname})
        else:
            messages.error(request, "Bad Creadentials")
            return redirect('signin')
    return render(request, 'registration/signin.html')

def signout(request):
    # return render(request, 'registration/signup.html')
    logout(request)
    messages.success(request, "Logged out Successfully!!")
    return redirect('index')

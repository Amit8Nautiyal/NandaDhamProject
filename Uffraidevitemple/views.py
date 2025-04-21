from django.shortcuts import render, redirect
from Uffraidevitemple.models import UfrainRegistration
from django.contrib import messages

# Create your views here.
def uffraintemple(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        dob = request.POST['birthDate']
        phone_no = request.POST['phoneNumber']
        hight = request.POST['height']
        weight = request.POST['weight']
        gender = request.POST['gender']
        print("First name =========================================================================", first_name)
        modeldata = UfrainRegistration(first_name=first_name, last_name=last_name, email=email, dob=dob, phone_no=phone_no, hight=hight,
                                       weight=weight, gender=gender)
        modeldata.save()
        messages.success(request, "Thank you for the registration!")
        return redirect('uffraintemple')
    return render(request, 'ufraintemple/uffrainhome.html')

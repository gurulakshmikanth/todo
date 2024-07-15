from django.shortcuts import render,redirect
from users.forms import *
from django.contrib import messages

# Create your views here.

def registration(request):
    registrationform=CustomerForm()
    d={'registrationform':registrationform}
    if request.method=='POST':
        registrationform=CustomerForm(request.POST)
        if registrationform.is_valid():
            registrationform.save()
            messages.success(request,("New User Acoount Created, Login To Get Started"))
            return redirect('registration')
    return render(request,'registrations.html',d)
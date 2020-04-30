from django.shortcuts import render, redirect
from Webapp.forms import MessageForm, OrderForm, UserForm, UserProfileInfoForm, ContactForm
from django.core.mail import send_mail #email settings
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def mainpage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            # send an email that something has been sent to the database
            from_email = settings.EMAIL_HOST_USER # the Domain email
            firstname = form.cleaned_data['first_name']
            message = form.cleaned_data['message']
            recipient_list = ['denohpakni@yahoo.com']

            send_mail(firstname,message,from_email,recipient_list,fail_silently=True)
            return redirect('Webapp:thanks')
    else:
        form = MessageForm()
    return render(request,'index.html',{'form':form})

def thanks(request):
    return render(request,'thanks.html')


#### Login manenos ##

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainpage'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return redirect('Webapp:userinfo')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mainpage'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request,'registration/invalid_login.html')
    else:
        return render(request,'login.html',{})


@login_required(login_url='/user_login/')
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # send email
            from_email = settings.EMAIL_HOST_USER # the Domain email
            Client = form.cleaned_data['Client']
            Analyis_Required = form.cleaned_data['Analyis_Required']
            recipient_list = ['denohpakni@yahoo.com']

            send_mail(Client,Analyis_Required,from_email,recipient_list,fail_silently=True)
            return redirect('Webapp:thanks')
    else:
        form = OrderForm()
    return render(request,'order.html',{'form':form})

# Custom error pages
def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

@login_required(login_url='/user_login/')
def userinfo(request):
    if request.method == 'POST':
        form = UserProfileInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainpage'))  

    form = UserProfileInfoForm()
    return render(request,'update_info.html',{'form':form})



####################################################
########## A Simple but Complex Form ###############
####################################################
def sbcform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'sbcform.html', {'form': form})
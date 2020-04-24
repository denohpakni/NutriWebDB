from django.shortcuts import render, redirect
from Webapp.forms import MessageForm, OrderForm
from django.core.mail import send_mail
from django.conf import settings

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
            return redirect(emailSuccess)
    else:
        form = MessageForm()
    return render(request,'index.html',{'form':form})

def emailSuccess(request):
    return render(request,'thanks.html')

# Creating the Order form for the client that will also be saved in the DB and send an emaail notification
def order(request):
    if request.method == 'POST':
        orderform = OrderForm(request.POST)

        if orderform.is_valid():
            orderform.save()
            # send email
            from_email = settings.EMAIL_HOST_USER # the Domain email
            Client = orderform.cleaned_data['Client']
            Analyis_Required = orderform.cleaned_data['Analyis_Required']
            recipient_list = ['denohpakni@yahoo.com']

            send_mail(Client,Analyis_Required,from_email,recipient_list,fail_silently=True)
            return redirect(emailSuccess)
    else:
        orderform = OrderForm()
    return render(request,'order.html',{'orderform':orderform})
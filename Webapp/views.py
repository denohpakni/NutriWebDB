from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail #email settings
from django.conf import settings

from Webapp.forms import MessageForm
from Webapp.models import Message


# Create your views here.
def emailSuccess(request):
    return render(request,'thanks.html')

def mainpage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            # send an email that something has been sent to the database
            from_email = settings.EMAIL_HOST_USER # the Domain email
            firstname = form.cleaned_data['first_name']
            message = form.cleaned_data['message']
            recipient_list = ['mosendirits@gmail.com']

            send_mail(firstname,message,from_email,recipient_list,fail_silently=True)
            return redirect('Webapp:thanks')
    else:
        form = MessageForm()
    return render(request,'index.html',{'form':form})


# Custom error pages
def handler404(request, *args, **argv):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)

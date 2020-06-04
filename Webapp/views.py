from django.shortcuts import render, redirect
from Webapp.forms import MessageForm, OrderForm, UserForm, UserProfileInfoForm
from django.contrib.auth.forms import UserCreationForm
from Webapp.models import Order, UserProfileInfo,FoodSafetyService, FoodNutritionService,OthersService,TraininService
from django.core.mail import send_mail #email settings
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from shopping_cart.models import OrderServices, OrderServicesNutrition, OrderServicesOthers,OrderServicesTraining


# Create your views here.
def mainpage(request):
    food_nutrition_services = FoodNutritionService.objects.all()
    food_safety_services = FoodSafetyService.objects.all()
    others_services = OthersService.objects.all()
    training_services= TraininService.objects.all()
    current_order_safety = []
    current_order_nutrition = []
    current_order_others = []
    current_order_trainin = []
    if request.user.is_authenticated:
        filtered_safety_services = OrderServices.objects.filter(owner=request.user.profile, is_ordered=False)
        filtered_nutrition_services = OrderServicesNutrition.objects.filter(owner= request.user.profile, is_ordered=False)
        print(filtered_safety_services)
        print(filtered_nutrition_services)
        filtered_others_services = OrderServicesOthers.objects.filter(owner=request.user.profile, is_ordered=False)
        filtered_training_services = OrderServicesTraining.objects.filter(owner=request.user.profile, is_ordered=False)
        
        if filtered_safety_services.exists():
            user_order = filtered_safety_services[0]
            user_order_items = user_order.items.all()
            current_order_safety = [service.service for service in user_order_items]


        if filtered_nutrition_services.exists():
            user_order = filtered_nutrition_services[0]
            user_order_items = user_order.items.all()
            current_order_nutrition = [service.service for service in user_order_items]

        if filtered_others_services.exists():
            user_order = filtered_others_services[0]
            user_order_items = user_order.items.all()
            current_order_others = [service.service for service in user_order_items]

        if filtered_training_services.exists():
            user_order = filtered_training_services[0]
            user_order_items = user_order.items.all()
            current_order_trainin = [service.service for service in user_order_items]
    

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
    
    

    context = {'form':form,'food_nutrition_services':food_nutrition_services,
    'food_safety_services':food_safety_services,'others_services':others_services,
    'training_services':training_services,'current_order_safety': current_order_safety,
    'current_order_nutrition': current_order_nutrition,'current_order_others': current_order_others
    ,'current_order_trainin': current_order_trainin}
    return render(request,'index.html',context)

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


@transaction.atomic
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = UserProfileInfoForm(request.POST)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            registered = True
            return redirect('Webapp:userinfo')
        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileInfoForm()
    return render(request,'signup.html',
                          {'user_form':user_form,
                           'registered':registered,
                           'profile_form': profile_form})

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
    form = OrderForm
    if request.user.is_authenticated:
        form = OrderForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                order = form.save(commit=False)
                order.Client = request.user
                order.save()
                # send email
                from_email = settings.EMAIL_HOST_USER # the Domain email            
                Analyis_Required = form.cleaned_data['Analyis_Required']
                Remarks = form.cleaned_data['Remarks']
                recipient_list = ['denohpakni@yahoo.com']

                send_mail(Analyis_Required,Remarks,from_email,recipient_list,fail_silently=True)
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
    myinfo = UserProfileInfo
    myorder = Order
    context = {'myinfo':myinfo,'myorder':myorder}
    return render(request,'userinfo.html',context)

# The DB frontend display page
@login_required(login_url='/user_login/')
def dbfront(request):
    all_objects = Order.objects.all()
    context= {'all_objects': all_objects}
    return render(request,'dbfront.html',context)



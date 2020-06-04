from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Webapp.models import Profile
from Webapp.forms import MessageForm
from Webapp.models import FoodSafetyService, FoodNutritionService,OthersService,TraininService
from shopping_cart.models import OrderServices, FoodSafetyItem
from django.urls import reverse


@login_required()
def add_to_cart (request, **kwargs):
    food_nutrition_services = FoodNutritionService.objects.all()
    filtered_nutrition_services = OrderServices.objects.filter(owner=request.user.profile, is_ordered=False)
    user_profile = get_object_or_404(Profile, user=request.user)

    
    food_safety_services = FoodSafetyService.objects.all()
    others_services = OthersService.objects.all()
    training_services= TraininService.objects.all()
    form = MessageForm()
    service = FoodSafetyService.objects.filter(id=kwargs.get('item_id',"")).first()
    if service in request.user.profile.services.all():
        messages.info(request, "You already added this service")
    #create a foodsafety item of the selected service
    foodsafety_item, status = FoodSafetyItem.objects.get_or_create(service=service)

   # print(foodsafety_item, status)

    #create order associated with the user

    user_order, status = OrderServices.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(foodsafety_item)

    if status:
        user_order.ref_code= 'REF001'
        user_order.save()

    context = {'form':form,'food_nutrition_services':food_nutrition_services,
    'food_safety_services':food_safety_services,'others_services':others_services,
    'training_services':training_services}
    return redirect(reverse('mainpage'))

    #return render(request,'index.html',context)

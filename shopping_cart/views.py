from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Webapp.models import Profile
from Webapp.forms import MessageForm
from Webapp.models import FoodSafetyService, FoodNutritionService,OthersService,TraininService
from shopping_cart.models import OrderServices, FoodSafetyItem, FoodNutritionItem, OthersItem, TrainingItem, OrderServicesNutrition, OrderServicesOthers, OrderServicesTraining
from django.urls import reverse


@login_required()
def add_to_cart (request, **kwargs):
    food_nutrition_services = FoodNutritionService.objects.all()
    food_safety_services = FoodSafetyService.objects.all()
    others_services = OthersService.objects.all()
    training_services= TraininService.objects.all()
    #filtered_nutrition_services = OrderServices.objects.filter(owner=request.user.profile, is_ordered=False)
    user_profile = get_object_or_404(Profile, user=request.user)

    form = MessageForm()
    safetyService = FoodSafetyService.objects.filter(id=kwargs.get('item_id',"")).first()
    nutritionService = FoodNutritionService.objects.filter(id=kwargs.get('item_id',"")).first()

    othersService = OthersService.objects.filter(id=kwargs.get('item_id',"")).first()
    traininService = TraininService.objects.filter(id=kwargs.get('item_id',"")).first()
    if safetyService in request.user.profile.services.all():
        messages.info(request, "You already added this service")

    if nutritionService in request.user.profile.services.all():
        messages.info(request, "You already added this service")

    if othersService in request.user.profile.services.all():
        messages.info(request, "You already added this service")

    if traininService in request.user.profile.services.all():
        messages.info(request, "You already added this service")
        
    #create a foodsafety item of the selected service
    safety_item, status = FoodSafetyItem.objects.get_or_create(service=safetyService)
    nutrition_item, status = FoodNutritionItem.objects.get_or_create(service=nutritionService)
    others_item, status = OthersItem.objects.get_or_create(service=othersService)
    trainin_item, status = TrainingItem.objects.get_or_create(service=traininService)

   

    #create order associated with the user

    safety_order, status = OrderServices.objects.get_or_create(owner=user_profile, is_ordered=False)
    nutrition_order, status = OrderServicesNutrition.objects.get_or_create(owner=user_profile, is_ordered=False)
    others_order, status = OrderServicesOthers.objects.get_or_create(owner=user_profile, is_ordered=False)
    trainin_order, status = OrderServicesTraining.objects.get_or_create(owner=user_profile, is_ordered=False)

    safety_order.items.add(safety_item)
    nutrition_order.items.add(nutrition_item)
    others_order.items.add(others_item)
    trainin_order.items.add(trainin_item)

    # if status:
    #     safety_order.ref_code= 'REF001'
    #     safety_order.save()
    #     nutrition_order.ref_code='REF001'
    #     nutrition_order.save()

    context = {'form':form,'food_nutrition_services':food_nutrition_services,
    'food_safety_services':food_safety_services,'others_services':others_services,
    'training_services':training_services}
    return redirect(reverse('mainpage'))

    #return render(request,'index.html',context)

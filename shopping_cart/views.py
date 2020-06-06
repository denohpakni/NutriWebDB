from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Webapp.models import Profile
from Webapp.forms import MessageForm
from Webapp.models import Services
from shopping_cart.models import OrderServices, ServiceItem
from django.urls import reverse


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = OrderServices.objects.filter(owner = user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required(login_url='/user_login/')
def add_to_cart (request, **kwargs):
    services = Services.objects.all()
    #filtered_services = OrderServices.objects.filter(owner=request.user.profile, is_ordered=False)
    user_profile = get_object_or_404(Profile, user=request.user)

    form = MessageForm()
    service = Services.objects.filter(id=kwargs.get('item_id',"")).first()
    if service in request.user.profile.services.all():
        messages.info(request, "You already added this service")
   
    service_item, status = ServiceItem.objects.get_or_create(service=service)


    user_order, status = OrderServices.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(service_item)

    if status:
        user_order.ref_code= 'REF001'
        user_order.save()

    context = {'form':form,'services':services}
    return redirect(reverse('mainpage'))

@login_required(login_url='/user_login/')
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)

@login_required(login_url='/user_login/')
def delete_from_cart(request, item_id):
    item_to_delete = ServiceItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))

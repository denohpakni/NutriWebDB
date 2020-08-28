from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Webapp.models import Profile
from Webapp.forms import MessageForm
from Webapp.models import Services
from shopping_cart.models import OrderServices, ServiceItem
from django.urls import reverse
from django.http import HttpResponse
from Webapp.models import Services
import csv, datetime
from django.utils.crypto import get_random_string


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
   
    service_item, status = ServiceItem.objects.get_or_create(service=service, owner=user_profile, is_ordered=False)


    user_order, status = OrderServices.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(service_item)

    if status:
        code = "NT_" + get_random_string(4)+ str(datetime.datetime.now().time())[0:2]
        user_order.ref_code= code
        user_order.save()

    context = {'form':form,'services':services}
    return redirect(reverse('Webapp:order'))

@login_required(login_url='/user_login/')
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)

@login_required(login_url='/user_login/')
def delete_from_cart(request, item_id):
    user_profile = get_object_or_404(Profile, user=request.user)
    item_to_delete = ServiceItem.objects.filter(pk=item_id, owner=user_profile)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))

@login_required(login_url = '/user_login/')
def update_item_number(request, **kwargs):
    item_id = kwargs.get('item_id', "10")
    item_number = kwargs.get('item_number', "10")
    item_to_update = get_object_or_404(ServiceItem, pk=item_id)
    item_to_update.number_of_samples= item_number
    item_to_update.save(update_fields=["number_of_samples"])
    return redirect(reverse('shopping_cart:order_summary')) 


@login_required(login_url = '/user_login/')
def export(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = OrderServices.objects.filter(owner = user_profile, is_ordered=False)

    response=  HttpResponse(content_type='text/csv')
    len_items = len(order.values_list('items__service__description'))
    our_array = ['Service Name','Number of Samples']
    for i in range(1,len_items+1):
        our_array.append('SampleNames#'+str(i))
    writer = csv.writer(response)
    writer.writerow(our_array)

    #order_object = order._meta_get_field('items__number_of_samples')

    for my_order in order.values_list('items__service__description','items__number_of_samples'):
        #ourTuple = tuple()
        #for value in  range (1,my_order[1]+1):
            #ourTuple = ourTuple + ('sample' + str(value),)

        writer.writerow(my_order  ) #+ ourTuple) 
    
    file_name= order.values_list('ref_code')[0][0]

    response['Content-Disposition'] = 'attachment; filename=' + file_name + '.csv'
    
    return response




    
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import AddProductModel, PlaceOrderModel
from accounts.forms import AddProductForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_staff == 1:
                return redirect('admin-dashboard')
            else:
                return redirect('user-dashboard')

        else:
            messages.info(request, 'invalid credentials')
            print('invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, "register.html")

@login_required
def adminDashboard(request):
    allUserDetails = User.objects.all()
    orderDetail = PlaceOrderModel.objects.all()
    context = {'orderDetail': orderDetail, 'allUserDetails': allUserDetails}
    return render(request, 'admin-dashboard.html', context)

@login_required
def userDashboard(request):
    return render(request, 'user-dashboard.html')

@login_required
def showUserDetail(request, id):
    userDetail = User.objects.get(pk=id)
    return render(request, "user-profile-order.html", {'userDetail': userDetail})

@login_required
def delete(request, id):
    deleteProduct = AddProductModel.objects.get(pk=id)
    deleteProduct.delete()
    return redirect("show-product-details")

@login_required
def addProduct(request):
    return render(request, 'add-product.html')

@login_required
def saveProduct(request):
    if request.method == 'POST':
        if request.POST.get('product_name') and request.POST.get('product_quantity') and request.POST.get(
                'product_price'):
            addProductModel = AddProductModel()
            addProductModel.product_name = request.POST['product_name']
            addProductModel.product_description = request.POST['product_description']
            addProductModel.product_price = request.POST['product_price']
            addProductModel.product_quantity = request.POST['product_quantity']

            addProductModel.save()
            return redirect('show-product-details')

@login_required
def showProductDetails(request):
    dests = AddProductModel.objects.all()
    return render(request, 'show-product-details.html', {'dests': dests})

@login_required
def showAvailableProd(request):
    dests = AddProductModel.objects.all()
    return render(request, 'show-available-products.html', {'dests': dests})

@login_required
def add(request):
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-product-details')

    context = {'form': form}
    return render(request, 'add.html', context)

@login_required
def update(request, pk):
    add = AddProductModel.objects.get(id=pk)
    form = AddProductForm(instance=add)
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=add)
        if form.is_valid():
            form.save()
            return redirect('show-product-details')

    context = {'form': form}
    return render(request, 'add.html', context)

@login_required
def placeOrder(request, id):
    username = request.user
    productDetail = AddProductModel.objects.get(pk=id)
    context = {'productDetail': productDetail, 'username': username}
    if request.method == 'POST':
        if request.POST.get('product_quantity'):
            orderModel = PlaceOrderModel()
            orderModel.product_name = request.POST['product_name']
            orderModel.product_description = request.POST['product_description']
            orderModel.product_price = request.POST['product_price']
            orderModel.order_by = request.POST['order_by']
            orderModel.product_quantity = request.POST['product_quantity']
            orderModel.product_status = request.POST['product_status']

            orderModel.save()
            return redirect('user-dashboard')
    return render(request, 'place-order.html', context)



def showOrderHistory(request):
    username = request.user
    orderDetail = PlaceOrderModel.objects.filter(order_by=username)
    print(orderDetail)
    context = {'orderDetail': orderDetail}

    return render(request, 'order-history.html', context)


def updateStatus(request):
    username = request.user
    PlaceOrderModel.objects.filter(order_by=username).filter(product_status='Ordered').update(product_status='Completed')
    return HttpResponse("Status Updated")

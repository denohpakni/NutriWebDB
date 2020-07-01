from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin-dashboard', views.adminDashboard, name='admin-dashboard'),
    path('user-dashboard', views.userDashboard, name='user-dashboard'),
    path('show-product-details', views.showProductDetails, name='show-product-details'),
    path('add-product', views.addProduct, name='add-product'),
    path('save-product', views.saveProduct, name='save-product'),
    path('show-user/<id>', views.showUserDetail, name='show-user'),
    path('delete/<id>', views.delete, name='delete'),
    path('add', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('place-order/<int:id>', views.placeOrder, name='place-order'),
    path('show-product', views.showAvailableProd, name='show-product'),
    path('order-history', views.showOrderHistory, name='order-history'),
    path('update-status', views.updateStatus, name='update-status'),
]

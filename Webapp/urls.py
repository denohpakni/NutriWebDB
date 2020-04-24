from django.urls import path
from Webapp import views


urlpatterns = [
    path('thanks/',views.emailSuccess,name='thanks'),
    path('order/',views.order,name='order'),
]
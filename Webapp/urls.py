from django.urls import path
from Webapp import views

# SET THE NAMESPACE!
app_name = 'Webapp'

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('thanks/',views.emailSuccess,name='thanks'),
]
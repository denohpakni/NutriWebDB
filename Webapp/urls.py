from django.urls import path
from Webapp import views

# SET THE NAMESPACE!
app_name = 'Webapp'

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/',views.register,name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('special/',views.special,name='special'),
    path('thanks/',views.emailSuccess,name='thanks'),
    path('order/',views.order,name='order'),
]
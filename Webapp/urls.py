from django.urls import path
from Webapp import views

# SET THE NAMESPACE!
app_name = 'Webapp'

urlpatterns = [
    path('order/',views.order,name='order'),
    path('user_login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('thanks/',views.thanks,name='thanks'),
    path('userinfo/',views.userinfo,name='userinfo'),
    path('sbc/',views.sbcform,name='sbcform'),
]
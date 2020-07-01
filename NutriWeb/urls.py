
from django.contrib import admin
from django.urls import path, include
from Webapp import views

handler404 = 'Webapp.views.handler404'
handler500 = 'Webapp.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

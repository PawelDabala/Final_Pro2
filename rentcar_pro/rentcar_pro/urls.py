"""rentcar_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rentcar_app.views import (
    CarsView,
    CarView,
    UpdateCarView,
    AddCarView,

    CustomersView,
    CustomerView,
    UpdateCustomerView,
    AddCustomerView,

    HwLoginView,
    HwLogoutView,

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^detal_car/(?P<id>\d+)', CarView.as_view()),
    url(r'^cars', CarsView.as_view(), name='cars'),
    url(r'^update_car/(?P<id>\d+)', UpdateCarView.as_view()),
    url(r'^add_car', AddCarView.as_view(),),

    #Customers
    url(r'^customers', CustomersView.as_view(), name='customers'),
    url(r'^detal_customer/(?P<id>\d+)', CustomerView.as_view()),
    url(r'^update_customer/(?P<id>\d+)', UpdateCustomerView.as_view()),
    url(r'^add_customer', AddCustomerView.as_view(),),
    
    #LOGIN
    url(r'^hwlogin/$', HwLoginView.as_view(), name='hwlogin'),
    url(r'^hwlogout/$', HwLogoutView.as_view(), name='hwlogout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
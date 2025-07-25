"""
URL configuration for webbanhang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views as hv
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hv.home,name='home'),
    path('about/', hv.about,name='about'),
    path('order/', hv.order,name='order'),
    path('contact/', hv.contact,name='contact'),
    path('menu/', hv.menu,name='menu'),
    path('cart/', hv.cart, name='cart'),
    path('register/',hv.register,name='register'),
    path('login/', hv.user_login, name='login'),
    path('logout/', hv.user_logout, name='logout'),
    #cart sản phẩm
    path('cart/add/<int:id>/', hv.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', hv.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         hv.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         hv.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', hv.cart_clear, name='cart_clear'),
    path('cart/',hv.cart_detail,name='cart_detail'),
    path('cart/checkout/',hv.checkout,name='checkout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name="index"),
   # path('add',views.add,name="add"),
    path('menu.html',views.menu,name="menu"),
    path('about.html',views.about,name="about"),
    path('cart.html',views.cart,name="cart"),
   
]
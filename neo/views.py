from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
#from .models import Pizza
from .models import * 
from django import template

register = template.Library()

def index(request):
    pizzas=Pizza.objects.all()
    ctx={'pizzas':pizzas}
    pizza=request.POST.get('pizza')
    cart=request.session.get('cart')
    if cart:
        quantity=cart.get(pizza)
        if quantity:
            cart[pizza]=quantity+1
        else:
            cart[pizza]=1
    else:
        cart={}
        cart[pizza]=1
    if 'null' in cart:
        del cart['null']
    print(cart)
    request.session['cart']=cart

    return render(request,'index.html',ctx)

def menu(request):
    
    return render(request,'menu.html')
def about(request):
    
    return render(request,'about.html')
def style(request):
    return render(request,'style.css')

@register.filter(name='is_in_cart')
def is_in_cart(pizza  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == pizza.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(pizza  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == pizza.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(pizza , cart):
    return pizza.priceM * cart_quantity(pizza , cart)


@register.filter(name='total_cart_price')
def total_cart_price(pizza , cart):
    sum = 0 
    for p in pizza:
        sum += price_total(p , cart)

    return sum
    
def cart(request):
   
    ids = list(request.session.get('cart').keys())
    pizza = Pizza.get_products_by_id(ids)
    print(pizza)
    cart=request.session.get('cart')
    quantity=[]
    for i in pizza:
       quantity.append(cart_quantity(i,cart))
    total=total_cart_price(pizza,cart)
    print(total)
    #myzip=zip(pizza,quantity)
    content={'pizza':pizza,'total':total}
    #for a,b in myzip:
     #   print(a.name)
      #  print(a,b)
    #return render(request , 'cart.html' , {'products' : products} )
    return render(request,'cart.html',content)

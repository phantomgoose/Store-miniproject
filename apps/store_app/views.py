# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from ..helper_functions import admin_required, login_required
from .models import Product
import json

class StoreIndex(View):
    def get(self, request):
        products = Product.objects.all()
        cart = {}
        if 'user_id' in request.session.keys():
            cart = request.session['cart']
        context = {
            'products': products,
            'cart': cart,
        }
        return render(request, 'store_app/store_index.html', context)

    #creates a new entry in the store
    @method_decorator(admin_required)
    def post(self, request):
        server_response = {
            'product_created': False,
        }
        Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=float(request.POST['price']))
        server_response['product_created'] = True
        return HttpResponse(json.dumps(server_response))

class StoreRemove(View):
    @method_decorator(admin_required)
    def get(self, request, product_id):
        server_response = {
            'product_removed': False,
        }
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            server_response['product_removed'] = True
        except ObjectDoesNotExist:
            print 'Product does not exist'
        return HttpResponse(json.dumps(server_response))

class CartUpdate(View):
    @method_decorator(login_required)
    def post(self, request):
        server_response = {
            'cart_updated': False,
            'server_message': 'An error has occured while updating the cart'
        }
        #validation
        if all(k in request.POST.keys() for k in ('product_id', 'amount')):
            try:
                product = Product.objects.get(id=request.POST['product_id'])
            except:
                server_response['server_message'] = "Target product doesn't exist"
                return HttpResponse(json.dumps(server_response))
            product_id = str(product.id)
            try:
                product_amount = int(request.POST['amount'])
            except:
                server_response['server_message'] = 'Invalid amount entered'
                return HttpResponse(json.dumps(server_response))
            if product_amount < 1:
                server_response['server_message'] = 'Invalid amount entered'
                return HttpResponse(json.dumps(server_response))
            cart = request.session['cart']
            if product_id in cart.keys():
                cart[product_id] = int(cart[product_id]) + int(product_amount)
            else:
                cart[product_id] = product_amount
            request.session.modified = True
            server_response['cart_updated'] = True
            server_response['server_message'] = 'Cart updated!'
        return HttpResponse(json.dumps(server_response))

class CartShow(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'store_app/cart_index.html', getCartContext(request))

def getCartAmount(cart, item_id):
    return float(cart[item_id])

class CartConfirmCheckout(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'store_app/checkout_index.html', getCartContext(request))

def getCartContext(request):
    cart = request.session['cart']
    relevant_products = Product.objects.filter(id__in=cart.keys())
    products_and_prices = []
    for product in relevant_products:
        #name, price, amount, total price
        products_and_prices.append({
            'name': product.name,
            'price': product.price,
            'amount': cart[str(product.id)],
            'subtotal': float(cart[str(product.id)])*product.price,
        })
    total_price = sum(product['subtotal'] for product in products_and_prices)
    context = {
        'products_and_prices': products_and_prices,
        'total_price': total_price,
    }
    return context
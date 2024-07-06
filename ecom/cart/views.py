from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse,HttpResponseBadRequest
from django.contrib import messages

# Create your views here.
def cart_summary(request):
   #get the cart
    cart = Cart(request)
    cart_products =cart.get_prods
    quantities = cart.get_quants
    totals =cart.cart_total()
    return render(request,"cart_summary.html",{"cart_products":cart_products,"quantities":quantities,"totals":totals})
    #return render(request,"cart_summary.html",{"cart_products":cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
       # try:
            product_id = int(request.POST.get('product_id'))
            
            product_qty = int(request.POST.get('product_qty'))

            product = get_object_or_404(Product,id=product_id)
            cart.add(product=product,quantity=product_qty)
             #, quantity= product_qty)
            cart_quantity = cart.__len__()
            messages.success(request,("Product added"))
  
            response = JsonResponse({'qty': cart_quantity})
            return response
            
        #except (ValueError, TypeError):
        #    return JsonResponse({'error': 'Invalid input'}, status=400)

        #product = get_object_or_404(Product, id=product_id)
        
        #response = JsonResponse({'Product Name': product.name, 'qty': cart_quantity})
        #response = JsonResponse({'qty': cart_quantity})
         



def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        #product_qty = int(request.POST.get('product_qty'))

        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request,("item deleted "))
  
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id,quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        messages.success(request,(" Cart updated"))
        return response
        #return redirect('cart_summary')
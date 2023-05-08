import json
import stripe
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product,Category,Order,OrderItem
from django.db.models import Q
from .cart import Cart
from vendor.forms import OrderForm
from django.conf import settings
from django.http import JsonResponse

#______________________________add product_______________________________________
def add_to_cart(request,product_id):
    cart=Cart(request)
    cart.add(product_id)
    return redirect('cart_view')

#______________________________remove product_______________________________________
def remove_from_cart(request,product_id):
    cart=Cart(request)
    cart.remove(str(product_id))
    return redirect('cart_view')

#______________________________update quantity_______________________________________
def update_quantity(request,product_id):
    action = request.GET.get('action','')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        
        cart=Cart(request)
        cart.add(product_id,quantity,True)
    
    return redirect('cart_view')

#______________________________les info sur les produits de la panier_______________________________________
def cart_view(request):
    cart=Cart(request)
    return render(request,'cart/cart.html',{
        'cart':cart
    })

#______________________________success page afer ordering_______________________________________
def success(request):
    return render(request,'cart/success.html')

#____________________________checkout_______________________________________
@login_required
def checkout(request):
    cart = Cart(request)

    if cart.get_total_cost() == 0:
        return redirect('cart_view')

    if request.method == 'POST':
        data=json.loads(request.body)
        first_name=data['first_name']
        last_name=data['last_name']
        email_address=data['email_address']
        phone_number=data['phone_number']
        address=data['address']
        zipcode=data['zipcode']
        city=data['city']
        if first_name and last_name and email_address and phone_number and address and zipcode and city:
          
            form = OrderForm(request.POST)

            total_price = 0
            items=[]

            for item in cart:
                    product = item['product']
                    total_price += product.price * int(item['quantity'])

                    items.append({
                        'price_data': {
                            'currency': 'mad',
                            'product_data': {
                                'name': product.title,
                            },
                            'unit_amount': int(product.price * 100),
                        },
                        'quantity': int(item['quantity']),
                    })

            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=items,
                    mode='payment',
                    success_url='http://127.0.0.1:8000/cart/success',
                    cancel_url='http://127.0.0.1:8000/cart',
                )
            payment_intent= session.payment_intent

            order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            phone_number=phone_number,
            address=address,
            zipcode=zipcode,
            city=city,
            created_by = request.user,
            is_paid = True,
            payment_intent = payment_intent,
            paid_amount = total_price
            )

            for item in cart:
                    product = item['product']
                    quantity = int(item['quantity'])
                    price = product.price * quantity

                    item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
    
            cart.clear()

            return JsonResponse({'session':session,'order':payment_intent})
    else:
        form = OrderForm()

    return render(request, 'cart/checkout.html', {
        'cart': cart,
        'form': form,
        'pub_key': settings.STRIPE_PUB_KEY,
    })
  
#______________________________search_______________________________________
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query))
    return render(request, 'product/search.html', {'products': products, 'query': query})


#______________________________products in frontpage_______________________________________
def product(request):
    product_object = Product.objects.filter(active=True)
    return render(request, 'product/product.html', {'product_object': product_object})


#______________________________detail_______________________________________
def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'product/product.html', {'product': product_object}) 


#______________________________category_______________________________________
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'product/category.html', {'category': category})

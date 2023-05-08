from django.conf import settings
from .models import Product

class Cart(object):
# set the variables
    def __init__(self, request):
# get the session from request
        self.session = request.session
# check if there is a cart with a session id in it
        cart = self.session.get(settings.CART_SESSION_ID)

# if not we create a new session and set it as an empty dectionary
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
#cree ou retourner une carte         
        self.cart = cart

#get the product from DB
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

#augmenter le prix si on ogmente la quantity       
        for item in self.cart.values():
            item['total_price'] =int(item['product'].price * item['quantity'])

            yield item
    
# show how many product we have in the cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

#convert the key to string 
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

 #si le produit n'es pas dans la panier on l'ajoute       
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}

#si il ya deja un produit dans la carte on incremente la quantite       
        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)
 
#if the quantite equals 0 then dont show any product 
        if self.cart[product_id]['quantity'] == 0:
            self.remove(product_id)
                        
        self.save()
    
    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
 
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
# return the total price of all products qui se trouvent dans la panier 
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['quantity'] * item['product'].price for item in self.cart.values()))
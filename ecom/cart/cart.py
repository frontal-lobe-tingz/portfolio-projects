from store.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        #get request
        self.request = request
        # Get the current cart from the session, or create a new one if it doesn't exist
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages
        self.cart = cart

    def db_add(self,product,quantity):
        product_id = str(product)
        product_qty =str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
         #get current profile
         current_user = Profile.objects.filter(user__id=self.request.user.id)   
         #conver ' into ""
         carty = str(self.cart)
         #update cart
         carty = carty.replace("\'","\"")
        #save carty to profile model
        current_user.update(old_cart=str(carty))


    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty =str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        #deal with logged in user
        if self.request.user.is_authenticated:
         #get current profile
         current_user = Profile.objects.filter(user__id=self.request.user.id)   
         #conver ' into ""
         carty = str(self.cart)
         #update cart
         carty = carty.replace("\'","\"")
        #save carty to profile model
        current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get ids from cart
        product_ids=self.cart.keys()

        #use id to look up pro
        products = Product.objects.filter(id__in = product_ids)

        #return those looked up prods
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart

        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart

        if self.request.user.is_authenticated:
         #get current profile
         current_user = Profile.objects.filter(user__id=self.request.user.id)   
         #conver ' into ""
         carty = str(self.cart)
         #update cart
         carty = carty.replace("\'","\"")
         #save carty to profile model
         current_user.update(old_cart=str(carty))

        return thing

    def cart_total(self):
        #get product IDS
        product_ids =self.cart.keys()
        #lookup keys in our products database model
        products = Product.objects.filter(id__in=product_ids)

        quantities =self.cart
        #start at 0
        total = 0 
        for key,value in quantities.items():
            #convert string into int to do maths
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                       total = total + (product.price * value)

        return total

    def delete(self, product):
    
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

        if self.request.user.is_authenticated:
         #get current profile
         current_user = Profile.objects.filter(user__id=self.request.user.id)   
         #conver ' into ""
         carty = str(self.cart)
         #update cart
         carty = carty.replace("\'","\"")
        #save carty to profile model
         current_user.update(old_cart=str(carty))
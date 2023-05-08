from django.db import models
from vendor.models import Vendor
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=True,blank=True)
    date_added= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,related_name='products',on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    date_added= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2,default=0,null=True,blank=True)
    is_paid = models.BooleanField(default=False)
    payment_intent = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title
    
    def get_total_price(self):
        return self.price * self.quantity
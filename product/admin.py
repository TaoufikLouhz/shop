from django.contrib import admin
from .models import Category,Product,Order,OrderItem
admin.site.site_header = 'Shop Admin'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','category','vendor','active','date_added']
    list_editable = ['active']
    search_fields=['title']
    list_filter=['category','price','active']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_address','is_paid','created_at']
    list_editable = ['is_paid']
    search_fields=['first_name','last_name','email_address','phone_number','address','zipcode','city']
    list_filter=['is_paid','created_at']

class Order_itemAdmin(admin.ModelAdmin):
    list_display = ['order','product','price','quantity']
    search_fields=['product','price','quantity']
    list_filter=['order','product','price','quantity']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,Order_itemAdmin)


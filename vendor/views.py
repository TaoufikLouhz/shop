from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.shortcuts import render, redirect
from .models import Vendor
from product.models import Product,Order,OrderItem
from .forms import ProductForm
from .forms import UserRegistrationForm

def become_vendor(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserRegistrationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    return render(request, 'vendor/vendor_admin.html', {
        'vendor': vendor, 
        'products': products,
        })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    vendor = request.user.vendor
    product = vendor.products.get(pk=pk)


    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('vendor_admin')
    else:
        form = ProductForm(instance=product)
        return render(request, 'vendor/edit_product.html', {'form': form,'product':product})

def orders(request):
    vendor = request.user.vendor
    order_items = OrderItem.objects.filter(product__vendor=vendor)
    return render(request,'vendor/orders.html', {
        'vendor': vendor, 
        'order_items': order_items,
        })


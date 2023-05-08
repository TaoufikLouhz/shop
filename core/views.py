from django.shortcuts import render
from django.core.paginator import Paginator
from product.models import Product

def frontpage(request):
    nouveau_products = Product.objects.all()
    paginator=Paginator(nouveau_products,8)
    page=request.GET.get('page')
    nouveau_products=paginator.get_page(page)

    return render(request, 'core/frontpage.html', {'nouveau_products': nouveau_products})

def contact(request):
    return render(request, 'core/contact.html') 
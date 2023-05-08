from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('update_quantity/<str:product_id>/',views.update_quantity,name='update_quantity'),
    path('cart/',views.cart_view, name='cart_view'),
    path('cart/success/', views.success, name='success'),
    path('cart/checkout/',views.checkout, name='checkout'),
    path('<int:myid>', views.detail, name="detail"),
    path('search/<int:myid>', views.detail, name="detail"),
    path('pc/<int:myid>', views.detail, name="detail"),
    path('Phones/<int:myid>', views.detail, name="detail"),
    path('Clothes/<int:myid>', views.detail, name="detail"),
    path('<slug:category_slug>/', views.category, name='category'),
]


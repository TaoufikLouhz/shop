from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact', views.contact,name='contact'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import User
from product.models import Product,Order
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

#________________________________________login form___________________________________________________________________
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username= forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "enter username",
    }))

    password= forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "password",
        "placeholder" : "enter password",
    }))

#_________________________________creation du compte ___________________________________________________
class UserRegistrationForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "text",
        "placeholder" : "enter username",
    }),label="Username")

    password1= forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "password",
        "placeholder" : "enter password",
    }))

    password2= forms.CharField(widget=forms.TextInput(attrs={
        "class" : "input",
        "type" : "password",
        "placeholder" : "re-enter password",
    }))

    class Meta:
        model = User
        fields = ['username','password1','password2']

#__________________________________ajouter des produits_____________________________________
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price','active']

#__________________________________Order form_____________________________________
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email_address', 'phone_number','address','zipcode','city']



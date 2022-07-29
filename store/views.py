from django.contrib import messages
from django import views
from django.shortcuts import render
from django.views import View
from .models import Customer, Product,Cart, OrderPlaced, User
from .forms import CustomerRegistrationForm
# Create your views here.
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request,'store/home.html',{'topwears':topwears, 'bottomwears':bottomwears,'mobiles':mobiles})

class ProductDetailView(View):
    def get(self,request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'store/productdetail.html', {'product':product})

def mobile(request, data=None):
    if data==None:
        mobiles = Product.objects.filter(category='M')
    elif data== 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'store/mobile.html',{'mobiles':mobiles})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'store/customerregistration.html', {'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'store/customerregistration.html', {'form':form})

def profile(request):
    return render(request, 'store/profile.html')

def add_to_cart(request):
    user = request.user 
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return render(request, 'store/addtocart.html')
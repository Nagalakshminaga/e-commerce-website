from django.shortcuts import render,redirect
from .forms import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request, "store/index.html",{"products":products})

def logout_page(request):
    if request.user.is_authenticated:
      logout(request)
      messages.success(request,"logout successfully")
    return render(request, "store/index.html")


def login_usage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
      if request.method=="POST":    
         name=request.POST.get('username')
         pwd=request.POST.get('password')
         user=authenticate(request, username=name, password=pwd)
         if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect('home')
         else:
             messages.error(request,"Invalid username or password")
             return redirect('login_usage')
      return render(request,"store/login.html") 
def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
          form.save()
          messages.success(request,"Registration Success you can login now..!")
          return redirect('login_usage')
    return render(request,"store/register.html",{"form":form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request, "store/collections.html", {"catagory":catagory})

def collectionsview(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
     products=Product.objects.filter(category__name=name)
     return render(request,"store/products/index.html",{"products":products,"category":name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"store/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Category Found")
        return redirect('collections')
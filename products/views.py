from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm



@login_required(login_url='login')
def index(request):
    products =  Product.objects.all()
    return render(request,'index.html',
                  {'products':products})

def loginuser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
                login(request,user)
                return redirect('home')

    return render(request,"loginpage.html",{'page':page})


def logoutuser(request):
    logout(request)
    return redirect('login')    

def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #  form.save()
             
            user = form.save(commit=False)
            user.save()

            user = authenticate(request,username=request.POST['username'],password=request.POST['password1'])
            if user is not None:
                login(request,user)
                return redirect('home')

    context ={'form':form,'page':page}
    return render(request,'loginpage.html',context)

def new(request):
    return HttpResponse(
     New products comming soon )




from django.shortcuts import render,redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
# Create your views here.

User=settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            new_user=authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect('core:index')
    else:
        form=UserRegisterForm()
    context={
    'form':form
    }
    return render(request, 'core/userauth/signup.html',context)


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request,"You are already logged in")
        return redirect('core:index')
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=User.objects.get(email=email)
        except:
            messages.warning(request,f'User with {email} doesnt exist.')
        
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You logged in successfully!!!")
            return redirect('core:index')
        else:
            messages.warning(request,f'Invalid credentials')
    return render(request, 'core/userauth/login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You logged out successfully!!!")
        return redirect('userauth:login')
    else:
        messages.warning(request,"You are not logged in")
        return redirect('userauth:login')
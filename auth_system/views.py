from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from auth_system.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, 'Some error')

    form = CustomUserCreationForm()
    return render(
        request, 
        template_name='auth_system/register.html',
        context = {'form': form}
    )

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else: 
                messages.error(request, "Incorrect login and password.")
    else:
        form = AuthenticationForm() 
        return render(
        request, 
        template_name='auth_system/login.html',
        context = {'form': form}
    )

def logoutview(request):
    logout(request)
    return redirect('index')               
             
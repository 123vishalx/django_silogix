from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from .models import ContactSubmission

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('contact')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contact')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'index4.html')

def about(request):
    return render(request, 'about1.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def research(request):
    return render(request, 'research.html')

def services(request):
    return render(request, 'services.html')

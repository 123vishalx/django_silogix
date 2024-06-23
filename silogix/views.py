from django.shortcuts import render



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

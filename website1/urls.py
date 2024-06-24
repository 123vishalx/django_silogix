"""
URL configuration for website1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from silogix import views
from silogix.views import contact_view, register, user_login
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from silogix.views import contact_view, success_view
 


urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('', views.home, name='index4'),
    path('about1/', views.about, name='about'),
    path('product/', views.product, name='product1'),
    path('product2/', views.product2, name='product2'),
    path('product3/', views.product3, name='product3'),
    path('research/', views.research, name='research'),
    path('services/', views.services, name='services'),
    path('contact/', contact_view, name='contact'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]

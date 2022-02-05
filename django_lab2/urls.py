"""django_lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from affairs.views import registeruser,login,home,insert,delete,update,search
from apicall.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registeruser', registeruser),
    path('login', login),
    path('home', home),
    path('add', insert, name= "insert"),
    path('delete/<id>', delete,name="delete"),
    path('update/<id>', update, name="update"),
    path('homesearch', search, name="search"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

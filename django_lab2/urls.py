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
from django.urls import path
from affairs.views import registeruser,login,home,insert,delete,update,search,log_out,insert_form,insert_model_form,add_admin,login_admin,MyUserList,TrackList

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('registeruser', registeruser),
    # path('login', login),
    path('registeruser', add_admin),
    path('login', login_admin),
    path('log_out', log_out, name="log_out"),
    path('home', home),
    path('tracklist', TrackList.as_view()),
    path('userlist', MyUserList.as_view()),
    path('add', insert, name= "insert"),
    path('addform', insert_form, name= "insert"),
    path('addmodelform', insert_model_form, name= "insert"),
    path('delete/<id>', delete,name="delete"),
    path('update/<id>', update, name="update"),
    path('homesearch', search, name="search"),
]

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import myuser,Students,Track,Intake
from .forms import Form, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
# Create your views here.
def registeruser(request):
    if(request.method== 'GET'):
        return  render(request, 'pages/register.html')
    else:
        print(request.POST)
        myuser.objects.create(name=request.POST['username'], email=request.POST['email'],password=request.POST['password'])
        user=myuser.objects.all()
        return redirect('/login',{'users':user})

def login(request):
    context={}
    if(request.method=='GET'):
        context['users']=myuser.objects.all()
        return render(request, 'pages/login.html',context)
    else:
        username=request.POST['username']
        password=request.POST['password']
        user= myuser.objects.filter(name=username,password=password)
        if(user):
            return HttpResponseRedirect('/home')

        else:
            context['errormsg']='no such credentials found'
            return render(request, 'pages/login.html', context)


class MyUserList(ListView):
    model = myuser


class TrackList(ListView):
    model = Track

def home(request):
    context = {}
    context['users'] = Students.objects.all()
    return render(request, 'pages/home.html', context)

def insert(request):
    if (request.method == 'GET'):
        return render(request, 'pages/insertform.html')
    else:
        Students.objects.create(name=request.POST['username'], track=request.POST['track'])
        user = Students.objects.all()
        return redirect('/home', {'users': user})

def insert_form(request):
    context = {}
    form = Form()
    if (request.method == 'GET'):
        context['form'] = form
        return render(request, 'pages/insertform2.html', context)
    else:
        Students.objects.create(name=request.POST['username'], track=request.POST['track'])
        user = Students.objects.all()
        return redirect('/home', {'users': user})

def insert_model_form(request):
    context={}
    form=ModelForm()
    if(request.method=='GET'):
        context['form']=form
        return render(request, 'pages/insertform2.html', context)
    else:
        Students.objects.create(name=request.POST['username'], track=request.POST['track'])
        user = Students.objects.all()
        return redirect('/home', {'users': user})


def delete(request,id):
    Students.objects.filter(id=id).delete()
    return redirect ('/home')

def update(request,id):
    if(request.method=='GET'):
        context={}
        user = Students.objects.filter(id=id)
        for cred in user:
            context['track']= cred.track
            context['name'] = cred.name
            print(context)
        return render (request,'pages/editform.html',context)
    else :
        user=Students.objects.get(id=id)
        user.name=request.POST['username']
        user.track=request.POST['track']
        user.save()
        return redirect('/home')

def search(request):
    context = {}
    query = request.GET.get('searched')
    print(query)
    context['users'] = Students.objects.filter(name=query)
    return render(request, 'pages/homesearch.html', context)

def log_out(request):
    request.session['username']=None
    logout(request)
    return render(request, 'pages/login.html')

def login_admin(request):
    context={}
    if(request.method=='GET'):
        return render(request, 'pages/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        authuser = authenticate(username=username,password=password)
        user=myuser.objects.filter(name=username,password=password)

        if(authuser is not None and user is not  None):
            request.session['username']=username
            login(request, authuser)
            return render(request,'pages/home.html',context)
        else:
            context['msg'] = 'Invalid credentials'
            return render(request, 'pages/login.html', context)

def add_admin(request):
    context={}
    if(request.method=='GET'):
        return render(request,'pages/adminform.html',context)
    else:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        myuser.objects.create(name=username,password=password)
        User.objects.create_user(username=username,email=email,password=password,is_staff="True")
        return render(request, 'pages/login.html', context)
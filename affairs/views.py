from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import myuser,Students
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

def delete(request,id):
    Students.objects.filter(id=id).delete()
    return redirect ('/home')

def update(request,id):
    if(request.method=='GET'):
        context={}
        user = myuser.objects.filter(id=id)
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
    context['users'] = Students.objects.filter(name=query)
    return render(request, 'pages/homesearch.html', context)
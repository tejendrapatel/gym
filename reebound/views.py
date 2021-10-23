from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from reebound.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import User

def Home(request):
    gal = Gallery.objects.all()
    trainer = Trainers.objects.all()
    workout = Workout.objects.all()
    plan = Plan.objects.all()
    d = {"gal": gal,"trainer":trainer,"plan":plan,"workout":workout}
    return render(request,'index.html',d)
def About(request):
    aboutus = ABOUTUS.objects.all()
    train = Trainers.objects.all()
    d = {"train":train,"aboutus":aboutus}
    return render (request,'about-us.html',d)
def Services(request):
    plan = Plan.objects.all()
    servicesvideo = SERVICES.objects.all()
    d = {"plan": plan,"servicesvideo":servicesvideo}
    return render (request,'services.html',d)
def Team(request):
    trainer = Trainers.objects.all()
    d= {"trainer":trainer}
    return render (request,'team.html',d)
def Class (request):
    ttable = TimeTable.objects.all()
    d= {"ttable":ttable}
    return render (request,'class-details.html',d)
def Contact(request):
    return render (request,'contact.html')
def BMIcalculator(request):
    return render (request,'bmi-calculator.html')
def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)
def Registration (request):
    plan = Plan.objects.all()
    workout = Workout.objects.all()
    trainer = Trainers.objects.all()
    d = {"plan": plan,"trainer":trainer,"workout":workout}
    return render (request,'registration.html',d)
def BLOG(request):
    blogg = blog.objects.all()
    d = {"blogg":blogg}
    return render(request,'blog.html',d)
def Blogdetail(request):
    return render(request,'blog-details.html')
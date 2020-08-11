from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base2.html")

def home(request):
    return render(request,"myapp2/home.html")

def profile(request):
    name="Hrushikesh"
    return render(request,"myapp2/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html")
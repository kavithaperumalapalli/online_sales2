from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showindex(request):
    return render(request,"index.html")
def validateUser(request):
    uname=request.POST.get('username')
    passward=request.POST.get('passward')

    if uname=="sathya" and passward=="tech":
       return render(request,"welcome.html")
    else:
       return render(request,"index.html",{"meg":"invalid user"})
def logoutUser(request):
    return render(request,"index.html")



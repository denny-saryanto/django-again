from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from djangomid import views as viewsDjangomid

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse(viewsDjangomid.index))

def login_render(request):
    context = {}
    if request.user.is_authenticated:
        return render(request, "accounts/login-accounts.html", {})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error" : "Invalid Username or Password"}
            return render(request, "accounts/login-accounts.html", context)
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    return render(request, "accounts/login-accounts.html", context=context)

def logout_render(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    return render(request, "accounts/logout-accounts.html", context={})

def register_render(request):
    return render(request, "accounts/register.html", context={})
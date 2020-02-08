from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import LoginForm,SignUpForm


# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/contact")

    return render(request, "login.html", {"forms": form})


def register(request):
    
    if request.method == "POST" :
        form = SignUpForm(request.POST or None)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect('/login')
    else :
        form = SignUpForm()

    return render(request,'register.html',{'forms':form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError


@login_required
def account_settings(request):
    """main page of account settings"""
    return render(request, "account/account.html")


def login_func(request):
    """user authorization"""
    if request.method == "GET":
        return render(request, "account/login_user.html")
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            try:
                return redirect(request.GET["next"])
            except MultiValueDictKeyError:
                return redirect("account")
        else:
            return render(request, "account/login_user.html",
                          {"error": "Username or password does not exist or does not match"})


def signup_func(request):
    """user registration"""
    if request.method == "GET":
        return render(request, "account/signup_user.html")
    else:
        if request.POST["password1"] is None and request.POST["password2"] is None:
            if request.POST["password1"] == request.POST["password2"]:
                try:
                    user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                    user.save()
                    login(request, user)
                    try:
                        return redirect(request.GET["next"])
                    except MultiValueDictKeyError:
                        return redirect("account")
                except (IntegrityError, ValueError):
                    return render(request, "account/signup_user.html",
                                  {"error": "Username already exists, please try another one"})
            else:
                return render(request, "account/signup_user.html",
                              {"error": "Password mismatch"})
        else:
            return render(request, "account/signup_user.html",
                          {"error": "Password not entered"})


@login_required
def logout_user(request):
    """user logout"""
    if request.method == "POST":
        logout(request)
        return redirect("home")

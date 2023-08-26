from django.shortcuts import render


def account(request):
    return render(request, "account/account.html")


def login_user(request):
    pass


def signup_user(request):
    pass


def logout_user(request):
    pass

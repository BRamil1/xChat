from django.shortcuts import render


def home(request):
    return render(request, "base/home.html")


def author(request):
    return render(request, "base/author.html")


def test_404(request):
    return render(request, "base/404.html")

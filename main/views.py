from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def author(request):
    return render(request, "main/author.html")

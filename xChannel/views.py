from django.shortcuts import render
from .models import Message
# from django.contrib.auth.models import User


def channel(request):
    messages = Message.objects.all()
    if not messages:
        messages = None
    return render(request, "xChannel/xChannel.html", {"messages": messages})


def my_messages(request):
    messages = Message.objects.filter(user=request.user).order_by("-date_creation")
    if not messages:
        messages = None
    return render(request, "xChannel/my_messages.html", {"messages": messages})

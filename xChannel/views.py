from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm


def channel(request):
    """shows all notifications"""
    messages = Message.objects.all()
    return render(request, "xChannel/xChannel.html", {"messages": messages})


def my_messages(request):
    """shows your messages"""
    messages = Message.objects.filter(user=request.user).order_by("-date_creation")
    return render(request, "xChannel/my_messages.html", {"messages": messages})


def create(request):
    """create a message"""
    if request.method == "POST":
        try:
            form = MessageForm(request.POST)
            new_messages = form.save(commit=False)
            new_messages.user = request.user
            new_messages.save()
            return redirect("xChannel")
        except ValueError:
            return redirect("xChannel")
    else:
        return redirect("xChannel")

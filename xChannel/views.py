from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageCreateForm, MessageUpdateForm, MessageDeleteForm


def channel(request):
    """shows all notifications"""
    messages = Message.objects.filter(is_show=False)
    return render(request, "xChannel/xChannel.html", {"messages": messages})


def my_messages(request):
    """shows your messages"""
    messages = Message.objects.filter(user=request.user, is_show=False).order_by("-date_creation")
    return render(request, "xChannel/my_messages.html", {"messages": messages})


def create(request):
    """create a message"""
    if request.method == "POST":
        try:
            form = MessageCreateForm(request.POST)
            new_message = form.save(commit=False)
            new_message.user = request.user
            new_message.save()
            return redirect("xChannel")
        except ValueError:
            return redirect("xChannel")
    else:
        return redirect("xChannel")


def update(request):
    if request.method == "POST":
        form = MessageUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            message = Message.objects.get(id=form.cleaned_data["id"])
            message.text = form.cleaned_data["text"]
            message.image = form.cleaned_data["image"]
            message.save()
            return redirect("xChannel")
    else:
        return redirect("xChannel")


def delete(request):
    """delete a message"""
    if request.method == "POST":
        try:
            form = MessageDeleteForm(request.POST)
            message = Message.objects.filter(user=request.user, id=form.message.id)
            message.is_show = True
            message.save()
            return redirect("xChannel")
        except ValueError:
            return redirect("xChannel")
    else:
        return redirect("xChannel")


def delete_all(request):
    """delete all messages"""
    if request.method == "POST":
        messages = Message.objects.filter(user=request.user)
        for message in messages:
            message.is_show = True
        messages.save()
        return redirect("xChannel")
    else:
        return redirect("xChannel")

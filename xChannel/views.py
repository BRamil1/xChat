from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageCreateForm, MessageUpdateForm


@login_required
def channel(request):
    """shows all notifications"""
    messages = Message.objects.filter(is_show=False)
    return render(request, "xChannel/xChannel.html", {"messages": messages})


@login_required
def my_messages(request):
    """shows your messages"""
    messages = Message.objects.filter(user=request.user, is_show=False).order_by("-date_creation")
    return render(request, "xChannel/my_messages.html", {"messages": messages})


@login_required
def create(request):
    """create a message"""
    if request.method == "POST":
        form = MessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
        return redirect("xChannel")
    else:
        return redirect("xChannel")


@login_required
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


@login_required
def delete(request, id_msg):
    """delete a message"""
    if request.method == "POST":
        message = Message.objects.get(id=id_msg)
        if message.user.id == request.user.id:
            message.is_show = True
            message.save()
        return redirect("my_messages")
    else:
        return redirect("my_messages")


@login_required
def delete_all(request):
    """delete all messages"""
    if request.method == "POST":
        messages = Message.objects.filter(user=request.user)
        for message in messages:
            message.is_show = True
            message.save()
        return redirect("account")
    else:
        return redirect("account")

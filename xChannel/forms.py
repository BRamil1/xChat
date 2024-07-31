from django.forms import ModelForm
from .models import Message


class MessageCreateForm(ModelForm):
    class Meta:
        model = Message
        fields = ["text", "image"]


class MessageUpdateForm(ModelForm):
    class Meta:
        model = Message
        fields = ["text", "image"]


class MessageDeleteForm(ModelForm):
    class Meta:
        model = Message
        fields = ["id"]
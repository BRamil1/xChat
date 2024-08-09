from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(max_length=4096)
    image = models.ImageField(upload_to="xChannel/images", blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return f"ID: {self.id} USER: {self.user}"

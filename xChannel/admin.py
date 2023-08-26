from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ("date_creation", "id",)


admin.site.register(Message, MessageAdmin)

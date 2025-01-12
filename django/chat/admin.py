from django.contrib import admin
from .models import Room, Message


@admin.register(Room)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    pass

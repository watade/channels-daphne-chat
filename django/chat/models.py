from django.db import models
from ulid import ULID

from accounts.models import User

ULID_LENGTH = 26


class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = ULID_LENGTH
        kwargs["unique"] = True
        kwargs["default"] = self._generate_ulid
        super().__init__(*args, **kwargs)

    def _generate_ulid(self):
        return str(ULID())

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"], kwargs["unique"], kwargs["default"]
        return name, path, args, kwargs


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    public_id = ULIDField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    publisher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

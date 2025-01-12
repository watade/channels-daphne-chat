from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("", views.RoomView.as_view(), name="index"),
    path("<str:public_id>/", views.room, name="room"),
]

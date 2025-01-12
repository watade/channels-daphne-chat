from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import RoomForm
from .models import Room


class RoomView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = "chat/index.html"
    form_class = RoomForm

    def get_success_url(self):
        return reverse("chat:room", kwargs={"public_id": self.object.public_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context


@login_required
def room(request, public_id):
    room = Room.objects.get(public_id=public_id)
    return render(request, "chat/room.html", {"room": room})

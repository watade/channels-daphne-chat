from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(UserPassesTestMixin, CreateView):
    template_name = "accounts/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("chat:index")

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect("chat:index")

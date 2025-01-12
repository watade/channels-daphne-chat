from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import LoginForm
from .views import SignupView

login_view = LoginView.as_view(
    template_name="accounts/login.html",
    redirect_authenticated_user=True,
    form_class=LoginForm,
)
logout_view = LogoutView.as_view(template_name="accounts/login.html")
signup_view = SignupView.as_view()

app_name = "accounts"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]

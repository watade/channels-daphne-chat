from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

# from .forms import LoginForm

login_view = LoginView.as_view(
    template_name="login.html",
    redirect_authenticated_user=True,  # , form=LoginForm()
)
logout_view = LogoutView.as_view(template_name="logout.html")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

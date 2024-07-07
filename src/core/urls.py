from django.urls import path

from core.views import LoginView, SignupView


urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_usuario, name="login"),
    path("logout", views.logout_usuario, name="logout")
]

from django.urls import path

from OhMyDog.views.home import home
from OhMyDog.views.auth import register, login_usuario, logout_usuario

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
]

from django.urls import path

# from . import views_a_borrar
from OhMyDog.views.home import home
from OhMyDog.views.auth import login_usuario, logout_usuario, register

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
]

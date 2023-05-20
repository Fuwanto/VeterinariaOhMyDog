from django.urls import path
from . import views_a_borrar
from OhMyDog.views.home import home

urlpatterns = [
    path("", home, name="home"),
    path("register", views_a_borrar.register, name="register"),
    path("login", views_a_borrar.login_usuario, name="login"),
    path("logout", views_a_borrar.logout_usuario, name="logout"),
]

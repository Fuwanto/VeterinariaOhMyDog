from django.urls import path
from . import views_a_borrar
from OhMyDog.views.home import home

urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_usuario, name="login"),
    path("logout", views.logout_usuario, name="logout")
=======
    path("", home, name="home"),
    path("register", views_a_borrar.register, name="register"),
    path("login", views_a_borrar.login_usuario, name="login"),
    path("logout", views_a_borrar.logout_usuario, name="logout"),
>>>>>>> 3a81d9f2968b8ed7d554bfdd8b29a498b0c57a9e
]

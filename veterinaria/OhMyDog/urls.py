from django.urls import path

from OhMyDog.views.home import home
from OhMyDog.views.auth import register, login_usuario, logout_usuario, primer_inicio
from OhMyDog.views.clientes import mis_datos, mis_perros, mis_turnos, todos_los_clientes
from OhMyDog.views.turnos import solicitudes_de_turnos

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
    path("mis_datos", mis_datos, name="mis_datos"),
    path("mis_perros", mis_perros, name="mis_perros"),
    path("mis_turnos", mis_turnos, name="mis_turnos"),
    path("clientes", todos_los_clientes, name="clientes"),
    path("solicitudes_de_turnos", solicitudes_de_turnos, name="solicitudes_de_turnos"),
    path("primer_inicio", primer_inicio, name="primer_inicio")
]

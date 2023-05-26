from django.urls import path

from OhMyDog.views.home import home
from OhMyDog.views.auth import register, login_usuario, logout_usuario, primer_inicio
from OhMyDog.views.clientes import mis_datos, mis_perros, mis_turnos, todos_los_clientes, datos_de_un_cliente, buscar_clientes, listado_de_perros_cliente, agregar_perro
from OhMyDog.views.turnos import solicitar_turnos, turnos_pendientes


urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
    path("mis_datos", mis_datos, name="mis_datos"),
    path("mis_perros", mis_perros, name="mis_perros"),
    path("mis_turnos", mis_turnos, name="mis_turnos"),
    path("primer_inicio", primer_inicio, name="primer_inicio"),
    path('buscar_clientes', buscar_clientes, name='buscar_clientes'),
    path("clientes", todos_los_clientes, name="clientes"),
    path('clientes/<int:cliente_id>/', datos_de_un_cliente, name='datos_de_un_cliente'),
    path('clientes/<int:cliente_id>/perros', listado_de_perros_cliente, name='listado_de_perros_cliente'),
    path('clientes/<int:cliente_id>/agregar_perro', agregar_perro, name='agregar_perro'),
    path('solicitar_turno',solicitar_turnos, name="solicitar_turno")
    path('turnos_pendientes',turnos_pendientes, name"turnos_pendientes")
    
]

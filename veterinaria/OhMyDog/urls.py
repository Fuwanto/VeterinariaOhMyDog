from django.urls import path

from OhMyDog.views.home import home
from OhMyDog.views.auth import register, login_usuario, logout_usuario, primer_inicio
from OhMyDog.views.clientes import (
    mis_datos,
    mis_perros,
    mis_turnos,
    todos_los_clientes,
    datos_de_un_cliente,
    buscar_clientes,
    listado_de_perros_cliente,
    agregar_perro,
    datos_de_un_perro,
    datos_de_mi_perro,
    borrar_perro,
    borrar_cliente,
)
from OhMyDog.views.turnos import (
    solicitar_turnos,
    solicitudes_de_turnos,
    confirmar_turno,
    rechazar_turno,
)
from OhMyDog.views.atenciones import (
    agregar_atencion_clinica,
    agregar_consulta,
    agregar_desparacitacion,
    agregar_castracion,
    agregar_vacunacion
)


urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
    path("mis_datos", mis_datos, name="mis_datos"),
    path("mis_perros", mis_perros, name="mis_perros"),
    path("mis_perros/<int:perro_id>/", datos_de_mi_perro, name="datos_de_mi_perro"),
    path("mis_turnos", mis_turnos, name="mis_turnos"),
    path("primer_inicio", primer_inicio, name="primer_inicio"),
    path("buscar_clientes", buscar_clientes, name="buscar_clientes"),
    path("clientes", todos_los_clientes, name="clientes"),
    path("clientes/<int:cliente_id>/", datos_de_un_cliente, name="datos_de_un_cliente"),
    path(
        "clientes/<int:cliente_id>/perros",
        listado_de_perros_cliente,
        name="listado_de_perros_cliente",
    ),
    path("clientes/<int:cliente_id>/agregar_perro", agregar_perro, name="agregar_perro"),
    path("solicitar_turno", solicitar_turnos, name="solicitar_turno"),
    path("solicitudes_de_turnos", solicitudes_de_turnos, name="solicitudes_de_turnos"),
    path("confirmar_turno", confirmar_turno, name="confirmar_turno"),
    path("rechazar_turno", rechazar_turno, name="rechazar_turno"),
    path("perros/<int:perro_id>/", datos_de_un_perro, name="datos_de_un_perro"),
    path("borrar_perro/<int:perro_id>", borrar_perro, name="borrar_perro"),
    path("borrar_cliente/<int:cliente_id>", borrar_cliente, name="borrar_cliente"),
    path(
        "agregar_atencion_clinica/",
        agregar_atencion_clinica,
        name="agregar_atencion_clinica",
    ),
    path("agregar_consulta/", agregar_consulta, name="agregar_consulta"),
    path(
        "agregar_desparacitacion/",
        agregar_desparacitacion,
        name="agregar_desparacitacion",
    ),
    path("agregar_castracion/", agregar_castracion, name="agregar_castracion"),
    path("agregar_vacunacion/", agregar_vacunacion, name="agregar_vacunacion")
]

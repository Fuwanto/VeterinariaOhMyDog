from django.urls import path

from OhMyDog.views.home import home
from OhMyDog.views.auth import (
    registrar_cliente,
    login_usuario,
    logout_usuario,
    cambiar_contraseña,
)
from OhMyDog.views.clientes import (
    mis_datos,
    mis_perros,
    mis_turnos,
    listar_clientes,
    datos_de_un_cliente,
    listar_perros_cliente,
    registrar_perro,
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
    agregar_desparasitacion,
    agregar_castracion,
    agregar_vacunacion,
    mostrar_datos_atencion,
)
from OhMyDog.views.perros import (
    datos_de_un_perro,
    atenciones_de_un_perro_cliente,
    atenciones_de_un_perro_veterinario,
    filtrar_listado_atenciones_cliente,
    filtrar_listado_atenciones_veterinario,
)
from OhMyDog.views.paseadores_cuidadores import (
    visualizar_mapa_paseadores,
    agregar_paseador_cuidador_al_mapa,
    visualizar_mapa_cuidadores,
    eliminar_publicacion_paseador,
    eliminar_publicacion_cuidador,
)
from OhMyDog.views.publicaciones_busquedas import (
    tengo_informacion,
    marcar_como_encontrado,
    eliminar_busqueda,
    listar_publicaciones_de_busquedas,
    agregar_publicacion_busqueda,
    mis_busquedas,
)
from OhMyDog.views.publicaciones_adopciones import (
    mis_adopciones,
    agregar_publicacion_adopcion,
    listar_publicaciones_de_adopciones,
    filtrar_listado_adopciones,
    marcar_como_adoptado,
    marcar_como_me_interesa,
    eliminar_adopcion,
)

from OhMyDog.views.campanias_donacion import(
    agregar_campania_donacion,
    listar_campanias_de_donaciones,
    terminar_campania_donacion,
)


miscelaneo = [
    path("", home, name="home"),
    path("login", login_usuario, name="login"),
    path("logout", logout_usuario, name="logout"),
    path("cambiar_contraseña", cambiar_contraseña, name="cambiar_contraseña"),
    path("borrar_perro/<int:perro_id>", borrar_perro, name="borrar_perro"),
    path("borrar_cliente/<int:cliente_id>", borrar_cliente, name="borrar_cliente"),
    path("confirmar_turno", confirmar_turno, name="confirmar_turno"),
    path("rechazar_turno", rechazar_turno, name="rechazar_turno"),
]

datos = [
    path("mis_datos", mis_datos, name="mis_datos"),
    path("mis_perros/<int:perro_id>/", datos_de_mi_perro, name="datos_de_mi_perro"),
    path("clientes/<int:cliente_id>/", datos_de_un_cliente, name="datos_de_un_cliente"),
    path("perros/<int:perro_id>/", datos_de_un_perro, name="datos_de_un_perro"),
    path("datos_atencion_clinica", mostrar_datos_atencion, name="datos_atencion_clinica"),
    path("datos_consulta", mostrar_datos_atencion, name="datos_consulta"),
    path("datos_vacunacion", mostrar_datos_atencion, name="datos_vacunacion"),
    path("datos_castracion", mostrar_datos_atencion, name="datos_castracion"),
    path("datos_desparasitacion", mostrar_datos_atencion, name="datos_desparasitacion"),
]

formularios = [
    path(
        "agregar_atencion_clinica/",
        agregar_atencion_clinica,
        name="agregar_atencion_clinica",
    ),
    path("agregar_castracion/", agregar_castracion, name="agregar_castracion"),
    path("agregar_vacunacion/", agregar_vacunacion, name="agregar_vacunacion"),
    path("agregar_consulta/", agregar_consulta, name="agregar_consulta"),
    path(
        "agregar_desparasitacion/",
        agregar_desparasitacion,
        name="agregar_desparasitacion",
    ),
    path("agregar_publicacion_adopcion", agregar_publicacion_adopcion, name="agregar_publicacion_adopcion"),
    path("agregar_publicacion_busqueda", agregar_publicacion_busqueda, name="agregar_publicacion_busqueda"),
    path("registrar_cliente", registrar_cliente, name="registrar_cliente"),
    path("solicitar_turno", solicitar_turnos, name="solicitar_turno"),
    path("clientes/<int:cliente_id>/registrar_perro", registrar_perro, name="registrar_perro"),
    path("agregar_campania_donacion", agregar_campania_donacion, name= "agregar_campania_donacion")
]

listados = [
    path("clientes", listar_clientes, name="clientes"),
    path(
        "clientes/<int:cliente_id>/perros",
        listar_perros_cliente,
        name="listar_perros_cliente",
    ),
    path("listado_de_atenciones_cliente", atenciones_de_un_perro_cliente, name="listado_de_atenciones_cliente"),
    path("listado_de_atenciones", atenciones_de_un_perro_veterinario, name="listado_de_atenciones"),
    path(
        "filtrar_listado_atenciones_cliente",
        filtrar_listado_atenciones_cliente,
        name="filtrar_listado_atenciones_cliente",
    ),
    path(
        "filtrar_listado_atenciones_veterinario",
        filtrar_listado_atenciones_veterinario,
        name="filtrar_listado_atenciones_veterinario",
    ),
    path("solicitudes_de_turnos", solicitudes_de_turnos, name="solicitudes_de_turnos"),
    path("mis_turnos", mis_turnos, name="mis_turnos"),
    path("mis_perros", mis_perros, name="mis_perros"),
]

publicaciones = [
    path("mis_adopciones", mis_adopciones, name="mis_adopciones"),
    path("mis_busquedas", mis_busquedas, name="mis_busquedas"),
    path(
        "publicaciones/adopciones",
        listar_publicaciones_de_adopciones,
        name="listar_publicaciones_de_adopciones",
    ),
    path(
        "publicaciones/busquedas",
        listar_publicaciones_de_busquedas,
        name="listar_publicaciones_de_busquedas",
    ),
    path("filtar_listado_adopciones", filtrar_listado_adopciones, name="filtrar_listado_adopciones"),
    path("marcar_como_adoptado/<int:adopcion_id>", marcar_como_adoptado, name="marcar_como_adoptado"),
    path("marcar_como_encontrado/<int:busqueda_id>", marcar_como_encontrado, name="marcar_como_encontrado"),
    path("eliminar_adopcion/<int:adopcion_id>", eliminar_adopcion, name="eliminar_adopcion"),
    path("eliminar_busqueda/<int:busqueda_id>", eliminar_busqueda, name="eliminar_busqueda"),
    path("marcar_como_me_interesa", marcar_como_me_interesa, name="marcar_como_me_interesa"),
    path("tengo_informacion", tengo_informacion, name="tengo_informacion"),
    path("mapa_paseadores", visualizar_mapa_paseadores, name="visualizar_mapa_paseadores"),
    path("mapa_cuidadores", visualizar_mapa_cuidadores, name="visualizar_mapa_cuidadores"),
    path(
        "agregar_paseador_cuidador_al_mapa", agregar_paseador_cuidador_al_mapa, name="agregar_paseador_cuidador_al_mapa"
    ),
    path(
        "eliminar_publicacion_C/<int:paseador_cuidador_id>",
        eliminar_publicacion_cuidador,
        name="eliminar_publicacion_C",
    ),
    path(
        "eliminar_publicacion_P/<int:paseador_cuidador_id>",
        eliminar_publicacion_paseador,
        name="eliminar_publicacion_P",
    ),
    path(
        "listar_campanias_de_donaciones",
        listar_campanias_de_donaciones,
        name="listar_campanias_de_donaciones",
    ),
    path(
        "terminar_campania_donacion/<int:campania_id>",
        terminar_campania_donacion,
        name="terminar_campania_donacion",
    )
]

urlpatterns = formularios + listados + miscelaneo + publicaciones + datos

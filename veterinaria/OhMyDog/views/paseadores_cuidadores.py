import folium
from OhMyDog.modelos.publicaciones import (
    todos_los_paseadores,
    todos_los_cuidadores,
    agregar_paseador_cuidador,
    buscar_paseador_cuidador_por_email,
    eliminar_paseador_cuidador,
)
from OhMyDog.views.utils import agregar_mensaje_error
from django.contrib import messages
from django.shortcuts import render, redirect


def mapa_inicial():
    # Crear un mapa de Folium centrado en una ubicación específica
    # location=[longitud, latitud]
    return folium.Map(location=[-34.9214, -57.9544], zoom_start=12)


def generar_punto_paseador_cuidador(paseador_cuidador, user):
    # Agrega un botón dependiendo de la condición
    eliminar_url = "#"
    oculto = "none"
    if user.is_staff:
        eliminar_url = "/eliminar_publicacion_" + f"{paseador_cuidador.tipo}" + "/" + f"{paseador_cuidador.id}"
        oculto = "block"
    popup_html = f"""<strong>Email:</strong> {paseador_cuidador.email}<br>
    <strong>Nombre:</strong> {paseador_cuidador.nombre}<br>
    <strong>Franja Horaria:</strong> {paseador_cuidador.franja_horaria}<br>
    <a href="{eliminar_url}" class="btn btn-danger" style="display:{oculto}; color: white">Eliminar</a>"""

    return folium.Marker(
        location=[float(paseador_cuidador.latitud), float(paseador_cuidador.longitud)],
        popup=popup_html,
        tooltip="Haz clic aquí para más detalles",
    )


def visualizar_mapa_paseadores(request):
    paseadores = todos_los_paseadores()
    mi_mapa = mapa_inicial()

    for paseador in paseadores:
        # Agregar un marcador con información personalizada
        generar_punto_paseador_cuidador(paseador, request.user).add_to(mi_mapa)

    return render(request, "visualizar_mapa.html", {"mapa": mi_mapa.get_root().render(), "tipo": "Paseadores"})


def visualizar_mapa_cuidadores(request):
    cuidadores = todos_los_cuidadores()
    mi_mapa = mapa_inicial()

    for cuidador in cuidadores:
        # Agregar un marcador con información personalizada
        generar_punto_paseador_cuidador(cuidador, request.user).add_to(mi_mapa)

    return render(request, "visualizar_mapa.html", {"mapa": mi_mapa.get_root().render(), "tipo": "Cuidadores"})


def agregar_paseador_cuidador_al_mapa(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        franja_horaria = request.POST.get("franja_horaria")
        latitud = request.POST.get("latitud")
        longitud = request.POST.get("longitud")
        tipo = request.POST.get("tipo")

        trabajador = buscar_paseador_cuidador_por_email(email)
        if trabajador is None:
            # Agregar el nuevo paseador
            agregar_paseador_cuidador(nombre, email, latitud, longitud, franja_horaria, tipo)
            messages.success(request, "Agregado con exito!")
        else:
            agregar_mensaje_error(request, f"Ya existe un cuidador o paseador con email {email}!")

    return render(request, "agregar_paseador_cuidador.html")


def eliminar_publicacion_cuidador(request, paseador_cuidador_id):
    eliminar_paseador_cuidador(paseador_cuidador_id)
    messages.success(request, "Cuidador eliminado con exito!")
    return redirect("visualizar_mapa_cuidadores")


def eliminar_publicacion_paseador(request, paseador_cuidador_id):
    eliminar_paseador_cuidador(paseador_cuidador_id)
    messages.success(request, "Paseador eliminado con exito!")
    return redirect("visualizar_mapa_paseadores")

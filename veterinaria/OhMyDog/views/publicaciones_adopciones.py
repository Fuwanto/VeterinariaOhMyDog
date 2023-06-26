from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones import (
    filtrar_adopciones_por_cliente,
    agregar_adopcion,
    buscar_adopcion_por_nombre_y_cliente,
    listar_todas_adopciones,
    listar_adopciones_no_mias,
    adoptar,
    eliminar_publicacion_adopcion,
    usuario_tiene_interes_adopcion,
    agregar_usuario_interesa,
)
from django.contrib import messages
from OhMyDog.views.utils import agregar_mensaje_error


@login_required
def mis_adopciones(request):
    cliente = request.user.cliente
    adopciones = filtrar_adopciones_por_cliente(cliente)
    return render(request, "mis_adopciones.html", {"adopciones": adopciones})


def listar_publicaciones_de_adopciones(request):
    if request.user.is_authenticated:
        adopciones = listar_adopciones_no_mias(request.user.cliente.id)
        for adopcion in adopciones:
            if usuario_tiene_interes_adopcion(adopcion, request.user.cliente) is None:
                adopcion.tiene_interes = False
            else: 
                adopcion.tiene_interes = True
        return render(
            request,
            "listar_publicaciones_de_adopciones.html",
            {"adopciones": adopciones, "cliente": request.user.cliente},
        )
    else:
        adopciones = listar_todas_adopciones()
        return render(
            request,
            "listar_publicaciones_de_adopciones.html",
            {"adopciones": adopciones, "cliente": None},
        )


@login_required
def agregar_publicacion_adopcion(request):
    tamanios_perro = TamanioPerro.objects.all()
    etapas_vida_perro = EtapaVidaPerro.objects.all()
    cliente = request.user.cliente
    context = {"tamanios": tamanios_perro, "etapas": etapas_vida_perro}
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        tamanio_perro_id = request.POST.get("tamanio_perro_id")
        etapa_vida_perro_id = request.POST.get("etapa_vida_perro_id")
        sexo = request.POST.get("sexo")
        castrado = request.POST.get("castrado")

        publicacion = buscar_adopcion_por_nombre_y_cliente(cliente, nombre)

        if publicacion is None:
            agregar_adopcion(cliente, nombre, descripcion, tamanio_perro_id, etapa_vida_perro_id, sexo, castrado)
            messages.success(request, "Publicacion agregada con exito.")
            return redirect("mis_adopciones")
        else:
            agregar_mensaje_error(request, f"Publicacion con nombre: {nombre}, ya publicada.")
            return redirect("agregar_publicacion_adopcion")
    else:
        return render(request, "agregar_publicacion_adopcion.html", context)


def filtrar_listado_adopciones(request):
    if request.user.is_authenticated:
        adopciones = listar_adopciones_no_mias(request.user.cliente.id)
    else:
        adopciones = listar_todas_adopciones()
    seleccion_sexo = request.GET.get("seleccionSexo")
    seleccion_tamanio = request.GET.get("seleccionTamanio")
    seleccion_etapa_vida = request.GET.get("seleccionEtapaVida")
    seleccion_castrado = request.GET.get("seleccionCastrado")
    if seleccion_sexo != "":
        adopciones = adopciones.filter(sexo=seleccion_sexo)
    if seleccion_tamanio != "":
        tamanio_filtro = TamanioPerro.objects.get(nombre=seleccion_tamanio)
        adopciones = adopciones.filter(tamanio_perro=tamanio_filtro)
    if seleccion_etapa_vida != "":
        etapa_vida_filtro = EtapaVidaPerro.objects.get(nombre=seleccion_etapa_vida)
        adopciones = adopciones.filter(etapa_vida_perro=etapa_vida_filtro)
    if seleccion_castrado != "":
        adopciones = adopciones.filter(castrado=seleccion_castrado)
    return render(
        request,
        "listar_publicaciones_de_adopciones.html",
        {
            "adopciones": adopciones,
            "seleccion_sexo": seleccion_sexo,
            "seleccion_tamanio": seleccion_tamanio,
            "seleccion_etapa_vida": seleccion_etapa_vida,
            "seleccion_castrado": seleccion_castrado,
        },
    )


def marcar_como_me_interesa(request):
    if request.method == "POST":
        adopcion_id = request.POST.get("adopcion_id")
        print(adopcion_id)
        email_interesado = request.POST.get("email")
        telefono = request.POST.get("telefono")
        nombre = request.POST.get("nombre")
        nombre_perro = request.POST.get("nombre_perro")
        email_autor = request.POST.get("email_autor")
        asunto = "Nuevo interesado en Adoptar"
        mensaje = f"{nombre} esta interesado en adoptar a {nombre_perro}. Contacto:\n\nEmail: {email_interesado}\nTeléfono: {telefono}\nNombre: {nombre}"
        remitente = settings.EMAIL_HOST_USER
        destinatario = [email_autor]
        send_mail(asunto, mensaje, remitente, destinatario)
        if request.user.is_authenticated:
            agregar_usuario_interesa(adopcion_id, request.user.cliente)
        messages.success(request, "Tus datos fueron enviados al autor de la publicación. Aguarda su respuesta!")
        return redirect("listar_publicaciones_de_adopciones")
    return redirect("listar_publicaciones_de_adopciones")


@login_required
def marcar_como_adoptado(request, adopcion_id):
    adoptar(adopcion_id)
    messages.success(request, "Publicación marcada como adoptada con exito!")
    return redirect("mis_adopciones")


@login_required
def eliminar_adopcion(request, adopcion_id):
    eliminar_publicacion_adopcion(adopcion_id)
    messages.success(request, "Publicación eliminada con exito!")
    return redirect("mis_adopciones")

from OhMyDog.modelos.publicaciones import (
    agregar_busqueda,
    buscar_busqueda_por_nombre_archivo_y_cliente,
    filtrar_busquedas_por_cliente,
    eliminar_publicacion_busqueda,
    listar_busquedas_por_zona,
    listar_busquedas_no_mias_y_por_zona,
    se_encontro,
    agregar_usuario_tiene_informacion_busqueda,
    usuario_tiene_informacion_busqueda,
)
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from OhMyDog.views.utils import agregar_mensaje_error


@login_required
def mis_busquedas(request):
    cliente = request.user.cliente
    busquedas = filtrar_busquedas_por_cliente(cliente)
    return render(request, "mis_busquedas.html", {"busquedas": busquedas})


def listar_publicaciones_de_busquedas(request):
    zona = request.GET.get("zona", "")
    if request.user.is_authenticated and request.user.cliente:
        busquedas = listar_busquedas_no_mias_y_por_zona(request.user.cliente.id, zona)
        for busqueda in busquedas:
            if usuario_tiene_informacion_busqueda(busqueda, request.user.cliente) is None:
                busqueda.tiene_informacion = False
            else:
                busqueda.tiene_informacion = True
        return render(
            request,
            "listar_publicaciones_de_busquedas.html",
            {"busquedas": busquedas, "zona": zona, "cliente": request.user.cliente},
        )
    else:
        busquedas = listar_busquedas_por_zona(zona)
        return render(
            request, "listar_publicaciones_de_busquedas.html", {"busquedas": busquedas, "zona": zona, "cliente": None}
        )


@login_required
def agregar_publicacion_busqueda(request):
    if request.method == "POST":
        cliente = request.user.cliente
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        zona = request.POST.get("zona")
        foto = request.FILES["foto"]
        publicacion = buscar_busqueda_por_nombre_archivo_y_cliente(cliente, foto.name)

        if publicacion is None:
            agregar_busqueda(cliente, nombre, descripcion, zona, foto)
            messages.success(request, "Publicacion agregada con exito.")
            return redirect("mis_busquedas")
        else:
            agregar_mensaje_error(request, f"Publicacion con archivo: {foto.name}, ya publicada.")
            return redirect("agregar_publicacion_busqueda")
    else:
        return render(request, "agregar_publicacion_busqueda.html")


def tengo_informacion(request):
    if request.method == "POST":
        busqueda_id = request.POST.get("busqueda_id")
        email_interesado = request.POST.get("email")
        telefono = request.POST.get("telefono")
        nombre = request.POST.get("nombre")
        nombre_perro = request.POST.get("nombre_perro")
        email_autor = request.POST.get("email_autor")
        asunto = "Nueva persona con información"
        mensaje = f"{nombre} tiene información sobre el perro perdido {nombre_perro}. Contacto:\n\nEmail: {email_interesado}\nTeléfono: {telefono}\nNombre: {nombre}"
        remitente = settings.EMAIL_HOST_USER
        destinatario = [email_autor]
        send_mail(asunto, mensaje, remitente, destinatario)
        if request.user.is_authenticated:
            agregar_usuario_tiene_informacion_busqueda(busqueda_id, request.user.cliente)
        messages.success(request, "Tus datos fueron enviados al autor de la publicación. Aguarda su respuesta!")
        return redirect("listar_publicaciones_de_busquedas")
    return redirect("listar_publicaciones_de_busquedas")


@login_required
def marcar_como_encontrado(request, busqueda_id):
    se_encontro(busqueda_id)
    messages.success(request, "Publicación marcada como encontrado con exito!")
    return redirect("mis_busquedas")


@login_required
def eliminar_busqueda(request, busqueda_id):
    eliminar_publicacion_busqueda(busqueda_id)
    messages.success(request, "Publicación eliminada con exito!")
    return redirect("mis_busquedas")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import folium  # para los mapas
from OhMyDog.modelos.clientes import (
    Cliente,
    deshabilitar_cliente,
    perros_cliente,
    perros_habilitados_cliente,
    buscar_clientes_contienen_mail,
)
from OhMyDog.modelos.perros import (
    buscar_perro_por_nombre_y_dueño,
    registrar_perro,
    Perro,
    deshabilitar_perro,
)
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones import (
    filtrar_adopciones_por_cliente,
    agregar_adopcion,
    agregar_busqueda,
    buscar_adopcion_por_nombre_y_cliente,
    buscar_busqueda_por_nombre_archivo_y_cliente,
    listar_adopciones,
    adoptar,
    se_encontro,
    eliminar_publicacion_adopcion,
    eliminar_publicacion_busqueda,
    filtrar_busquedas_por_cliente,
    listar_busquedas_por_zona,
    todos_los_paseadores,
    todos_los_cuidadores,
    agregar_paseador_cuidador,
    buscar_paseador_cuidador_por_email,
)
from OhMyDog.views.auth import user_passes_test, superuser_check
from django.contrib import messages
from OhMyDog.modelos.turnos import filtrar_turnos_por_cliente
from datetime import date
from decimal import Decimal
from OhMyDog.models import modificar_mail
from OhMyDog.views.utils import agregar_mensaje_error


def listar_clientes(request):
    email = request.GET.get("email", "")
    clientes = buscar_clientes_contienen_mail(email)
    return render(request, "listado_clientes.html", {"clientes": clientes})


@login_required
def mis_datos(request):
    cliente = request.user.cliente
    if request.method == "POST":
        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        if cliente.email == email:
            cliente.nombre = nombre
            cliente.telefono = telefono
            cliente.save()
            messages.success(request, f"Datos modificados correctamente")
            return redirect("mis_datos")
        else:
            try:
                cliente = Cliente.objects.get(email=email)
                agregar_mensaje_error(request, "El mail ingresado ya se encuentra registrado.")
                return redirect("mis_datos")
            except cliente.DoesNotExist:
                modificar_mail(email, request.user.cliente)
                cliente.nombre = nombre
                cliente.telefono = telefono
                cliente.email = email
                cliente.save()
                messages.success(request, f"Datos modificados correctamente")
                return redirect("mis_datos")

    return render(request, "mis_datos.html", {"cliente": request.user.cliente})


@user_passes_test(superuser_check)
def datos_de_un_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "datos_de_un_cliente.html", {"cliente": cliente})


@user_passes_test(superuser_check)
def listar_perros_cliente(request, cliente_id):
    perros = perros_cliente(cliente_id)
    return render(request, "listado_de_perros_cliente.html", {"perros": perros})


@user_passes_test(superuser_check)
def registrar_perro(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        nombre = request.POST.get("nombre_perro")
        raza = request.POST.get("raza")
        peso = request.POST.get("peso")
        peso = Decimal(peso).quantize(Decimal("0.00"))
        sexo = request.POST.get("sexo")
        fecha_de_nacimiento = request.POST.get("fecha_de_nacimiento")
        descripcion = request.POST.get("descripcion")

        perro = buscar_perro_por_nombre_y_dueño(nombre, cliente)

        if perro is None:
            registrar_perro(cliente, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo)
            messages.success(request, "Perro registrado con exito.")
            return redirect("home")
        else:
            agregar_mensaje_error(request, f"Perro {nombre} ya registrado.")
            return redirect(f"/clientes/{cliente.id}/registrar_perro")
    else:
        return render(
            request,
            "agregar_perro.html",
            {"cliente_id": cliente_id, "hoy": date.today().isoformat()},
        )


@user_passes_test(superuser_check)
def borrar_perro(request, perro_id):
    deshabilitar_perro(perro_id)
    messages.success(request, "Perro eliminado con exito.")
    return redirect("clientes")


@user_passes_test(superuser_check)
def borrar_cliente(request, cliente_id):
    deshabilitar_cliente(cliente_id)
    messages.success(request, "Cliente eliminado con exito")
    return redirect("clientes")


@login_required
def mis_perros(request):
    perros = perros_habilitados_cliente(request.user.cliente.id)
    return render(request, "mis_perros.html", {"perros": perros})


@login_required
def mis_turnos(request):
    cliente = request.user.cliente
    turnos = filtrar_turnos_por_cliente(cliente)
    return render(request, "mis_turnos.html", {"turnos": turnos})


@login_required
def datos_de_mi_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    return render(request, "datos_de_mi_perro.html", {"perro": perro})


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


def listar_publicaciones_de_adopciones(request):
    adopciones = listar_adopciones()
    return render(request, "listar_publicaciones_de_adopciones.html", {"adopciones": adopciones})


@login_required
def mis_adopciones(request):
    cliente = request.user.cliente
    adopciones = filtrar_adopciones_por_cliente(cliente)
    return render(request, "mis_adopciones.html", {"adopciones": adopciones})


@login_required
def marcar_como_adoptado(request, adopcion_id):
    adoptar(adopcion_id)
    messages.success(request, "Publicación marcada como adoptada con exito!")
    return redirect("mis_adopciones")


def marcar_como_me_interesa(request):
    if request.method == "POST":
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
        messages.success(request, "Tus datos fueron enviados al autor de la publicación. Aguarda su respuesta!")
        return redirect("listar_publicaciones_de_adopciones")
    return redirect("listar_publicaciones_de_adopciones")


@login_required
def eliminar_adopcion(request, adopcion_id):
    eliminar_publicacion_adopcion(adopcion_id)
    messages.success(request, "Publicación eliminada con exito!")
    return redirect("mis_adopciones")


@login_required
def mis_busquedas(request):
    cliente = request.user.cliente
    busquedas = filtrar_busquedas_por_cliente(cliente)
    return render(request, "mis_busquedas.html", {"busquedas": busquedas})


def listar_publicaciones_de_busquedas(request):
    zona = request.GET.get("zona", "")
    busquedas = listar_busquedas_por_zona(zona)
    return render(request, "listar_publicaciones_de_busquedas.html", {"busquedas": busquedas})


@login_required
def eliminar_busqueda(request, busqueda_id):
    eliminar_publicacion_busqueda(busqueda_id)
    messages.success(request, "Publicación eliminada con exito!")
    return redirect("mis_busquedas")


@login_required
def marcar_como_encontrado(request, busqueda_id):
    se_encontro(busqueda_id)
    messages.success(request, "Publicación marcada como encontrado con exito!")
    return redirect("mis_busquedas")


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
        messages.success(request, "Tus datos fueron enviados al autor de la publicación. Aguarda su respuesta!")
        return redirect("listar_publicaciones_de_busquedas")
    return redirect("listar_publicaciones_de_busquedas")


"""
VIEWS PARA MAPAS
"""


def mapa_inicial():
    # Crear un mapa de Folium centrado en una ubicación específica
    # location=[longitud, latitud]
    return folium.Map(location=[-34.9214, -57.9544], zoom_start=12)


def generar_punto_paseador_cuidador(paseador_cuidador):
    # Agrega un botón dependiendo de la condición
    return folium.Marker(
        location=[float(paseador_cuidador.latitud), float(paseador_cuidador.longitud)],
        popup=f"""<strong>Email:</strong>{paseador_cuidador.email}<br>
            <strong>Nombre:</strong>{paseador_cuidador.nombre}<br>
            <strong>Franja Horaria:</strong>{paseador_cuidador.franja_horaria}
            """,
        tooltip="Haz clic aquí para más detalles",
    )


def cargar_mapa_paseadores():
    paseadores = todos_los_paseadores()

    mi_mapa = mapa_inicial()

    for paseador in paseadores:
        # Agregar un marcador con información personalizada
        generar_punto_paseador_cuidador(paseador).add_to(mi_mapa)

    return mi_mapa._repr_html_()


def cargar_mapa_cuidadores():
    cuidadores = todos_los_cuidadores()

    mi_mapa = mapa_inicial()

    for cuidador in cuidadores:
        # Agregar un marcador con información personalizada
        generar_punto_paseador_cuidador(cuidador).add_to(mi_mapa)

    return mi_mapa._repr_html_()


def visualizar_mapa_paseadores(request):
    return render(request, "visualizar_mapa.html", {"mapa": cargar_mapa_paseadores(), "tipo": "Paseadores"})


def visualizar_mapa_cuidadores(request):
    return render(request, "visualizar_mapa.html", {"mapa": cargar_mapa_cuidadores(), "tipo": "Cuidadores"})


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
            if tipo == "P":
                agregar_mensaje_error(request, f"Paseador {email} ya ha sido agregado con anterioridad!")
            else:
                agregar_mensaje_error(request, f"Cuidador {email} ya ha sido agregado con anterioridad!")

    return render(request, "agregar_paseador_cuidador.html")

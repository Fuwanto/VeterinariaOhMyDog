from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

from OhMyDog.modelos.clientes import agregar_cliente, buscar_cliente_por_mail
from OhMyDog.models import (
    Usuario,
    alternar_primer_acceso,
    buscar_usuario_por_mail,
    actualizar_contraseña,
)
from OhMyDog.views.utils import agregar_mensaje_error, generar_contraseña
from django.contrib.auth.hashers import make_password, check_password


def superuser_check(user):
    return user.is_staff


@user_passes_test(superuser_check)
def registrar_cliente(request):
    if request.method == "GET":
        return render(request, "agregar_cliente.html")

    email = request.POST["email"]
    cliente = buscar_cliente_por_mail(email)
    if cliente is not None:
        agregar_mensaje_error(request, f"El cliente {email} ya existe.")
        return redirect("registrar_cliente")

    nombre = request.POST["nombre"]
    telefono = request.POST["telefono"]
    contraseña = generar_contraseña()
    cliente = agregar_cliente(
        nombre,
        email,
        telefono,
    )
    Usuario.objects.create_user(email, contraseña, cliente)
    send_mail(
        "Contraseña de su cuenta de OhMyDog",
        f"La contraseña autogenerada es: {contraseña}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    messages.success(
        request,
        "Cliente registrado correctamente. Contraseña autogenerada enviada.",
    )
    return redirect("home")


def login_usuario(request):
    if request.method == "GET":
        return render(request, "login.html")

    email = request.POST["email"]
    password = request.POST["contraseña"]
    usuario_solo_por_mail = buscar_usuario_por_mail(email)
    if usuario_solo_por_mail is None:
        agregar_mensaje_error(request, "Usuario no registrado.")
        return redirect("login")
    else:
        usuario = authenticate(request, mail=email, password=password)
        if usuario is None:
            agregar_mensaje_error(request, "Contraseña incorrecta.")
            return redirect("login")
        else:
            if not usuario.habilitado:
                agregar_mensaje_error(request, "Cliente deshabilitado.")
                return redirect("login")
            login(request, usuario)
            if usuario.primer_inicio:
                return redirect("cambiar_contraseña")
            else:
                return redirect("home")


@login_required
def cambiar_contraseña(request):
    if request.method == "POST":
        contraseña_actual_guardada = request.user.password
        contraseña_actual_ingresada = request.POST.get("contraseña_actual")
        contraseña_nueva = request.POST.get("contraseña_nueva")
        contraseña_nueva_repetida = request.POST.get("contraseña_nueva_confirmar")

        if not check_password(contraseña_actual_ingresada, contraseña_actual_guardada):
            agregar_mensaje_error(request, "La contraseña actual ingresada es incorrecta")
            return render(request, "cambiar_contraseña.html")

        if contraseña_nueva == contraseña_actual_ingresada:
            agregar_mensaje_error(request, "La contraseña nueva no puede ser igual a la actual")
            return render(request, "cambiar_contraseña.html")

        if contraseña_nueva != contraseña_nueva_repetida:
            agregar_mensaje_error(request, "Las contraseñas no coinciden")
            return render(request, "cambiar_contraseña.html")

        if contraseña_nueva == request.user.mail or contraseña_nueva == request.user.cliente.telefono:
            agregar_mensaje_error(
                request,
                "La contraseña nueva no puede ser igual a su informacion personal",
            )
            return render(request, "cambiar_contraseña.html")

        if len(contraseña_nueva) < 8:
            agregar_mensaje_error(request, "La contraseña debe tener al menos 8 caracteres")
            return render(request, "cambiar_contraseña.html")

        if contraseña_nueva.isdigit():
            agregar_mensaje_error(request, "La contraseña no puede ser totalmente numerica")
            return render(request, "cambiar_contraseña.html")

        actualizar_contraseña(request.user.id, make_password(contraseña_nueva))
        alternar_primer_acceso(request.user.id)
        messages.success(request, "La contraseña ha sido cambiada correctamente")
        return redirect("login")
    else:
        return render(request, "cambiar_contraseña.html")


@login_required
def logout_usuario(request):
    logout(request)
    return redirect("login")

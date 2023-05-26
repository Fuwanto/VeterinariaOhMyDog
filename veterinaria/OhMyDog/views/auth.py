import string, random

from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

from OhMyDog.modelos.clientes import agregar_cliente, buscar_cliente_por_mail
from OhMyDog.models import Usuario, alternar_primer_acceso


def superuser_check(user):
    return user.is_staff


@user_passes_test(superuser_check)
def register(request):
    if request.method == "GET":
        return render(request, "agregar_cliente.html")

    email = request.POST["email"]
    cliente = buscar_cliente_por_mail(email)
    if cliente is None:
        nombre = request.POST["nombre"]
        telefono = request.POST["telefono"]
        contraseña = "".join(
            random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8
            )
        )
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
        redirect("register")
    else:
        messages.error(request, f"Cliente {email} ya existente.")
        return redirect("register")

    return redirect("home")


def buscar_usuario_por_mail(email):
    try:
        return Usuario.objects.get(mail=email)
    except:
        return None


def login_usuario(request):
    if request.method == "POST":
        mail = request.POST["email"]
        password = request.POST["contraseña"]
        usuario_solo_por_mail = buscar_usuario_por_mail(mail)
        usuario = authenticate(request, mail=mail, password=password)
        if usuario_solo_por_mail is None:
            messages.error(request, "Usuario no registrado")
            return redirect("login")  # redirecciona al login de nuevo

        elif usuario_solo_por_mail and (
            usuario is None
        ):  # quiere decir que la contraseña no coincide
            messages.error(request, "Contraseña incorrecta")
            return redirect("login")  # redirecciona al login de nuevo
        else:
            login(request, usuario)
            if usuario.primer_inicio:
                # Llamar funcion para mostrar cambiar contraseña
                alternar_primer_acceso(usuario.id)
                return redirect("primer_inicio")
            else:
                # Si no es el primer inicio se lo redirecciona al home
                return redirect("home")

    return render(request, "login.html")


@login_required
def primer_inicio(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Tu contraseña ha sido cambiada exitosamente.")
            return redirect("login")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = PasswordChangeForm(request.user)

    context = {"form": form}
    return render(request, "primer_inicio.html", context)


@login_required
def logout_usuario(request):
    logout(request)
    return redirect("home")

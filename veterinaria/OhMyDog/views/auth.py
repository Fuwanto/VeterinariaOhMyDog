from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect

from OhMyDog.modelos.clientes import agregar_cliente, buscar_cliente_por_mail
from OhMyDog.models import Usuario, alternar_primer_acceso, buscar_usuario_por_mail
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
                return redirect("primer_inicio")
            else:
                return redirect("home")


@login_required
def primer_inicio(request):
    if request.method == "POST":
        mail = request.user.mail
        telefono = request.user.cliente.telefono
        contraseña_actual_guardada = request.user.password 
        contraseña_actual_ingresada = request.POST.get("currentPassword")
        contraseña_nueva = request.POST.get("newPassword")
        contraseña_nueva_repetida = request.POST.get("confirmPassword")
        if (not check_password(contraseña_actual_ingresada, contraseña_actual_guardada)):
            messages.add_message(
                request,
                messages.ERROR,
                "La contraseña actual ingresada es incorrecta",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html")
        if (contraseña_nueva == contraseña_actual_ingresada):
            messages.add_message(
                request,
                messages.ERROR,
                "La contraseña nueva no puede ser igual a la actual",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html")
        if (contraseña_nueva != contraseña_nueva_repetida):
            messages.add_message(
                request,
                messages.ERROR,
                "Las contraseñas no coinciden",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html")
        if (contraseña_nueva == mail or contraseña_nueva == telefono):
            messages.add_message(
                request,
                messages.ERROR,
                "La contraseña nueva no puede ser igual a su informacion personal",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html")
        if (len(contraseña_nueva) < 8 ):
            messages.add_message(
                request,
                messages.ERROR,
                "La contraseña debe tener al menos 8 caracteres",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html")          
        if (contraseña_nueva.isdigit()):
            messages.add_message(
                request,
                messages.ERROR,
                "La contraseña no puede ser totalmente numerica",
                extra_tags="danger",
            )
            return render(request, "primer_inicio.html") 
        encrypted_password = make_password(contraseña_nueva)
        request.user.password = encrypted_password
        request.user.save()   
        messages.success(
            request,
            "La contraseña ha sido cambiada correctamente",
        )
        return redirect("home")
    else:
        return render(request, "primer_inicio.html")


@login_required
def logout_usuario(request):
    logout(request)
    return redirect("login")

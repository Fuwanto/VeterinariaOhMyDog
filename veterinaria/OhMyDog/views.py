import string
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from .models import Usuario
from .modelos.clientes import agregar_cliente, buscar_cliente_por_mail, listar_clientes
from django.contrib.auth import logout


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
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
                "Constraseña de su cuenta de OhMyDog",
                f"La contraseña autogenerada es: {contraseña}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(
                request,
                "Tu cuenta ha sido creada exitosamente. Revisa tu correo para obtener tu contraseña.",
            )
        else:
            messages.error(request, f"Cliente {email} ya existente.")

        return redirect("login")

    else:
        return render(request, "register.html")


def login_usuario(request):
    if request.method == "POST":
        mail = request.POST["email"]
        password = request.POST["contraseña"]

        usuario = authenticate(request, mail=mail, password=password)
        if usuario is None:
            messages.error(request, "Datos incorrectos o usuario no existente")
            return redirect("login")  # redirecciona al login de nuevo

        else:
            login(request, usuario)
            if usuario.primer_inicio:
                # Llamar funcion para mostrar cambiar contraseña
                alternar_primer_acceso(usuario.id)
            else:
                # Si no es el primer inicio se lo redirecciona al home
                return redirect("home")

    return render(request, "login.html")


def logout_usuario(request):
    logout(request)
    return redirect("home")


def alternar_primer_acceso(id):
    usuario = Usuario.objects.get(id=id)
    usuario.primer_inicio = False
    usuario.save()


# def test_view(request):
#    clientes = listar_clientes()
#    return render(request, "test.html", {"clientes": clientes})

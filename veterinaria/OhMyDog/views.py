import string
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from .models import Usuario
from. models import UsuarioManager
from .modelos.clientes import agregar_cliente, buscar_cliente_por_mail, listar_clientes
from django.contrib.auth import logout


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        cliente =  buscar_cliente_por_mail(email)
        if cliente is None:            
            nombre = request.POST['nombre']
            telefono = request.POST['telefono']    
            contraseña = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
            cliente = agregar_cliente(nombre, email, telefono, )
            usuario = Usuario.objects.create_user(email, contraseña, cliente)
            send_mail(
                   "Constraseña de su cuenta de OhMyDog",
                   f"La contraseña autogenerada es: {contraseña}",
                   settings.EMAIL_HOST_USER,
                   ["nahucapara@gmail.com"],
                   fail_silently=False,
                    )
            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Revisa tu correo para obtener tu contraseña.')
        else:
            messages.error(request, f'Cliente {email} ya existente.')
        
        return redirect('login')
            
    else:
        return render(request, "register.html")
    
def login_usuario(request):
    if request.method == 'POST':
        mail = request.POST['email']
        password = request.POST['contraseña']
        send_mail(
                   "Constraseña de su cuenta de OhMyDog",
                   f"La contraseña autogenerada es: {password} {mail}",
                   settings.EMAIL_HOST_USER,
                   ["nahucapara@gmail.com"],
                   fail_silently=False,
                    )
        usuario = authenticate(request, mail=mail, password=password)    
        # despues habria que chequear la constraseña y eso. Igual creo que se puede hacer mejor
        # no se como hacer para que ande esto, creo que hace el login pero no se es raro
        # faltaria el logout tambien
        if usuario is not None:

            login(request, usuario) # esto es algo de django pero no lo pude usar
            if usuario.primer_inicio:
                #Mostrar cambiar contraseña
                alternar_primer_acceso(usuario.id)
            
            return redirect('home') # redirige a la página principal del sitio

        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos')
    
    return render(request, 'login.html')


def logout_usuario (request):
    logout(request)
    return redirect('home')

def alternar_primer_acceso(id):
    usuario = Usuario.objects.get(id = id)
    usuario.primer_inicio = False
    usuario.save()
#def test_view(request):
#    clientes = listar_clientes()
#    return render(request, "test.html", {"clientes": clientes})

import string
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail

from .modelos.clientes import agregar_cliente, comprobar_que_no_exista, alternar_primer_acceso, listar_clientes



def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        cliente = comprobar_que_no_exista(email)
        if cliente is None:            
            nombre = request.POST['nombre']
            telefono = request.POST['telefono']    
            contraseña = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
            agregar_cliente(nombre, email, telefono, contraseña,True)
            send_mail(
                   "Constraseña de su cuenta de OhMyDog",
                   f"La contraseña autogenerada es: {contraseña}",
                   settings.EMAIL_HOST_USER,
                   [email],
                   fail_silently=False,
                    )
            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Revisa tu correo para obtener tu contraseña.')
        else:
            messages.error(request, f'Cliente {email} ya existente.')
        
        return redirect('login')
            
    else:
        return render(request, "register.html")
    
def login_cliente(request):
    if request.method == 'POST':
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        cliente = comprobar_que_no_exista(email)
        
        # despues habria que chequear la constraseña y eso. Igual creo que se puede hacer mejor
        # no se como hacer para que ande esto, creo que hace el login pero no se es raro
        # faltaria el logout tambien
        if cliente is not None:
            ##user = authenticate(name=email,password=contraseña)
            login(request, cliente) # esto es algo de django pero no lo pude usar
            if cliente.primerInicio:
                #Mostrar cambiar contraseña
                alternar_primer_acceso(cliente.id)
            
            return redirect('home') # redirige a la página principal del sitio

        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos')
    
    return render(request, 'login.html')

#def test_view(request):
#    clientes = listar_clientes()
#    return render(request, "test.html", {"clientes": clientes})

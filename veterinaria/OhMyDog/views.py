import string
import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .modelos.clientes import agregar_cliente, comprobar_que_no_exista
from .modelos.clientes import listar_clientes


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        cliente = comprobar_que_no_exista(email)
        if cliente is None:            
            nombre = request.POST['nombre']
            telefono = request.POST['telefono']
            contraseña = "contraseña"
            #######LO QUE ESTA ENCERRADO ACA ES PARA EL ENVIO DE LA CONSTRASEÑA AUTOGENERADA, PERO TODAVIA NO TENEMOS 
            #UN GMAIL DE LA VETERINARIA, POR LO QUE LA CONTRASEÑA ES "contraseña" para todos#######
            
            #contraseña = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
            # enviar el mail para que pueda cambiar la contraseña (no busque como hacer para que el primer login sea 
            # diferente al resto, para el tema de cambiar la contraseña. De momento podría hacerlo yendo al apartado de 
            # modificar mis datos, cuando este)
            #send_mail("Constraseña de su cuenta de OhMyDog", f"La contraseña autogenerada es: {contraseña}",
            #          settings.EMAIL_HOST_USER, email, fail_silently=False)
            #######################################################
            agregar_cliente(nombre, email, telefono, contraseña)
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
            #login(request, cliente) # esto es algo de django pero no lo pude usar

            return redirect('home') # redirige a la página principal del sitio
        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos')
    
    return render(request, 'login.html')

#def test_view(request):
#    clientes = listar_clientes()
#    return render(request, "test.html", {"clientes": clientes})

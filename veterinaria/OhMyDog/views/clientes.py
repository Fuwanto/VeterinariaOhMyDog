from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from OhMyDog.modelos.clientes import listar_clientes, Cliente
from OhMyDog.modelos.perros import buscar_perros_por_dueño, buscar_perro_por_nombre, registrar_perro
from OhMyDog.views.auth import user_passes_test, superuser_check
from django.contrib import messages

def buscar_clientes(request):
    email = request.GET.get('email', '')
    cliente = Cliente.objects.filter(email__icontains=email)
    return render(request, 'listado_clientes.html', {"clientes": cliente})


def todos_los_clientes(request):
    clientes = listar_clientes()
    return render(request, "listado_clientes.html", {"clientes": clientes})

@login_required
def mis_datos(request):
    cliente = request.user.cliente
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        
        # Actualizar los datos del cliente
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.save()
        
        return redirect('mis_datos') 
    
    return render(request, 'mis_datos.html', {"cliente": request.user.cliente})


@user_passes_test(superuser_check)
def datos_de_un_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'datos_de_un_cliente.html', {'cliente': cliente})

@user_passes_test(superuser_check)
def listado_de_perros_cliente(request, cliente_id):
    return 

@user_passes_test(superuser_check)
def agregar_perro(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        nombre = request.POST.get("nombre_perro")
        if nombre:
            raza = request.POST.get("raza")
            peso = request.POST.get("peso")
            sexo = request.POST.get("sexo")
            fecha_de_nacimiento = request.POST.get("fecha_de_nacimiento")
            descripcion = request.POST.get("descripcion")
            print(nombre, raza, peso, sexo, fecha_de_nacimiento, descripcion)
            registrar_perro(cliente, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo)
            messages.success(request, "Perro registrado con exito.")
    else:
        messages.error(request, f"Perro  ya existente.")
    return render(request, 'agregar_perro.html', {"cliente_id": cliente_id})


@login_required
def mis_perros(request):
    cliente = request.user.cliente
    perros = buscar_perros_por_dueño(cliente)
    return render(request, 'mis_perros.html', {"perros": perros})

@login_required
def mis_turnos(request):
    return render(request, "mis_turnos.html", {"cliente": request.user.cliente})
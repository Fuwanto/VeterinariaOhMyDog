from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from OhMyDog.modelos.clientes import listar_clientes


def todos_los_clientes(request):
    clientes = listar_clientes()
    return render(request, "test.html", {"clientes": clientes})

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

@login_required
def mis_perros(request):
    return render(request, "mis_perros.html", {"cliente": request.user.cliente})

@login_required
def mis_turnos(request):
    return render(request, "mis_turnos.html", {"cliente": request.user.cliente})
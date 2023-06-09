from OhMyDog.views.auth import user_passes_test, superuser_check
from OhMyDog.modelos.perros import buscar_perro_por_id, modificar_datos
from django.shortcuts import render
from OhMyDog.modelos.atenciones import buscar_atenciones_por_perro


@user_passes_test(superuser_check)
def datos_de_un_perro(request, perro_id):
    perro = buscar_perro_por_id(perro_id)
    peso = request.POST.get("peso")
    if request.method == "POST" and peso:
        descripcion = request.POST.get("descripcion")
        modificar_datos(perro_id, peso, descripcion)

    return render(request, "datos_de_un_perro.html", {"perro": perro})

def atenciones_de_un_perro_cliente (request):
    perro_id = request.POST.get("perro_id")
    print (perro_id)
    perro = buscar_perro_por_id(perro_id)
    atenciones = buscar_atenciones_por_perro(perro)
    context = {
        'atenciones': atenciones
    }

    return render(request, "listado_de_atenciones_por_perro_cliente.html", context)

def atenciones_de_un_perro_veterinario(request):
    perro_id = request.GET.get("perro")
    print(perro_id)
    perro = buscar_perro_por_id(perro_id)
    atenciones = buscar_atenciones_por_perro(perro)
    context = {
        'atenciones': atenciones,
        'perro' : perro
    }
    print(buscar_atenciones_por_perro(perro))
    return render(request, "listado_de_atenciones_por_perro.html", context)




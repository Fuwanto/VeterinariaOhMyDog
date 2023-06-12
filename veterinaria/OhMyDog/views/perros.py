from OhMyDog.views.auth import user_passes_test, superuser_check
from OhMyDog.modelos.perros import buscar_perro_por_id, modificar_datos
from django.shortcuts import render
from OhMyDog.modelos.atenciones import buscar_atenciones_por_perro
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion


@user_passes_test(superuser_check)
def datos_de_un_perro(request, perro_id):
    perro = buscar_perro_por_id(perro_id)
    peso = request.POST.get("peso")
    if request.method == "POST" and peso:
        descripcion = request.POST.get("descripcion")
        modificar_datos(perro_id, peso, descripcion)

    return render(request, "datos_de_un_perro.html", {"perro": perro})

def atenciones_de_un_perro_cliente (request):
    if request.method == 'POST':
        perro_id = request.POST.get("perro_id")
        perro = buscar_perro_por_id(perro_id)
        atenciones = buscar_atenciones_por_perro(perro)
    else:
        perro_id = request.GET.get("perro_id")
        perro = buscar_perro_por_id(perro_id)
        atencion_filtro = request.GET.get("atencion_filtro")
        fecha_filtro = request.GET.get("fecha_filtro")
        atenciones = buscar_atenciones_por_perro(perro)
        if not atencion_filtro is "":
            TipoDeAtencion.objects.get(id = atencion_filtro)
            atenciones = atenciones.filter(tipo_atencion = atencion_filtro )
        if not fecha_filtro is "":
            atenciones = atenciones.filter(fecha = fecha_filtro)
    tipos_atencion = TipoDeAtencion.objects.all()
    context = {
    'atenciones': atenciones,
    'tipo_atencion': tipos_atencion,
    'perro': perro
    }

    return render(request, "listado_de_atenciones_por_perro_cliente.html", context)

def atenciones_de_un_perro_veterinario(request):
    if request.method == 'POST':
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        atenciones = buscar_atenciones_por_perro(perro)
    else:
        perro_id = request.GET.get("perro")
        print(perro_id)
        perro = buscar_perro_por_id(perro_id)
        atencion_filtro = request.GET.get("atencion_filtro")
        fecha_filtro = request.GET.get("fecha_filtro")
        atenciones = buscar_atenciones_por_perro(perro)
        if not atencion_filtro is "" and not atencion_filtro is None:
            TipoDeAtencion.objects.get(id = atencion_filtro)
            atenciones = atenciones.filter(tipo_atencion = atencion_filtro )
        if not fecha_filtro is "" and not atencion_filtro is None:
            atenciones = atenciones.filter(fecha = fecha_filtro)
    tipos_atencion = TipoDeAtencion.objects.all()
    context = {
    'atenciones': atenciones,
    'tipo_atencion': tipos_atencion,
    'perro': perro
    }
    return render(request, "listado_de_atenciones_por_perro.html", context)




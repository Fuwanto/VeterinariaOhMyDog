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


def atenciones_de_un_perro_cliente(request):
    context = atenciones_de_un_perro(request)   
    return render(request, "listado_de_atenciones_por_perro_cliente.html", context)

def atenciones_de_un_perro_veterinario(request):
    context = atenciones_de_un_perro(request)
    return render(request, "listado_de_atenciones_por_perro.html", context)

def atenciones_de_un_perro(request):
    perro_id = request.GET.get("perro")
    perro = buscar_perro_por_id(perro_id)
    atenciones = buscar_atenciones_por_perro(perro)
    tipos_atencion = TipoDeAtencion.objects.all()
    return {"atenciones": atenciones, "tipo_atencion": tipos_atencion, "perro": perro}

def filtrar_listado_atenciones_cliente(request):
    context = filtrar_listado_atenciones(request)
    return render(request, "listado_de_atenciones_por_perro_cliente.html", context)

def filtrar_listado_atenciones_veterinario(request):
    context = filtrar_listado_atenciones(request)
    return render(request, "listado_de_atenciones_por_perro.html", context)

def filtrar_listado_atenciones(request):
    perro_id = request.GET.get("perro")
    perro = buscar_perro_por_id(perro_id)
    atenciones = buscar_atenciones_por_perro(perro)
    seleccion_tipo_atencion = request.GET.get("atencion_filtro")
    seleccion_fecha = request.GET.get("fecha_filtro")
    if seleccion_tipo_atencion != "" and seleccion_tipo_atencion is not None:
        tipo_atencion = TipoDeAtencion.objects.get(nombre = seleccion_tipo_atencion)
        atenciones = atenciones.filter(tipo_atencion=tipo_atencion)
    if seleccion_fecha != "" and seleccion_fecha is not None:
        atenciones = atenciones.filter(fecha=seleccion_fecha)
    tipos_atencion = TipoDeAtencion.objects.all()
    return {"atenciones": atenciones, "tipo_atencion": tipos_atencion, "perro": perro, 
            "seleccion_tipo_atencion": seleccion_tipo_atencion, "seleccion_fecha": seleccion_fecha}

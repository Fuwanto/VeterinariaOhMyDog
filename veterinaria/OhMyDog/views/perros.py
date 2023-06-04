from OhMyDog.views.auth import user_passes_test, superuser_check
from OhMyDog.modelos.perros import buscar_perro_por_id, modificar_datos
from django.shortcuts import render


@user_passes_test(superuser_check)
def datos_de_un_perro(request, perro_id):
    perro = buscar_perro_por_id(perro_id)
    peso = request.POST.get("peso")
    if request.method == "POST" and peso:
        descripcion = request.POST.get("descripcion")
        modificar_datos(perro_id, peso, descripcion)

    return render(request, "datos_de_un_perro.html", {"perro": perro})

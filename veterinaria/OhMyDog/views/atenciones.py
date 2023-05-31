from django.shortcuts import render, redirect, get_object_or_404
from OhMyDog.modelos.perros import buscar_perro_por_id
from OhMyDog.modelos.atenciones import agregar_atencion_clinica_init
from datetime import datetime, date

def agregar_atencion_clinica(request):
    perro = None
    perro_id = None
    if request.method == 'GET':
        perro_id = request.GET.get('perro')
        print('GET', perro_id)
        perro = buscar_perro_por_id(perro_id)
        print(perro)
    if request.method == 'POST':
        fecha = request.POST.get('fecha_de_atencion')     
        observacion = request.POST.get('observacion')
        perro_id = request.POST.get('perro')
        print('POST', perro_id)
        print('LALALALALA',fecha)
        perro = buscar_perro_por_id(perro_id)
        agregar_atencion_clinica_init(perro, fecha, observacion)
        
    context = {
        'perro': perro
    }
    return render (request, 'agregar_atencion_clinica.html', context)
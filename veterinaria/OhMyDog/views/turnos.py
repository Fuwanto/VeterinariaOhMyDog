from django.shortcuts import render
from OhMyDog.modelos.turnos import solicitar_turno

def solicitar_turnos(request):
    tipos_de_atenciones = [1,2,3]
    if request.method == 'GET':
        render(request, "solicitar_turno.html",{'tipos_de_atenciones': tipos_de_atenciones})
    if request.method == 'POST':
        fecha_solicitud = request.POST['fecha_solicitud']
        tipo_atencion = request.POST['tipo_atencion_id']
        solicitar_turno(request.user.cliente, fecha_solicitud, 1, tipo_atencion, " ")
    return render(request, "solicitar_turno.html",{'tipos_de_atenciones': tipos_de_atenciones})
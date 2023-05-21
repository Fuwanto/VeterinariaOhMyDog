from django.shortcuts import render

def solicitudes_de_turnos(request):
    return render(request, "solicitudes_de_turnos.html")
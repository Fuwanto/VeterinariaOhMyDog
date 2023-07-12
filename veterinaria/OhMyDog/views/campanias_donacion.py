from django.shortcuts import render, redirect
from django.contrib import messages
from OhMyDog.modelos.publicaciones import (
    crear_campania,
    listar_campanias_de_donaciones_actualizadas,
    terminar_campania,
    obtener_campania_por_id,
    actualizar_fecha_fin_campania,
    existe_donacion_nombre,
    buscar_transaccion_por_id,
    grabar_transaccion,
    actualizar_monto_campania,
    grabar_descuento,
)
import requests
from OhMyDog.views.utils import agregar_mensaje_error
from datetime import datetime, date, timedelta
import datetime
import mercadopago
from django.conf import settings
from django.http import JsonResponse
import qrcode
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

def agregar_campania_donacion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        objetivo = request.POST.get("objetivo")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        monto = request.POST.get("monto")
        if fecha_fin <= fecha_inicio:
            agregar_mensaje_error(request, f"La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
            return redirect("agregar_campania_donacion")

        if existe_donacion_nombre(nombre):
            agregar_mensaje_error(request, f"Campaña con nombre: {nombre}, ya creada.")
            return redirect("agregar_campania_donacion")

        crear_campania(nombre, objetivo, monto, fecha_inicio, fecha_fin)
        messages.success(request, "Campaña agregada con exito.")
        return redirect("home")
    else:
        mañana = date.today() + timedelta(days=1)
        context = {
            "mañana": mañana.strftime("%Y-%m-%d"),
        }
        return render(request, "agregar_campania_donacion.html", context)


def listar_campanias_de_donaciones(request):
    return render(
        request, "listar_campanias_de_donaciones.html", {"campanias": listar_campanias_de_donaciones_actualizadas()}
    )


def terminar_campania_donacion(request, campania_id):
    terminar_campania(campania_id)
    return redirect("listar_campanias_de_donaciones")


def modificar_fecha_fin_campania(request):
    campania_id = request.POST.get("campania_id")
    nueva_fecha_fin_str = request.POST.get("nueva_fecha_fin")
    nueva_fecha_fin = datetime.strptime(nueva_fecha_fin_str, "%Y-%m-%d").date()
    campania = obtener_campania_por_id(campania_id)
    if nueva_fecha_fin <= campania.fecha_inicio:
        agregar_mensaje_error(request, f"La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
        return redirect("listar_campanias_de_donaciones")
    actualizar_fecha_fin_campania(campania_id, nueva_fecha_fin)
    messages.success(request, "Fecha de fin de la campaña modificada con éxito.")
    return redirect("listar_campanias_de_donaciones")


def realizar_donacion(request):
    campania_id = request.POST.get("campania_id")
    print(request.POST.get("campania_id"))
    campania = obtener_campania_por_id(campania_id)
    return render (request, "realizar_donacion.html",{"campania": campania, "controlBit": False})

def cambiar_codigo_qr(request, campania_id, value, email):
    print(email)
    mp = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)    
    cliente_email = email
    if request.user.is_authenticated:
        cliente_email = request.user.mail
    preference_data = {
        "items": [
            {
                "title": "Transacción",
                "quantity": 1,
                "currency_id": "ARS",  # Puedes cambiar esto según tu moneda
                "unit_price": value,  # Monto de la transacción
            }
        ],
        "notification_url": f"https://7c8f-190-188-17-13.ngrok-free.app/notificacion_mercadopago/?campania_id={campania_id}&monto={value}&email={cliente_email}",
    }
    preference_result = mp.preference().create(preference_data)
    if preference_result["status"] == 201:
        qr_code_url = preference_result["response"]["init_point"]
        qr_image = qrcode.make(qr_code_url)
        response = HttpResponse(content_type='image/png')
        qr_image.save(response, 'PNG')
        return response

    else:
        return JsonResponse({"error": "No se pudo generar el pago QR."}, status=500)

@csrf_exempt
def notificacion_mercadopago (request):
    type = request.GET.get('type')
    data_id = request.GET.get('data.id')
    payment_id = request.GET.get('data.id')  # O donde se encuentre el ID del pago QR en tu caso
    estado = obtener_estado_pago_qr(payment_id)
    print(estado)
    if type == 'payment':
        if buscar_transaccion_por_id (data_id) is None:
            campania_id = request.GET.get('campania_id')
            value = request.GET.get('monto')
            email =  request.GET.get('email')
            grabar_transaccion (data_id, value, campania_id)
            actualizar_monto_campania(campania_id, value)
            grabar_descuento (email)
            messages.success(request, 'La transacción se completó exitosamente.')
    response = HttpResponse("Exito")
    response.status_code = 200
    return response


# Funciones generales y útiles que se usan en muchos lugares
from django.contrib import messages
import random, string
from datetime import datetime


def agregar_mensaje_error(request, mensaje):
    messages.add_message(
        request,
        messages.ERROR,
        mensaje,
        extra_tags="danger",
    )


def generar_contraseña():
    return "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))


def calcular_cantidad_meses(fecha_seleccionada):
    fecha_actual = datetime.now()

    partes = fecha_seleccionada.split("-")
    anio_seleccionado = int(partes[0])
    mes_seleccionado = int(partes[1])

    anio_actual = fecha_actual.year
    mes_actual = fecha_actual.month
    cantidad_meses = ((anio_actual - anio_seleccionado) * 12) + (mes_actual - mes_seleccionado)

    return cantidad_meses

# Funciones generales y útiles que se usan en muchos lugares
from django.contrib import messages
import random, string


def agregar_mensaje_error(request, mensaje):
    messages.add_message(
        request,
        messages.ERROR,
        mensaje,
        extra_tags="danger",
    )


def generar_contraseña():
    return "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8
        )
    )

# Funciones generales y útiles que se usan en muchos lugares
from django.contrib import messages


def agregar_mensaje_error(request, mensaje):
    messages.add_message(
        request,
        messages.ERROR,
        mensaje,
        extra_tags="danger",
    )

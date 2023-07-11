from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime, timedelta, date
from OhMyDog.modelos.publicaciones import (
    cliente_tiene_cruza_nombre,
    agregar_cruza,
    cruzas_del_cliente,
    eliminar_cruza,
    buscar_candidatos,
    buscar_cruza_por_id,
    hay_interes_mutuo,
    agregar_interes_cruza,
)
from OhMyDog.views.utils import agregar_mensaje_error, calcular_cantidad_meses


@login_required
def mis_cruzas(request):
    cliente = request.user.cliente
    cruzas = cruzas_del_cliente(cliente)
    return render(request, "mis_cruzas.html", {"cruzas": cruzas})


@login_required
def agregar_publicacion_cruza(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        sexo = request.POST.get("sexo")
        raza = request.POST.get("raza")
        edad_meses = calcular_cantidad_meses(request.POST.get("edad_meses"))
        ultimo_celo = request.POST.get("ultimo_celo")
        peso = request.POST.get("peso")
        color = request.POST.get("color")
        antecedentes_salud = request.POST.get("antecedentes_salud")
        foto = request.FILES["foto"]
        cliente = request.user.cliente

        if sexo == "H":
            if calcular_cantidad_meses(ultimo_celo) > edad_meses:
                agregar_mensaje_error(request, f"La fecha del ultimo celo no puede ser mayor a la edad!")
                return redirect("agregar_publicacion_cruza")

        if cliente_tiene_cruza_nombre(cliente, nombre):
            agregar_mensaje_error(request, f"El nombre {nombre} ya se encuentra asociado a otra publicación!")
            return redirect("agregar_publicacion_cruza")
        else:
            agregar_cruza(cliente, nombre, sexo, raza, edad_meses, peso, color, antecedentes_salud, foto, ultimo_celo)
            messages.success(request, "Publicación agregada con exito!")
            return redirect("mis_cruzas")
    else:
        edad_minima = datetime.now() - timedelta(days=180)  # 180 días equivalen a 6 meses
        return render(
            request,
            "agregar_publicacion_cruza.html",
            {"edad_minima_meses": edad_minima.strftime("%Y-%m"), "hoy": date.today().isoformat()},
        )


@login_required
def listar_candidatos(request, cruza_id):
    cruza_seleccionada = buscar_cruza_por_id(cruza_id)
    candidatos = buscar_candidatos(cruza_seleccionada, request.user.cliente)
    context = {"candidatos": candidatos, "cruza_seleccionada": cruza_seleccionada, "cliente": request.user.cliente}
    return render(request, "listar_candidatos.html", context=context)


@login_required
def eliminar_publicacion_cruza(request, cruza_id):
    eliminar_cruza(cruza_id)
    messages.success(request, "Publicación eliminada con exito!")
    return redirect("mis_cruzas")


@login_required
def seleccionar_candidato(request):
    if request.method == "POST":
        cruza_de_interes = buscar_cruza_por_id(request.POST.get("cruza_id"))
        cruza_seleccionada = buscar_cruza_por_id(request.POST.get("cruza_seleccionada_id"))
        agregar_interes_cruza(cruza_seleccionada, cruza_de_interes)
        if hay_interes_mutuo(cruza_seleccionada, cruza_de_interes):
            cliente_de_interes = cruza_de_interes.cliente
            mensaje_para_el_interesado = f"""{cliente_de_interes.nombre} y tú tienen interes mutuo en 
                cruzar a {cruza_seleccionada.nombre} con {cruza_de_interes.nombre}. 
                Contacto de {cliente_de_interes.nombre}:\n\nEmail: 
                {cliente_de_interes.email}\nTeléfono: {cliente_de_interes.telefono}\n
            """
            cliente_interesado = cruza_seleccionada.cliente
            mensaje_para_el_de_interes = f"""{cliente_interesado.nombre} y tú tienen interes mutuo en 
                cruzar a {cruza_seleccionada.nombre} con {cruza_de_interes.nombre}. 
                Contacto de {cliente_interesado.nombre}:\n\nEmail: 
                {cliente_interesado.email}\nTeléfono: {cliente_interesado.telefono}\n
            """
            remitente = settings.EMAIL_HOST_USER
            asunto = f"Ha habido match entre {cruza_seleccionada.nombre} y {cruza_de_interes.nombre}"
            send_mail(asunto, mensaje_para_el_interesado, remitente, [cliente_interesado.email])
            send_mail(asunto, mensaje_para_el_de_interes, remitente, [cliente_de_interes.email])
            messages.success(request, "Ha habido interés mutuo! Te hemos enviado un email.")
        else:
            messages.success(request, "Candidato seleccionado con exito! Si hay interés mutuo te avisaremos por email!")
    return redirect("mis_cruzas")

from django.shortcuts import get_object_or_404
from OhMyDog.modelos.publicaciones.adopciones import Adopcion, UsuarioInteresaAdopcion
from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.publicaciones.busquedas import Busqueda, UsuarioTieneInformacionBusqueda
from OhMyDog.modelos.publicaciones.cruzas import Cruza
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones.paseadores_cuidadores import PaseadorCuidador
from OhMyDog.modelos.publicaciones.donaciones import Donacion, Transaccion, Descuento
from datetime import date, timedelta
import decimal


"""
        ADOPCIONES
"""


def filtrar_adopciones_por_cliente(cliente):
    return Adopcion.objects.filter(cliente=cliente)


def buscar_adopcion_por_nombre_y_cliente(cliente, nombre):
    try:
        return Adopcion.objects.get(cliente=cliente, nombre=nombre)
    except:
        return None


def agregar_adopcion(cliente, nombre, descripcion, tamanio_perro_id, etapa_vida_perro_id, sexo, castrado):
    tamanio_perro = TamanioPerro.objects.get(id=tamanio_perro_id)
    etapa_vida_perro = EtapaVidaPerro.objects.get(id=etapa_vida_perro_id)
    adopcion = Adopcion(
        cliente=cliente,
        nombre=nombre,
        descripcion=descripcion,
        tamanio_perro=tamanio_perro,
        etapa_vida_perro=etapa_vida_perro,
        sexo=sexo,
        castrado=castrado,
    )
    adopcion.save()
    return adopcion


def listar_todas_adopciones():
    return Adopcion.objects.all()


def listar_adopciones_no_mias(cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return Adopcion.objects.exclude(cliente=cliente)


def adoptar(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.adoptado = True
    adopcion.save()


def eliminar_publicacion_adopcion(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.delete()


def usuario_tiene_interes_adopcion(adopcion, cliente):
    try:
        return UsuarioInteresaAdopcion.objects.get(adopcion=adopcion, cliente=cliente)
    except UsuarioInteresaAdopcion.DoesNotExist:
        return None


def agregar_usuario_interesa(adopcion_id, cliente):
    adopcion = Adopcion.objects.get(id=adopcion_id)
    usuario_interesa_adopcion = UsuarioInteresaAdopcion(adopcion=adopcion, cliente=cliente)
    usuario_interesa_adopcion.save()


"""
        BUSQUEDAS
"""


def agregar_busqueda(cliente, nombre, descripcion, zona, foto):
    busqueda = Busqueda(
        cliente=cliente,
        nombre=nombre,
        descripcion=descripcion,
        zona=zona,
        foto=foto,
    )
    busqueda.save()
    return busqueda


def filtrar_busquedas_por_cliente(cliente):
    return Busqueda.objects.filter(cliente=cliente)


def listar_busquedas_por_zona(zona):
    return Busqueda.objects.filter(zona__icontains=zona)


def listar_busquedas_no_mias_y_por_zona(cliente_id, zona):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return Busqueda.objects.filter(zona__icontains=zona).exclude(cliente=cliente)


def eliminar_publicacion_busqueda(busqueda_id):
    busqueda = get_object_or_404(Busqueda, id=busqueda_id)
    busqueda.delete()


def se_encontro(busqueda_id):
    busqueda = get_object_or_404(Busqueda, id=busqueda_id)
    busqueda.encontrado = True
    busqueda.save()


def buscar_busqueda_por_nombre_archivo_y_cliente(cliente, nombre_archivo):
    try:
        return Busqueda.objects.get(cliente=cliente, foto__contains=nombre_archivo)
    except:
        return None


def usuario_tiene_informacion_busqueda(busqueda, cliente):
    try:
        return UsuarioTieneInformacionBusqueda.objects.get(busqueda=busqueda, cliente=cliente)
    except UsuarioTieneInformacionBusqueda.DoesNotExist:
        return None


def agregar_usuario_tiene_informacion_busqueda(busquedaId, cliente):
    busqueda = Busqueda.objects.get(id=busquedaId)
    usuario_busqueda = UsuarioTieneInformacionBusqueda(busqueda=busqueda, cliente=cliente)
    usuario_busqueda.save()


"""
        PASEADORES | Cuidadores
"""


def todos_los_paseadores():
    return PaseadorCuidador.objects.filter(tipo="P")


def todos_los_cuidadores():
    return PaseadorCuidador.objects.filter(tipo="C")


def agregar_paseador_cuidador(nombre, email, latitud, longitud, franja_horaria, tipo):
    paseador_cuidador = PaseadorCuidador(
        nombre=nombre, email=email, latitud=latitud, longitud=longitud, franja_horaria=franja_horaria, tipo=tipo
    )
    paseador_cuidador.save()
    return


def buscar_paseador_cuidador_por_email(email):
    try:
        return PaseadorCuidador.objects.get(email=email)
    except:
        return None


def existe_paseador_cuidador_mail(email):
    try:
        paseador_cuidador = PaseadorCuidador.objects.get(email=email)
        return True
    except:
        return False


def eliminar_paseador_cuidador(paseador_cuidador_id):
    paseador_cuidador = get_object_or_404(PaseadorCuidador, id=paseador_cuidador_id)
    paseador_cuidador.delete()


"""
        Donaciones
"""


def buscar_campania_por_nombre(otroNombre):
    try:
        return Donacion.objects.get(nombre=otroNombre)
    except Donacion.DoesNotExist:
        return None


def existe_donacion_nombre(nombre):
    try:
        donacion = Donacion.objects.get(nombre=nombre)
        return True
    except:
        return False


def crear_campania(nombre, objetivo, monto_objetivo, fecha_inicio, fecha_fin):
    donacion = Donacion(
        nombre=nombre, objetivo=objetivo, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, monto_objetivo=monto_objetivo
    )
    donacion.save()


def listar_campanias_de_donaciones_todas():
    return Donacion.objects.all()


def listar_campanias_de_donaciones_actualizadas():
    campañas = Donacion.objects.all()
    mañana = date.today() + timedelta(days=1)
    for campaña in campañas:
        progreso = (campaña.monto_recaudado / campaña.monto_objetivo) * 100
        campaña.progreso = round(progreso,1)

        if campaña.fecha_fin <= mañana:
            campaña.activa = False
    return campañas


def terminar_campania(campania_id):
    campania = get_object_or_404(Donacion, id=campania_id)
    campania.activa = False
    campania.save()


def obtener_campania_por_id(campania_id):
    try:
        return Donacion.objects.get(id=campania_id)
    except Donacion.DoesNotExist:
        return None


def actualizar_fecha_fin_campania(campania_id, nueva_fecha_fin):
    campania = Donacion.objects.get(id=campania_id)
    campania.fecha_fin = nueva_fecha_fin
    campania.save()

def buscar_transaccion_por_id (transaccion_id):
    try:
        return Transaccion.objects.get(transaccion_id=transaccion_id)
    except Transaccion.DoesNotExist:
        return None

def grabar_transaccion (transaccion_id, monto, campania_id):
    campania = Donacion.objects.get(id=campania_id)
    print(transaccion_id)
    transaccion = Transaccion (transaccion_id = transaccion_id, monto = monto, campania=campania)
    transaccion.save()

def actualizar_monto_campania (campania_id, monto):
    campania = Donacion.objects.get(id=campania_id)
    campania.monto_recaudado += decimal.Decimal(monto)
    campania.cantidad_donaciones += 1
    campania.save()

def buscar_descuento_por_email (email):
    try:
        return Descuento.objects.get(mail=email)
    except Descuento.DoesNotExist:
        return None

def grabar_descuento (email):
    if buscar_descuento_por_email (email) is None:
        descuento = Descuento (mail = email)
        descuento.save()

def utilizar_descuento(email):
    descuento = buscar_descuento_por_email(email)
    if  not descuento is None:
        descuento = descuento.delete()
"""
        Cruzas
"""

def buscar_cruza_por_cliente_y_nombre(cliente, nombre):
    try:
        return Cruza.objects.get(cliente=cliente, nombre=nombre)
    except:
        return None


def agregar_cruza(cliente, nombre, sexo, raza, edad_meses, peso, color, antecedentes_salud, foto, ultimo_celo):
    if ultimo_celo == "":
        ultimo_celo = None
    cruza = Cruza(
        cliente=cliente,
        nombre=nombre,
        sexo=sexo,
        raza=raza,
        edad_meses=edad_meses,
        peso=peso,
        color=color,
        antecedentes_salud=antecedentes_salud,
        foto=foto,
        ultimo_celo=ultimo_celo
    )
    cruza.save()
    return cruza

def filtrar_cruzas_por_cliente(cliente):
    return Cruza.objects.filter(cliente=cliente)

def eliminar_cruza(cruza_id):
    cruza = get_object_or_404(Cruza, id=cruza_id)
    cruza.delete()
    
def buscar_cruza_por_id(cruza_id):
    return Cruza.objects.get(id=cruza_id)    
    
    
def hay_compatibilidad_de_razas(raza_1, raza_2):
    return (raza_1.lower().replace(" ", "") == raza_2.lower().replace(" ", ""))

def me_interesa_cruzar(cruza_seleccionada, cruza_id):
    intereses = cruza_seleccionada.intereses.filter(id=cruza_id)
    if intereses.exists():
        return True
    else:
        return False
    
def buscar_candidatos(cruza_seleccionada, cliente):
    todas_las_cruzas = Cruza.objects.all().exclude(cliente=cliente)
    candidatos = []
    for cruza in todas_las_cruzas:
        if ((cruza_seleccionada.sexo != cruza.sexo) and 
            (not me_interesa_cruzar(cruza_seleccionada, cruza.id)) and
            (hay_compatibilidad_de_razas(cruza_seleccionada.raza, cruza.raza))):
            candidatos.append(cruza)
            
    return sorted(candidatos, key=lambda cruza: abs(cruza.edad_meses - cruza_seleccionada.edad_meses))

def agregar_interes_cruza(cruza_seleccionada, cruza_de_interes):
    cruza_seleccionada.intereses.add(cruza_de_interes)
    cruza_seleccionada.save()
    
def hay_interes_mutuo(cruza_seleccionada, cruza_de_interes):
    if ((me_interesa_cruzar(cruza_seleccionada=cruza_seleccionada, cruza_id=cruza_de_interes.id)) and
        (me_interesa_cruzar(cruza_seleccionada=cruza_de_interes, cruza_id=cruza_seleccionada.id))):
        return True
    else:
        return False
from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.atenciones.desparacitacion import Desparacitacion
from OhMyDog.modelos.atenciones.vacunacion import Vacunacion
from OhMyDog.modelos.tiposDeDosisVacunacion.tiposDeDosisVacunacion import TipoDeDosisVacunacion
from OhMyDog.modelos.perros import modificar_tiene_castracion


def crear_atencion_clinica(perro, fecha, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id=5)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion, tipo_atencion=tipo_atencion, url_mostrar_datos = "datos_atencion_clinica")
    atencion.save()


def crear_consulta(perro, fecha, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id=1)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion, 
                        tipo_atencion=tipo_atencion, url_mostrar_datos = "datos_consulta")
    atencion.save()


def crear_desparasitacion(perro, fecha, diagnostico, farmaco, fabricante, num_serie, num_lote ,dosis, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id=4)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion, 
                        tipo_atencion=tipo_atencion, url_mostrar_datos = "datos_desparacitacion")
    atencion.save()
    desparacitacion = Desparacitacion(atencion=atencion, diagnostico=diagnostico, farmaco=farmaco, 
                                      fabricante=fabricante, num_serie= num_serie, num_lote=num_lote, dosis=dosis)
    desparacitacion.save()


def crear_castracion(perro, fecha, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id=2)
    modificar_tiene_castracion(perro.id)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion, 
                        tipo_atencion=tipo_atencion, url_mostrar_datos = "datos_castracion")
    atencion.save()


def crear_vacunacion(perro, fecha, vacuna, fabricante, num_serie, num_lote, dosis, observaciones):
    tipo_atencion = TipoDeAtencion.objects.get(id=3)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observaciones, 
                        tipo_atencion=tipo_atencion, url_mostrar_datos = "datos_vacunacion")
    atencion.save()
    vacunacion = Vacunacion(
        atencion=atencion, vacuna=vacuna, fabricante=fabricante, num_serie=num_serie, num_lote=num_lote, dosis=dosis
    )
    vacunacion.save()


def buscar_atenciones_por_perro(perro):
    try:
        return Atencion.objects.filter(perro=perro)
    except Atencion.DoesNotExist:
        return None
    
def buscar_atencion_por_id (atencion_id):
    try:
        return Atencion.objects.get(id = atencion_id)
    except Atencion.DoesNotExist:
        return None

def buscar_vacunacion_por_atencion_id(atencion_id):
    try:
        atencion = Atencion.objects.get(id = atencion_id)
        return Vacunacion.objects.get(atencion = atencion)
    except Vacunacion.DoesNotExist:
        return None


def buscar_desparacitacion_por_atencion_id(atencion_id):
    try:
        atencion = Atencion.objects.get(id = atencion_id)
        return Desparacitacion.objects.get(atencion = atencion)
    except Desparacitacion.DoesNotExist:
        return None
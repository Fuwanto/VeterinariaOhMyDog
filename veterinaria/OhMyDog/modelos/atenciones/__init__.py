from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion

def agregar_atencion_clinica_init(perro, fecha, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id = 1)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion,tipo_atencion= tipo_atencion)
    atencion.save()

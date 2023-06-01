from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.atenciones.desparacitacion import Desparacitacion

def agregar_atencion_clinica_init(perro, fecha, observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id = 5)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion,tipo_atencion= tipo_atencion)
    atencion.save()

def agregar_consulta_init (perro,fecha,observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id = 1)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion,tipo_atencion= tipo_atencion)
    atencion.save()

def agregar_desparacitacion_init (perro,fecha,parasito,farmaco,dosis,observacion):
    tipo_atencion = TipoDeAtencion.objects.get(id= 4)
    atencion = Atencion(perro=perro, fecha=fecha, observacion=observacion,tipo_atencion= tipo_atencion)
    atencion.save()
    desparacitacion = Desparacitacion (atencion = atencion, parasito = parasito, farmaco=farmaco, dosis=dosis)
    desparacitacion.save()

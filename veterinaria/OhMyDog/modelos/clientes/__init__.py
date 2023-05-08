from OhMyDog.modelos import Clientes

def agregar_cliente(datos):
    cliente = Clientes(**datos)
    cliente.save()
    return cliente
from OhMyDog.modelos.clientes.clientes import Cliente


def agregar_cliente(nombre, email, telefono, contraseña):
    cliente = Cliente(
        nombre=nombre, email=email, telefono=telefono, contraseña=contraseña
    )
    cliente.save()
    print()
    return cliente


def borrar_cliente():
    pass


def modificar_cliente():
    pass


def buscar_cliente_por():
    pass


def listar_clientes():
    return Cliente.objects.all()

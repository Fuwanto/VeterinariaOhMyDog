from django.shortcuts import render
from OhMyDog.modelos import agregar_cliente
# Create your views here.


def home(request):
    nombre = "nombre"
    email = "email@gmail.com"
    telefono = "telefono"
    contraseña = "contraseña"
    agregar_cliente(nombre, email, telefono, contraseña)
    return render(request, "home.html")

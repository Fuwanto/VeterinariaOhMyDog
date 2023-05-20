from django.db import models
from OhMyDog.modelos.clientes.clientes import Cliente
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, mail, password, cliente):
        if not mail:
            raise ValueError("El email debe ser proporcionado")

        usuario = self.model(
            mail=self.normalize_email(mail),
            cliente=cliente,  # Asignar el objeto cliente directamente
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, mail, password):
        usuario = self.create_user(mail=mail, password=password, cliente=None)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    cliente = models.OneToOneField(Cliente, null=True, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)
    primer_inicio = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "mail"

    objects = UsuarioManager()

    def __str__(self):
        return self.mail


def alternar_primer_acceso(id):
    usuario = Usuario.objects.get(id=id)
    usuario.primer_inicio = False
    usuario.save()

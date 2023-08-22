from django.db.models import *
from django.contrib.auth.models import AbstractUser


# # ---- Rol de Usuario ---- #
# class Role(Model):
#     name = CharField("Nombre", max_length=15)
#     description = CharField(max_length=30, verbose_name="Descripción")
#     is_active = BooleanField("Activo", default=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "CS_CAT_ROLES"
#         verbose_name = "Rol"
#         verbose_name_plural = "Roles"


# ----- Usuarios ----- #
class User(AbstractUser):
    """
    Los usuarios dentro del sistema de autenticación están representados por este modelo.

    Se requiere nombre de usuario, email y  contraseña. Otros campos son opcionales.
    """

    # Permissions
    # roles = ForeignKey(
    #     Role,
    #     verbose_name="Rol",
    #     on_delete=RESTRICT,
    #     help_text="Designa el rol que tendrá el usuario",
    #     default=1,
    # )

    def __str__(self):
        return self.username

    class Meta:
        db_table = "CAT_USER"
        verbose_name = "Usuario"
        verbose_name_plural = "Users"

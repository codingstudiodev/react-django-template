from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserA
from django.contrib.auth.models import Group, Permission
from .models import User
from django.utils.translation import gettext_lazy as _


# admin.site.register(Group)
admin.site.register(Permission)


class UserAdmin(UserA):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("last_login", "date_joined")

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, UserAdmin)

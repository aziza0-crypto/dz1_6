
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "role",
        "is_verified",
        "is_active",
    )

    list_filter = (
        "role",
        "is_verified",
    )

    search_fields = (
        "email",
        "username",
    )

    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Личная информация",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "bio",
                    "birth_date",
                    "role",
                    "is_verified",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Даты", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
 
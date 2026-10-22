
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Администратор"
        MODERATOR = "MODERATOR", "Модератор"
        USER = "USER", "Пользователь"
        CLIENT = "CLIENT", "Клиент"

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
    )

    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
 
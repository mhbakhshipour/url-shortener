from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.username}"

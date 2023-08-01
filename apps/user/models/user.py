from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.user.managers import CustomUserManager
from common.base.base_model import BaseModel


class CustomUser(BaseModel, AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        self.username = self.email
        return super().save()


class Profile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.user.username}'

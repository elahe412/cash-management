from django.db import models

from apps.transaction.choices import CategoryChoices
from apps.user.models import CustomUser
from common.base.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)


class Transaction(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    kind = models.CharField(choices=CategoryChoices.choices, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=100, null=True)

from django.db import models


class CategoryChoices(models.TextChoices):
    INCOME = 'income'
    EXPENSE = 'expense'

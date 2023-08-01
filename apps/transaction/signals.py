from django.db.models.signals import post_save
from django.dispatch import receiver

from .choices import CategoryChoices
from .models import Transaction
from ..user.models import Profile


@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, created, **kwargs):
    user = instance.user
    profile = Profile.objects.get(user=user)

    if instance.kind == CategoryChoices.INCOME.value:
        profile.balance += instance.amount
    if instance.kind == CategoryChoices.EXPENSE.value:
        profile.balance -= instance.amount

    profile.save()

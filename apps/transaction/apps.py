from django.apps import AppConfig


class TransactionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.transaction'

    def ready(self):
        import apps.transaction.signals

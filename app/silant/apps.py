from django.apps import AppConfig


class SilantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'silant'

    def ready(self):
        import silant.signals

from django.apps import AppConfig


class ObservoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'observo'

    def ready(self):
        import observo.signals

from django.apps import AppConfig


from django.apps import AppConfig

class PharmaReaderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # A MUDANÇA É AQUI EMBAIXO:
    name = 'apps.pharma_reader'

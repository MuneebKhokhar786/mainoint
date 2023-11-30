from django.apps import AppConfig


class LaptopShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'laptop_shop'

    def ready(self):
        import laptop_shop.signals

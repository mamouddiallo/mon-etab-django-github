from django.apps import AppConfig

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_default_user

        post_migrate.connect(create_default_user, sender=self)

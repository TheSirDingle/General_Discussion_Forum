from django.apps import AppConfig
from django.contrib import admin


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'


    def ready(self):
        import Users.signals
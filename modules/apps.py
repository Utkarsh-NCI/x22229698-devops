'"Modules application configruation file"'
from django.apps import AppConfig

class ModulesConfig(AppConfig):
    """Config class for registering application"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules"

from django.apps import AppConfig


class RLoggingDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rlogging.integrations.django'
    label = 'rlogging_integrations_django'

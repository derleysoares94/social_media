from django.apps import AppConfig


class CommunitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'communities'

    def ready(self):
        import communities.templatetags.community_extras
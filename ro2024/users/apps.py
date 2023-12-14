from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ro2024.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import ro2024.users.signals  # noqa: F401
        except ImportError:
            pass

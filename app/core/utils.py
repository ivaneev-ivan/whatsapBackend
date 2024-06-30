from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoices(models.TextChoices):
    OFF = "OFF", _("Выключен")
    ON = "ON", _("Включен")
    IN_PROGRESS = "PROGRESS", _("Исполняет команду")

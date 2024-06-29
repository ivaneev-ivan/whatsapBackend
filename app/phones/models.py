from django.utils.translation import gettext_lazy as _

from django.db import models


class Phone(models.Model):
    class StatusChoices(models.TextChoices):
        OFF = "OFF", _("Выключен")
        ON = "ON", _("Включен")
        IN_PROGRESS = "PROGRESS", _("Исполняет команду")

    serial = models.CharField(verbose_name="Серий номер телефона", max_length=50, unique=True)
    model = models.CharField(verbose_name="Модель телефона", max_length=50)
    w_business = models.CharField(verbose_name="Номер телефона в whatsapp business", max_length=50, null=True,
                                  blank=True)
    w_base = models.CharField(verbose_name="Номер телефона в whatsapp", max_length=50, null=True, blank=True)
    is_usual = models.BooleanField(verbose_name="Используется 2 whatsapp", default=False)
    status = models.CharField(verbose_name="Статус телефона", choices=StatusChoices, default=StatusChoices.OFF)
    note = models.TextField(verbose_name="Пометки", null=True, blank=True)

    def get_status(self):
        return self.StatusChoices(self.status)
    
    def __str__(self):
        return f"{self.serial} - {self.model}"
    
    class Meta:
        db_table = 'phones'
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


class PhoneLimit(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    message_limits = models.SmallIntegerField(verbose_name="Диапазон пауз между сообщениями в рассылке")
    warming_message_limits = models.SmallIntegerField(verbose_name="Диапазон пауз между сообщениями в прогреве")
    call_outgoing_limits = models.SmallIntegerField(verbose_name="Диапазон пауз между исходящими звонками")
    call_take_phone_limits = models.SmallIntegerField(verbose_name="Диапазон пауз между исходящими звонками")
    
    def __str__(self):
        return f"{self.phone} - Лимиты"
    
    class Meta:
        db_table = 'phones_limits'
        verbose_name = 'Лимиты телефона'
        verbose_name_plural = 'Лимиты телефонов'

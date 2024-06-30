from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.utils import StatusChoices


class Device(models.Model):
    serial = models.CharField(verbose_name="Серий номер телефона", max_length=50, unique=True)
    model = models.CharField(verbose_name="Модель телефона", max_length=50)
    note = models.TextField(verbose_name="Пометки", null=True, blank=True)

    def __str__(self):
        return f"{self.serial} - {self.model}"

    class Meta:
        db_table = 'devices'
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class Phone(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, verbose_name="Номер телефона")
    status = models.CharField(verbose_name="Статус номера телефона", choices=StatusChoices)
    wa_is_business = models.BooleanField(default=False)

    def get_status(self):
        return StatusChoices(self.status)

    def __str__(self):
        return f"{self.device} - {self.phone}"

    class Meta:
        db_table = 'phones'
        verbose_name = "Телефон"
        verbose_name_plural = "Номера телефонов"


class PhoneLimit(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    message_sec_limits_from = models.SmallIntegerField(verbose_name="Диапазон пауз между сообщениями в рассылке от",
                                                       default=1)
    message_sec_limits_to = models.SmallIntegerField(verbose_name="Диапазон пауз между сообщениями в рассылке до",
                                                     default=3)
    warming_message_sec_limits_from = models.SmallIntegerField(
        verbose_name="Диапазон пауз между сообщениями в прогреве от",
        default=1)
    warming_message_sec_limits_to = models.SmallIntegerField(
        verbose_name="Диапазон пауз между сообщениями в прогреве до",
        default=3)
    call_outgoing_sec_limits_from = models.SmallIntegerField(verbose_name="Диапазон пауз между исходящими звонками от",
                                                             default=1)
    call_outgoing_sec_limits_to = models.SmallIntegerField(verbose_name="Диапазон пауз между исходящими звонками до",
                                                           default=3)
    call_take_phone_sec_limits_from = models.SmallIntegerField(
        verbose_name="Диапазон пауз между исходящими звонками от",
        default=1)
    call_take_phone_sec_limits_to = models.SmallIntegerField(verbose_name="Диапазон пауз между исходящими звонками до",
                                                             default=3)

    def __str__(self):
        return f"{self.phone} - Лимиты"

    class Meta:
        db_table = 'phones_limits'
        verbose_name = 'Лимиты телефона'
        verbose_name_plural = 'Лимиты телефонов'

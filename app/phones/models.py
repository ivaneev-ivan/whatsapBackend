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
    online = models.BooleanField(default=True)
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
    
    warming_call_outgoing_sec_limits_from = models.PositiveIntegerField(default=3600)
    warming_call_outgoing_sec_limits_to = models.PositiveIntegerField(default=10800 )
    warming_call_outgoing_sec_limits_delta = models.IntegerField(default=-100)
    warming_call_outgoing_sec_limits_from_min = models.PositiveIntegerField(default=1000)
    warming_call_outgoing_sec_limits_to_min = models.PositiveIntegerField(default=3600)
    warming_call_outgoing_duration_sec_limits_from = models.PositiveIntegerField(default=15)
    warming_call_outgoing_duration_sec_limits_to = models.PositiveIntegerField(default=35)
    warming_call_incoming_take_phone_sec_limits_from = models.PositiveIntegerField(default=20)
    warming_call_incoming_take_phone_sec_limits_from = models.PositiveIntegerField(default=40)
    
    warming_call_qty_outgoing = models.PositiveIntegerField(default=0)
    warming_call_qty_incoming = models.PositiveIntegerField(default=0)
    
    warming_message_sec_limits_from = models.PositiveIntegerField(default=300)
    warming_message_sec_limits_to = models.PositiveIntegerField(default=1500)
    warming_message_sec_limits_delta = models.IntegerField(default=-30)
    warming_message_sec_limits_from_min = models.PositiveIntegerField(default=80)
    warming_message_sec_limits_to_min = models.PositiveBigIntegerField(default=150)
    
    warming_message_qty_sent = models.PositiveIntegerField(default=0)
    warming_message_qty_receive = models.PositiveBigIntegerField(default=0)
    
    message_sec_limits_from = models.PositiveIntegerField(default=70)
    message_sec_limits_to = models.PositiveIntegerField(default=350)
    
    message_autoanswer_sec_limits_from = models.PositiveIntegerField(default=350)
    message_autoanswer_sec_limits_to = models.PositiveIntegerField(default=350)
    
    
    def __str__(self):
        return f"{self.phone} - Лимиты"

    class Meta:
        db_table = 'phones_limits'
        verbose_name = 'Лимиты телефона'
        verbose_name_plural = 'Лимиты телефонов'

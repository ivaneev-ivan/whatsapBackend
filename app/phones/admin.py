from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import PhoneLimit, Device, Phone


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial', 'model')
    list_display_links = ('id', 'serial')
    list_filter = ('id', 'model')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'phone', 'status', 'wa_is_business')


@admin.register(PhoneLimit)
class PhoneLimitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'link_to_phone', 'message_sec_limits_from', 'message_sec_limits_to', 'warming_message_sec_limits_from',
        'warming_message_sec_limits_to', 'call_outgoing_sec_limits_from', 'call_outgoing_sec_limits_to',
        'call_take_phone_sec_limits_from', 'call_take_phone_sec_limits_to')
    list_display_links = ('id', 'link_to_phone')

    def link_to_phone(self, obj):
        link = reverse("admin:phones_phone_change", args=[obj.phone.id])  # model name has to be lowercase
        return format_html(f'<a href="{link}">{obj.phone}</a>')

    link_to_phone.short_description = 'Телефон'

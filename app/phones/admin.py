from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Phone, PhoneLimit


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial', 'model', 'w_business', 'w_base', 'is_usual', 'status')
    list_display_links = ('id', 'serial')
    list_filter = ('id', 'model', 'status', 'is_usual')
    list_editable = ('is_usual', 'status')


@admin.register(PhoneLimit)
class PhoneLimitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'link_to_phone', 'message_limits', 'warming_message_limits', 'call_outgoing_limits',
        'call_take_phone_limits')
    list_display_links = ('id', 'link_to_phone')

    def link_to_phone(self, obj):
        link = reverse("admin:phones_phone_change", args=[obj.phone.id])  # model name has to be lowercase
        return format_html(f'<a href="{link}">{obj.phone}</a>')

    link_to_phone.short_description = 'Телефон'

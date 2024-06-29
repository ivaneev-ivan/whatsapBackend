from rest_framework import serializers

from phones.models import Phone, PhoneLimit


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class PhoneLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneLimit
        fields = '__all__'

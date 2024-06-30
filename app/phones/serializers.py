from rest_framework import serializers

from phones.models import Phone, PhoneLimit, Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)

    class Meta:
        model = Phone
        fields = '__all__'


class PhoneLimitSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(read_only=True)

    class Meta:
        model = PhoneLimit
        fields = '__all__'

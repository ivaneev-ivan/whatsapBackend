from rest_framework import serializers

from phones.models import Phone, PhoneLimit, Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    device_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Device.objects.all())

    def create(self, validated_data):
        data = {**validated_data, "device_id":validated_data['device_id'].pk}
        return super().create(data)   
    
    class Meta:
        model = Phone
        fields = '__all__'

class PhoneLimitSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(read_only=True)

    phone_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Phone.objects.all())

    def create(self, validated_data):
        data = {**validated_data, "phone_id":validated_data['phone_id'].pk}
        return super().create(data)   

    class Meta:
        model = PhoneLimit
        fields = '__all__'
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import Phone, PhoneLimit, Device
from .serializers import PhoneLimitSerializer, PhoneSerializer, DeviceSerializer


class DeviceModelViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneLimitModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneLimit.objects.all()
    serializer_class = PhoneLimitSerializer

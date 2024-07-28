from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import Phone, PhoneLimit
from .serializers import PhoneLimitSerializer, PhoneSerializer


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneLimitModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneLimit.objects.all()
    serializer_class = PhoneLimitSerializer

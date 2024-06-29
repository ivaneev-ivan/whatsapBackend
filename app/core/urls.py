from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from phones.views import PhoneModelViewSet, PhoneLimitModelViewSet

router = DefaultRouter()
router.register(r'phones', PhoneModelViewSet, basename='phones')
router.register(r'phones_limits', PhoneLimitModelViewSet, basename='phones_limits')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

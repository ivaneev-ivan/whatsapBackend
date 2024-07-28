from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from phones.views import PhoneModelViewSet, PhoneLimitModelViewSet
from tasks.views import TaskArgsViewSet, CommandArgViewSet, CommandViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'phones', PhoneModelViewSet, basename='api_phones')
router.register(r'phones_limits', PhoneLimitModelViewSet, basename='api_phones_limits')
router.register(r'tasks', TaskViewSet, basename='api_tasks')
router.register(r'commands', CommandViewSet, basename='api_commands')
router.register(r'tasks_args', TaskArgsViewSet, basename='api_tasks_args')
router.register(r'comment_args', CommandArgViewSet, basename='api_comment_args')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

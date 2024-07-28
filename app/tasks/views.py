from rest_framework import viewsets

from .models import Task, Command, CommandArg, TaskArg
from .serializers import TaskSerializer, TaskArgsSerializer, CommandArgsSerializer, CommandSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer


class CommandArgViewSet(viewsets.ModelViewSet):
    queryset = CommandArg.objects.all()
    serializer_class = CommandArgsSerializer


class TaskArgsViewSet(viewsets.ModelViewSet):
    queryset = TaskArg.objects.all()
    serializer_class = TaskArgsSerializer

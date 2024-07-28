from rest_framework import serializers

from phones.models import Phone
from phones.serializers import PhoneSerializer
from .models import Command, CommandArg, Task, TaskArg


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'


class CommandArgsSerializer(serializers.ModelSerializer):
    command = CommandSerializer(read_only=True)

    class Meta:
        model = CommandArg
        fields = '__all__'


class TaskArgsSerializer(serializers.ModelSerializer):
    arg = CommandArgsSerializer(read_only=True)

    class Meta:
        model = TaskArg
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    command = CommandSerializer(read_only=True)
    command_id = serializers.PrimaryKeyRelatedField(queryset=Command.objects.all())
    phone = PhoneSerializer(read_only=True)
    phone_id = serializers.PrimaryKeyRelatedField(queryset=Phone.objects.all())
    args = TaskArgsSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

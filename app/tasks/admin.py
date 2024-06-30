from django.contrib import admin

from .models import Command, CommandArg, Task, TaskArg


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


@admin.register(CommandArg)
class CommandArgAdmin(admin.ModelAdmin):
    list_display = ('id', 'command', 'name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'command', 'status')


@admin.register(TaskArg)
class TaskArgAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'arg', 'value')

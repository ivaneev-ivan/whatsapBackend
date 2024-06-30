from django.db import models
from django.template.defaultfilters import slugify

from core.utils import StatusChoices
from phones.models import Phone


class Command(models.Model):
    name = models.CharField(verbose_name="Название команды", max_length=100, unique=True)
    slug = models.SlugField(verbose_name="Slug команды", unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Command, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        db_table = "commands"
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class CommandArg(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название атрибута команды")

    def __str__(self):
        return f"{self.command} - {self.name}"

    class Meta:
        db_table = "commands_args"
        verbose_name = "Атрибуты команды"
        verbose_name_plural = "Атрибуты команд"


class Task(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    status = models.CharField(verbose_name="Статус задачи", choices=StatusChoices)

    def __str__(self):
        return f"{self.phone} выполняет {self.command.name} - {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class TaskArg(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    arg = models.ForeignKey(CommandArg, on_delete=models.CASCADE)
    value = models.CharField(verbose_name="Значение атрибута", max_length=255)

    def __str__(self):
        return f"{self.arg} - {self.value}"

    class Meta:
        db_table = "tasks_args"
        verbose_name = "Аргумент задачи"
        verbose_name_plural = "Аргументы задач"

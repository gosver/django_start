from django.conf import settings as settings_conf
from django.db import models
from django.utils import timezone


# Create your models here.
#from main.apps.category.models import Categories


# class Projects(models.Model):
#     name = models.CharField('Имя проекта', max_length=50)
#     date = models.DateTimeField('Дата добавления', default=timezone.now)
#     user = models.ForeignKey(
#         settings_conf.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='project_user'
#     )
#     settings = models.TextField('Настройки проекта', null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Проект"
#         verbose_name_plural = "Список проектов"

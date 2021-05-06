from django.db import models
from .basic_model import Basic


class User(Basic):
    full_name = models.CharField(
        verbose_name='نام',
    )
    username = models.CharField(
        verbose_name='نام کاربری',
        unique=True
    )
    password = models.CharField(
        verbose_name='رمز',
        unique=True
    )
    email = models.EmailField(
        verbose_name='ایمیل',
        unique=True
    )
    point = models.IntegerField(
        default=0,
        verbose_name='امتیاز'
    )
    level = models.IntegerField(
        default=-10,
        verbose_name='سطح'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='ایا فعال است؟'
    )

    def __str__(self):
        return self.username

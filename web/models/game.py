from .basic_model import Basic
from django.db import models

from .user import User


class Sponsor(Basic):
    title = models.CharField()
    followers = models.ManyToManyField(
        to=User,
        null=True
    )


class Company(Basic):
    title = models.CharField()
    followers = models.ManyToManyField(
        to=User,
        null=True
    )


class Game(Basic):
    title = models.CharField(
        max_length=200,
        verbose_name='نام',
        unique=True,
    )
    followers = models.ManyToManyField(
        to=User,
        null=True,
        verbose_name='دنبال کنندگان'
    )
    creator_companies = models.ManyToManyField(
        to=Company,
        verbose_name=''
    )


class Competition(Basic):
    game = models.ForeignKey(
        to=Game,
        verbose_name='',
        on_delete=models.CASCADE
    )
    beginning_time = models.DateTimeField(
        verbose_name=''
    )
    finishing_time = models.DateTimeField(
        verbose_name=''
    )
    sponsor = models.ForeignKey(
        to=Sponsor,
        on_delete=models.CASCADE,
        verbose_name='',
        null=True,
        blank=True
                                )
    awards = models.TextField(
        verbose_name=''
    )
    title = models.CharField(
        verbose_name=''
    )
    description = models.TextField(
        verbose_name='',
        null=True,
        blank=True
    )

from django.db import models

from admin_panel.models import *
from register.models import User


class Flat(models.Model):
    number = models.CharField(
        max_length=50,
        verbose_name='Номер квартиры',
        blank=False,
        null=True,
    )
    area = models.FloatField(
        max_length=50,
        verbose_name='Площадь(кв.м.)',
        blank=True,
        null=True,
    )
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='flats',
        default='',
        blank=False,
    )
    section = models.ForeignKey(
        HouseSection,
        on_delete=models.CASCADE,
        related_name='flats',
        default='',
        blank=True,
    )
    floor = models.ForeignKey(
        HouseFloor,
        on_delete=models.CASCADE,
        related_name='flats',
        default='',
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='flats',
        default='',
        blank=True,
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.CASCADE,
        related_name='flats',
        default='',
        blank=True,
    )

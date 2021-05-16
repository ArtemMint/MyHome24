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
        verbose_name='Дом',
        null=True,
        blank=False,
    )
    section = models.ForeignKey(
        HouseSection,
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Секция',
        null=True,
        blank=True,
    )
    floor = models.ForeignKey(
        HouseFloor,
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Этаж',
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Владелец',
        null=True,
        blank=True,
    )
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Тариф  ',
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'Квартира №{self.number} - {self.house}'

    class Meta:
        ordering = ('-editing_date',)

    @staticmethod
    def get_flats_count():
        return Flat.objects.all().count()

    @staticmethod
    def get_flats_list():
        return Flat.objects.all()

    @staticmethod
    def get_flat_by_pk(pk):
        return Flat.objects.get(pk=pk)

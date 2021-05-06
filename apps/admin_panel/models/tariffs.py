from django.db import models
from django.utils import timezone

from admin_panel.models import (
    Services,
    Metrics,
)


class Tariff(models.Model):
    """
    Tariff model
    """
    name = models.CharField(
        max_length=250,
        verbose_name='Название тарифа',
        blank=False,
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание тарифа',
        blank=True,
        null=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['-editing_date',]

    def __str__(self):
        return self.name

    def get_tariff_for_copy(pk):
        tarriff = Tariff.objects.get(id=pk)
        tarriff.id = None
        return tarriff




class TariffService(models.Model):
    """
    TariffService model
    """
    tariff = models.ForeignKey(
        Tariff,
        on_delete=models.CASCADE,
        related_name='tariff_service',
    )
    service = models.ForeignKey(
        Services,
        on_delete=models.CASCADE,
        related_name='tariff_services',
    )
    price = models.FloatField(
        max_length=500,
        verbose_name='Цена',
        blank=False,
    )
    currency = models.CharField(
        max_length=25,
        verbose_name='Валюта',
        default='грн',
    )
    metric = models.ForeignKey(
        Metrics,
        on_delete=models.CASCADE,
        related_name='tariff_metrics',
    )

    def __str__(self):
        return f'{self.tariff} - {self.service}'

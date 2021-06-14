from django.db import models


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
        ordering = ['-editing_date', ]

    def __str__(self):
        return self.name

    def get_tariff_for_copy(self, pk):
        tariff = self.objects.get(id=pk)
        tariff.id = None
        return tariff


class TariffService(models.Model):
    """
    TariffService model
    """
    tariff = models.ForeignKey(
        'admin_panel.Tariff',
        on_delete=models.CASCADE,
        related_name='tariff_service',
        verbose_name='Тариф',
    )
    service = models.ForeignKey(
        'admin_panel.Services',
        on_delete=models.CASCADE,
        related_name='tariff_services',
        verbose_name='Услуга',
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
        'admin_panel.Metrics',
        on_delete=models.CASCADE,
        related_name='tariff_metrics',
        verbose_name='Ед.изм.',
    )

    def __str__(self):
        return f'{self.tariff} - {self.service}'

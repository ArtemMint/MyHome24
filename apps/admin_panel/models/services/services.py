"""
Services model
"""

from django.db import models

from .metrics import Metrics


class Services(models.Model):
    """
    Services model
    """
    name = models.CharField(
        verbose_name='Услуга',
        max_length=250,
        blank=False,
    )
    metric = models.ForeignKey(
        Metrics,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Ед.изм.',
        related_name='metrics',
    )
    show_in_meter_reading = models.BooleanField(
        default='False',
        verbose_name='Показывать в счетчиках',
    )

    def __str__(self):
        return self.name
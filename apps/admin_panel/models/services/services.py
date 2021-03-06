"""
Services model
"""

from django.db import models


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
        'admin_panel.Metrics',
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
        return f'{self.name} ({self.metric.name})'

    @classmethod
    def get_service_list(cls):
        return cls.objects.all()

    @classmethod
    def get_active_services(cls):
        return cls.get_service_list().filter(show_in_meter_reading=True)

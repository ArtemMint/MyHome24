"""
Services page on website
"""

from django.db import models

from solo.models import SingletonModel


class ServicesPage(SingletonModel):
    seo = models.OneToOneField(
        'admin_panel.SEO',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Settings SEO',
        related_name='services_page',
    )


class ServicesSite(models.Model):
    """
    Table with services_metrics info for website
    """
    image = models.ImageField(
        blank=True,
        upload_to='images/services_metrics/',
        verbose_name='Рекомендуемый размер: (650x300)'
    )
    name = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Название услуги',
    )
    description = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='Описание услуги'
    )
    services_page = models.ForeignKey(
        'admin_panel.ServicesPage',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='service',
        related_name='services',
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)

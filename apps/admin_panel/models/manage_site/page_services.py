"""
Services page on website
"""

from django.db import models

from solo.models import SingletonModel
from .page_seo import SEO


class ServicesPage(SingletonModel):
    seo = models.OneToOneField(
        SEO,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Settings SEO',
        related_name='services_page',
    )


class Services(models.Model):
    """
    Table with services info for website
    """
    image = models.ImageField(
        blank=True,
        upload_to='images/services/',
        verbose_name='Recommend size (650x300)'
    )
    name = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Service name',
    )
    description = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='Service description'
    )
    services_page = models.ForeignKey(
        ServicesPage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='service',
        related_name='services',
    )

    def __str__(self):
        return str(self.name)

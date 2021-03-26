"""
Services page on website
"""

from django.db import models

from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from ..models import SEO


class ServicesPage(SingletonModel):
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
    )
    description = RichTextField(
        blank=True,
        max_length=1000,
    )
    seo = models.OneToOneField(
        SEO,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Settings SEO',
        related_name='services_page',
    )

    def __str__(self):
        return str(self.name)
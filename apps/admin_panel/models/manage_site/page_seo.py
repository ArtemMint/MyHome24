"""
Module with SEO table of the website
"""

from django.db import models


class SEO(models.Model):
    """
    Table with SEO info about each pages on website
    """
    seo_title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Title',
    )
    seo_description = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name='Description',
    )
    seo_keywords = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name='Keywords',
    )

    def __str__(self):
        return self.seo_title

"""
Metrics model
"""

from django.db import models


class Metrics(models.Model):
    """
    Metrics model
    """
    name = models.CharField(
        verbose_name='Ед.изм.',
        max_length=100,
    )

    def __str__(self):
        return self.name
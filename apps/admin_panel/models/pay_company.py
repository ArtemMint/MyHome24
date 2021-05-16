"""
Pay-company model
"""

from django.db import models

from solo.models import SingletonModel


class PayCompany(SingletonModel):
    """
    Pay-company model
    """
    name = models.CharField(
        verbose_name='Название компании',
        max_length=250,
    )
    info = models.TextField(
        verbose_name='Информация',
        max_length=1500,
    )

from django.db import models

from admin_panel import models as admin_models


class Account(models.Model):
    STATUS = (
        ('Активен', 'Активен'),
        ('Неактивен', 'Неактивен'),
    )
    number = models.BigIntegerField(
        verbose_name='№',
        unique=True,
        blank=False,
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS,
        default=STATUS[0][0],
        verbose_name='Статус',
        blank=False,
    )
    account_balance = models.FloatField(
        max_length=50,
        verbose_name='Остаток',
        default=0,
    )
    house = models.ForeignKey(
        admin_models.House,
        on_delete=models.CASCADE,
        verbose_name='Дом',
        related_name='accounts',
        blank=False,
    )
    section = models.ForeignKey(
        admin_models.HouseSection,
        on_delete=models.CASCADE,
        verbose_name='Секция',
        related_name='accounts',
        blank=False,
    )
    flat = models.ForeignKey(
        admin_models.Flat,
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='accounts',
        blank=False,
    )

from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    STATUS = (
        ('Оплачена', 'Оплачена'),
        ('Частично оплачена', 'Частично оплачена'),
        ('Неоплачена', 'Неоплачена'),
    )
    number = models.CharField(
        max_length=20,
        verbose_name='№',
        unique=True,
        blank=False,
    )
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        verbose_name='Дом',
        related_name='invoices',
        null=True,
        blank=True,
    )
    section = models.ForeignKey(
        'admin_panel.HouseSection',
        on_delete=models.CASCADE,
        verbose_name='Секция',
        related_name='invoices',
        null=True,
        blank=True,
    )
    flat = models.ForeignKey(
        'admin_panel.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='invoices',
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        'register.User',
        on_delete=models.SET_NULL,
        related_name='invoices',
        null=True,
        blank=True,
    )
    confirm = models.BooleanField(
        verbose_name='Проведен',
        default=True,
    )
    status = models.CharField(
        max_length=50,
        verbose_name='Статус',
        choices=STATUS,
        default=STATUS[0][0],
    )
    tariff = models.ForeignKey(
        'admin_panel.Tariff',
        on_delete=models.SET_NULL,
        related_name='invoices',
        verbose_name='Тариф',
        null=True,
        blank=True,
    )
    start_date = models.DateTimeField(
        default=timezone.now,
    )
    end_date = models.DateTimeField(
        default=timezone.now,
    )
    account = models.ForeignKey(
        'admin_panel.Account',
        on_delete=models.CASCADE,
        verbose_name='Лицевой счет',
        related_name='invoices',
        blank=False,
    )
    created_date = models.DateTimeField(
        default=timezone.now,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        ordering = ('-editing_date',)

    @classmethod
    def get_invoice_list(cls):
        return cls.objects.all()

    @classmethod
    def get_invoice_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

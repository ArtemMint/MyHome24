from django.db import models
from django.utils import timezone


class AccountTransaction(models.Model):
    number = models.CharField(
        max_length=20,
        verbose_name='№',
        unique=True,
        blank=False,
    )
    owner = models.ForeignKey(
        'register.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец квартиры',
        related_name='account_transactions_owners',
        blank=False,
    )
    manager = models.ForeignKey(
        'register.User',
        on_delete=models.CASCADE,
        verbose_name='Менеджер',
        related_name='account_transactions_managers',
        blank=False,
    )
    account = models.ForeignKey(
        'admin_panel.Account',
        on_delete=models.CASCADE,
        verbose_name='Лицевой счет',
        related_name='account_transactions',
        blank=False,
    )
    transaction = models.ForeignKey(
        'admin_panel.TransactionPurpose',
        on_delete=models.CASCADE,
        verbose_name='Статья',
        related_name='account_transactions',
        blank=False,
    )
    total = models.FloatField(
        max_length=50,
        verbose_name='Сумма',
        blank=False,
        null=True,
    )
    confirm = models.BooleanField(
        verbose_name='Проведен',
        default=True,
    )
    comment = models.CharField(
        max_length=500,
        verbose_name='Комментарий',
        blank=True,
        default='',
    )
    type = models.CharField(
        max_length=50,
        verbose_name='Приход/расход',
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
    def get_queryset_list(cls,):
        return cls.objects.all()

    @classmethod
    def get_account_transaction_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def get_total_income(cls,):
        income = 0
        queryset = cls.objects.filter(type='Приход')
        for value in queryset:
            income += value.total
        return income

    @classmethod
    def get_total_expenditure(cls,):
        expenditure = 0
        queryset = cls.objects.filter(type='Расход')
        for value in queryset:
            expenditure += value.total
        return abs(expenditure)

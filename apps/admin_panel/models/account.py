from django.db import models


class Account(models.Model):
    STATUS = (
        ('Активен', 'Активен'),
        ('Неактивен', 'Неактивен'),
    )
    number = models.CharField(
        max_length=20,
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
    balance = models.FloatField(
        max_length=50,
        verbose_name='Остаток',
        default=0,
    )
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        verbose_name='Дом',
        related_name='accounts',
        blank=False,
    )
    section = models.ForeignKey(
        'admin_panel.HouseSection',
        on_delete=models.CASCADE,
        verbose_name='Секция',
        related_name='accounts',
        blank=False,
    )
    flat = models.ForeignKey(
        'admin_panel.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='accounts',
        blank=False,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        ordering = ('-editing_date',)

    def get_account_balance(self):
        if not self.account_transactions:
            return 0.00
        incomes = self.account_transactions.filter(
            account__status='Активен'
        ).aggregate(models.Sum('total'))['total__sum'] or 0.00
        outcomes = self.account_transactions.filter(
            account__status='Неактивен'
        ).aggregate(models.Sum('total'))['total__sum'] or 0.00
        return round((incomes - outcomes), 2)

    @staticmethod
    def get_accounts_list():
        return Account.objects.all()

    @staticmethod
    def get_account_by_pk(pk):
        return Account.objects.get(pk=pk)

    @staticmethod
    def get_accounts_count():
        return Account.objects.all().count()

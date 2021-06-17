from django.db import models
from django.utils import timezone


class CounterData(models.Model):
    STATUS = (
        ('Новое', 'Новое'),
        ('Учтено', 'Учтено'),
        ('Нулевое', 'Нулевое'),
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
        related_name='counter_data',
        blank=False,
    )
    section = models.ForeignKey(
        'admin_panel.HouseSection',
        on_delete=models.CASCADE,
        verbose_name='Секция',
        related_name='counter_data',
        blank=False,
    )
    flat = models.ForeignKey(
        'admin_panel.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='counter_data',
        blank=False,
    )
    counter = models.ForeignKey(
        'admin_panel.Services',
        on_delete=models.CASCADE,
        verbose_name='Cчетчик',
        related_name='counter_data',
        blank=False,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default=STATUS[0][0],
        verbose_name='Статус',
        blank=False,
    )
    value = models.FloatField(
        max_length=50,
        verbose_name='Показания счетчика',
        default=0,
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
    def get_counter_data_list(cls,):
        return cls.objects.all()

    @classmethod
    def get_counter_data_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

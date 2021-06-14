from django.db import models
from django.utils import timezone


class MasterRequest(models.Model):
    STATUS = (
        ('Новое', 'Новое'),
        ('В работе', 'В работе'),
        ('Выполнено', 'Выполнено'),
    )
    MASTER_TYPE = (
        ('Сантехник', 'Сантехник'),
        ('Электрик', 'Электрик'),
        ('Слесарь', 'Слесарь'),
        ('Любой специалист', 'Любой специалист'),
    )

    time = models.TimeField(
        verbose_name='Время',
        unique=True,
        blank=False,
    )
    owner = models.ForeignKey(
        'register.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец квартиры',
        related_name='master_request_owners',
        blank=False,
    )
    description = models.TextField(
        max_length=1500,
        verbose_name='Описание',
        blank=True,
        default='',
    )
    flat = models.ForeignKey(
        'admin_panel.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='master_requests',
        blank=False,
    )
    master_type = models.CharField(
        max_length=50,
        verbose_name='Тип мастера',
        choices=MASTER_TYPE,
        default=MASTER_TYPE[3][0],
    )
    status = models.CharField(
        max_length=100,
        verbose_name='Статус',
        choices=STATUS,
        default=STATUS[0][0],
    )
    master = models.ForeignKey(
        'register.User',
        on_delete=models.CASCADE,
        verbose_name='Мастер',
        related_name='master_request_managers',
        blank=True,
    )
    comment = models.CharField(
        max_length=500,
        verbose_name='Комментарий',
        blank=True,
        default='',
    )
    created_date = models.DateTimeField(
        default=timezone.now,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ('-editing_date',)

    @classmethod
    def get_all_queryset_list(cls):
        return cls.objects.all()

    @classmethod
    def get_master_request_by_pk(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def get_all_queryset_count(cls):
        return cls.objects.all().count()

    @classmethod
    def get_new_request_count(cls):
        return cls.objects.filter(status='Новое').count()

    @classmethod
    def get_in_work_request_count(cls):
        return cls.objects.filter(status='В работе').count()

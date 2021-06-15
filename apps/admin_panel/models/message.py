from django.db import models


class Message(models.Model):
    title = models.TextField(
        max_length=100,
        blank=False,
    )
    text = models.CharField(
        max_length=1000,
        blank=True,
    )
    indebtedness = models.BooleanField(
        default=False,
        verbose_name='Владельцам с задолженностями',
    )
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        verbose_name='Дом',
        related_name='messages',
        blank=True,
        null=True,
    )
    section = models.ForeignKey(
        'admin_panel.HouseSection',
        on_delete=models.CASCADE,
        verbose_name='Секция',
        related_name='messages',
        blank=True,
        null=True,
    )
    floor = models.ForeignKey(
        'admin_panel.HouseFloor',
        on_delete=models.CASCADE,
        verbose_name='Этаж',
        related_name='messages',
        blank=True,
        null=True,
    )
    flat = models.ForeignKey(
        'admin_panel.Flat',
        on_delete=models.CASCADE,
        verbose_name='Квартира',
        related_name='messages',
        blank=True,
        null=True,
    )
    sender = models.CharField(
        max_length=100,
        verbose_name='Отправитель',
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    @classmethod
    def get_messages_list(cls):
        return cls.objects.all()

    @classmethod
    def get_message(cls, pk):
        return cls.objects.get(pk=pk)

    @property
    def recipient(self):
        result = [
            str(point)
            for point in (self.house, self.section, self.floor, self.flat)
            if point
        ]
        if result:
            return ', '.join(result)
        else:
            return 'Всем'

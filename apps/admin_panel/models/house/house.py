from django.db import models


class House(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        blank=False,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=150,
        blank=False,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['-editing_date', ]

    def __str__(self):
        return f'Дом : {self.name}'

    @classmethod
    def get_houses_count(cls):
        return cls.objects.all().count()

    @classmethod
    def get_houses_list(cls):
        return cls.objects.all()

    @classmethod
    def get_house_by_pk(cls, pk):
        return cls.objects.get(pk=pk)


class HousePreview(models.Model):

    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='house_preview',
        null=True,
    )
    image = models.ImageField(
        upload_to='images/house/preview/',
        verbose_name='Изображение',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Дом: {self.house} - изображение: {self.id}'

    @classmethod
    def get_queryset_all_images(cls, pk):
        return cls.objects.filter(house=pk)

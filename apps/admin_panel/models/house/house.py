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


class HousePreview(models.Model):

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='house_preview',
        default=None,
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/house/preview/',
        verbose_name='Изображение',
    )

    def __str__(self):
        return f'Дом: {self.house} - изображение: {self.id}'

    @staticmethod
    def get_queryset_all_images(pk):
        return HousePreview.objects.filter(house=pk)

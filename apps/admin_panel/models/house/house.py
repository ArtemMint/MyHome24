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

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return f'Дом : {self.name}'


class HousePreview(models.Model):

    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='house',
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/house/preview/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return f'Дом: {self.house} - изображение: {self.id}'

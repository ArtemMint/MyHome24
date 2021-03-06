from django.db import models


class HouseFloor(models.Model):
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='house_floor',
        default=None,
    )
    name = models.CharField(
        verbose_name="Номер этажа",
        max_length=50,
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_floor_list(cls):
        return cls.objects.all()

    @classmethod
    def get_floor_count(cls, pk):
        return cls.objects.filter(house=pk).count()

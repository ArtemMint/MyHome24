from django.db import models

from admin_panel.models import House


class HouseSection(models.Model):
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='house_sections',
        default=None,
    )
    name = models.CharField(
        verbose_name="Название секции",
        max_length=50,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_sections_count(pk):
        return HouseSection.objects.filter(house=pk).count()

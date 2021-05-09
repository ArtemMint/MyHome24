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
        verbose_name="Название",
        max_length=50,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

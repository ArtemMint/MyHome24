from django.db import models


class HouseSection(models.Model):
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='house_sections',
        default=None,
    )
    name = models.CharField(
        verbose_name="Название секции",
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

    def get_sections_count(self, pk):
        return self.objects.filter(house=pk).count()

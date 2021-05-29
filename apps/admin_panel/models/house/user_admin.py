from django.db import models


class HouseUserAdmin(models.Model):
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='house_user_admin',
        default=None,
    )
    name = models.CharField(
        verbose_name="ФИО",
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

    @staticmethod
    def get_user_admin_list(pk):
        return HouseUserAdmin.objects.filter(house=pk)
